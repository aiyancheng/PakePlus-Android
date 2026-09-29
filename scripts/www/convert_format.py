#!/usr/bin/env python3
"""
批量转换365培训HTML文件格式
从旧格式（checkAnswer + data-correct）转换为新格式（initChoiceQuestions + choiceQuestions数组）
"""

import re
import os

def extract_choice_questions(html_content):
    """从HTML中提取选择题数据"""
    # 找到所有选择题卡片
    pattern = r'<div class="question-card" data-correct="([^"]*)" data-explanation="([^"]*)">.*?</div>'
    # 使用非贪婪匹配和dotall模式
    pattern = r'<div class="question-card" data-correct="([^"]*)" data-explanation="(.*?)">'
    
    questions = []
    
    # 更简单的提取方法：按行处理
    lines = html_content.split('\n')
    in_question = False
    current_question = None
    
    for i, line in enumerate(lines):
        # 检测选择题开始
        if 'class="question-card" data-correct=' in line:
            in_question = True
            # 提取正确答案和解释
            correct_match = re.search(r'data-correct="([^"]*)"', line)
            explanation_match = re.search(r'data-explanation="([^"]*)"', line)
            
            if correct_match and explanation_match:
                correct_answer = correct_match.group(1)
                explanation = explanation_match.group(1)
                current_question = {
                    'correct': correct_answer,
                    'explanation': explanation,
                    'text': '',
                    'options': []
                }
        
        elif in_question:
            # 提取题目文本
            if 'class="question-text"' in line:
                text_match = re.search(r'>(.*?)</div>', line)
                if text_match:
                    current_question['text'] = text_match.group(1)
            
            # 提取选项
            elif 'class="option-text"' in line:
                text_match = re.search(r'>(.*?)</span>', line)
                value_match = re.search(r'value="([^"]*)"', line)
                if text_match and value_match:
                    current_question['options'].append({
                        'text': text_match.group(1),
                        'value': value_match.group(1)
                    })
            
            # 检测选择题结束（提交按钮后）
            elif 'class="feedback"' in line and current_question:
                questions.append(current_question)
                current_question = None
                in_question = False
    
    return questions

def convert_html_file(file_path):
    """转换单个HTML文件"""
    print(f"正在处理: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经是新格式
    if 'initChoiceQuestions' in content:
        print(f"  跳过（已是新格式）: {file_path}")
        return False
    
    # 提取选择题数据
    choice_questions = extract_choice_questions(content)
    
    if not choice_questions:
        print(f"  警告：未找到选择题数据: {file_path}")
        return False
    
    print(f"  找到 {len(choice_questions)} 道选择题")
    
    # 生成新的练习题区HTML
    new_practice_html = generate_practice_html(choice_questions)
    
    # 生成新的JavaScript
    new_javascript = generate_javascript(choice_questions)
    
    # 替换练习题区
    # 找到练习题区的开始和结束位置
    practice_start = content.find('<!-- ===== 练习题区 ===== -->')
    practice_end = content.find('<!-- 底部导航按钮区 -->')
    
    if practice_start == -1 or practice_end == -1:
        print(f"  错误：找不到练习题区标记: {file_path}")
        return False
    
    # 替换练习题区
    new_content = content[:practice_start] + new_practice_html + content[practice_end:]
    
    # 替换JavaScript部分
    script_start = new_content.find('<script>')
    script_end = new_content.find('</script>')
    
    if script_start == -1 or script_end == -1:
        print(f"  错误：找不到JavaScript标记: {file_path}")
        return False
    
    new_content = new_content[:script_start] + '<script>\n' + new_javascript + '\n    </script>\n' + new_content[script_end + len('</script>'):]
    
    # 替换底部署名
    footer_pattern = r'<div style="text-align: center; padding: 20px; color: #999; font-size: 14px;">\s*技术支持：闫胜君视光工作室\s*</div>'
    new_content = re.sub(footer_pattern, '<div class="footer-support">\n        技术支持：闫胜君视光工作室\n    </div>', new_content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  转换完成: {file_path}")
    return True

def generate_practice_html(choice_questions):
    """生成新的练习题区HTML"""
    html = '''        <!-- ===== 练习题区 ===== -->
        <div class="practice-section">
            <div class="section-title">练习题</div>
'''
    
    # 添加选择题
    for i, q in enumerate(choice_questions):
        question_num = i + 1
        html += f'''            <!-- 选择题{question_num} -->
            <div class="choice-question">
                <div class="question-text">{question_num}. {q['text']}</div>
                <div class="question-meta">单选题 · 10分</div>
                <ul class="options-list"></ul>
                <div class="feedback"></div>
            </div>
'''
    
    # 添加问答题（这里需要手动处理，因为问答题格式各异）
    html += '''
            <!-- 问答题部分需要手动调整 -->
        </div>
'''
    
    return html

def generate_javascript(choice_questions):
    """生成新的JavaScript代码"""
    js = '''        // ========== 选择题数据 ==========
        const choiceQuestions = [
'''
    
    for i, q in enumerate(choice_questions):
        # 确定正确答案的索引
        correct_value = q['correct']  # 如 "B"
        correct_index = ord(correct_value) - ord('A')
        
        js += f'''            {{
                type: 'single',
                options: [
'''
        
        for j, opt in enumerate(q['options']):
            js += f'''                    {{ text: '{opt["text"]}' }},
'''
        
        js += f'''                ],
                answer: [{correct_index}],
                score: 10,
                explanation: '{q["explanation"]}'
            }},
'''
    
    js += '''        ];

        // ========== 初始化选择题 ==========
        function initChoiceQuestions() {
            const containers = document.querySelectorAll('.choice-question');
            containers.forEach((container, idx) => {
                const q = choiceQuestions[idx];
                if (!q) return;
                const optionsList = container.querySelector('.options-list');
                const isMulti = q.type === 'multi';
                q.options.forEach((opt, optIdx) => {
                    const li = document.createElement('li');
                    li.className = 'option-item';
                    li.dataset.qidx = idx;
                    li.dataset.optidx = optIdx;
                    const marker = document.createElement('div');
                    marker.className = 'option-marker';
                    marker.textContent = String.fromCharCode(65 + optIdx);
                    const text = document.createElement('span');
                    text.className = 'option-text';
                    text.textContent = opt.text;
                    li.appendChild(marker);
                    li.appendChild(text);
                    li.addEventListener('click', () => toggleOption(idx, optIdx, isMulti));
                    optionsList.appendChild(li);
                });
            });
        }

        function toggleOption(qIdx, optIdx, isMulti) {
            const container = document.querySelectorAll('.choice-question')[qIdx];
            const item = container.querySelectorAll('.option-item')[optIdx];
            if (isMulti) { item.classList.toggle('selected'); }
            else { container.querySelectorAll('.option-item').forEach(li => li.classList.remove('selected')); item.classList.add('selected'); }
        }

        function getSelectedIndices(qIdx) {
            const container = document.querySelectorAll('.choice-question')[qIdx];
            const selected = [];
            container.querySelectorAll('.option-item.selected').forEach(li => selected.push(parseInt(li.dataset.optidx)));
            return selected.sort((a, b) => a - b);
        }

        // ========== 提交判分 ==========
        function submitAll() {
            let totalScore = 0;
            choiceQuestions.forEach((q, qIdx) => {
                const container = document.querySelectorAll('.choice-question')[qIdx];
                const selected = getSelectedIndices(qIdx);
                const correct = q.answer.slice().sort((a, b) => a - b);
                const isCorrect = JSON.stringify(selected) === JSON.stringify(correct);
                container.querySelectorAll('.option-item').forEach(li => li.classList.remove('correct', 'wrong'));
                container.querySelector('.feedback')?.classList.remove('show');
                q.options.forEach((opt, optIdx) => {
                    const li = container.querySelectorAll('.option-item')[optIdx];
                    if (correct.includes(optIdx)) li.classList.add('correct');
                    if (selected.includes(optIdx) && !correct.includes(optIdx)) li.classList.add('wrong');
                });
                const feedback = container.querySelector('.feedback');
                if (feedback) {
                    feedback.classList.add('show');
                    if (isCorrect) {
                        feedback.className = 'feedback correct-feedback show';
                        feedback.innerHTML = '✅ 回答正确！' + (q.explanation || '');
                        totalScore += q.score || 10;
                    } else {
                        feedback.className = 'feedback wrong-feedback show';
                        const correctLetters = correct.map(i => String.fromCharCode(65 + i)).join('、');
                        feedback.innerHTML = '❌ 回答错误。正确答案：' + correctLetters + '。' + (q.explanation || '');
                    }
                } else { if (isCorrect) totalScore += q.score || 10; }
            });
            const scoreDisplay = document.getElementById('scoreDisplay');
            const scoreNumber = document.getElementById('scoreNumber');
            const maxScore = choiceQuestions.reduce((sum, q) => sum + (q.score || 10), 0);
            scoreDisplay.classList.add('show');
            scoreNumber.textContent = totalScore + '/' + maxScore + '分';
            scoreDisplay.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        // ========== 问答题：显示参考答案 ==========
        function showReference(btnId, answerId) {
            const answerDiv = document.getElementById(answerId);
            const btn = document.getElementById(btnId);
            if (answerDiv.classList.contains('show')) {
                answerDiv.classList.remove('show');
                btn.textContent = '📖 查看参考答案';
            } else {
                answerDiv.classList.add('show');
                btn.textContent = '🙈 隐藏参考答案';
            }
        }

        document.addEventListener('DOMContentLoaded', () => { initChoiceQuestions(); });
'''
    
    return js

def main():
    """主函数"""
    # 需要转换的文件列表
    files_to_convert = [
        'day088.html', 'day089.html', 'day090.html', 'day091.html', 'day092.html',
        'day093.html', 'day094.html', 'day095.html', 'day096.html', 'day097.html',
        'day099.html', 'day100.html', 'day101.html', 'day102.html', 'day103.html',
        'day104.html'
    ]
    
    base_dir = r'd:\365培训'
    
    success_count = 0
    fail_count = 0
    
    for file_name in files_to_convert:
        file_path = os.path.join(base_dir, file_name)
        
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            fail_count += 1
            continue
        
        try:
            if convert_html_file(file_path):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"处理失败 {file_name}: {str(e)}")
            fail_count += 1
    
    print(f"\n转换完成！成功: {success_count}, 失败: {fail_count}")

if __name__ == '__main__':
    main()