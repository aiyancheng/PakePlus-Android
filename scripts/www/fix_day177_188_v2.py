#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动修复day177-day188.html文件的格式问题
主要修复：
1. footer-support位置（移到</body>前）
2. JavaScript中的choiceQuestions添加correct属性
3. 替换JavaScript函数为day001.html标准格式
"""

import re
import os

# day001.html标准JavaScript模板（只包含函数部分，不包括choiceQuestions数据）
STANDARD_JS_FUNCTIONS = '''
    <script>
        // ========== 选择题数据 ==========
        const choiceQuestions = [
            %CHOICE_QUESTIONS_DATA%
        ];

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
    </script>
'''

def extract_choice_questions(js_content):
    """从JavaScript内容中提取choiceQuestions数据，并转换为标准格式（添加correct属性）"""
    # 找到choiceQuestions数组
    match = re.search(r'const choiceQuestions = \[(.*?)\];', js_content, re.DOTALL)
    if not match:
        return None
    
    questions_str = match.group(1)
    
    # 解析每个question对象
    # 使用正则表达式找到每个{...}块
    question_blocks = re.findall(r'\{\s*type:.*?\}', questions_str, re.DOTALL)
    
    if not question_blocks:
        return None
    
    result_questions = []
    for q_block in question_blocks:
        # 提取type
        type_match = re.search(r"type:\s*'(single|multi)'", q_block)
        q_type = type_match.group(1) if type_match else 'single'
        
        # 提取options
        options_match = re.search(r'options:\s*\[(.*?)\]', q_block, re.DOTALL)
        if not options_match:
            continue
        options_str = options_match.group(1)
        
        # 提取每个option
        option_items = re.findall(r'\{\s*text:\s*[\'"](.*?)[\'"].*?\}', options_str, re.DOTALL)
        
        # 提取answer
        answer_match = re.search(r'answer:\s*\[(.*?)\]', q_block)
        answer_indices = []
        if answer_match:
            answer_str = answer_match.group(1)
            answer_indices = [int(x.strip()) for x in answer_str.split(',') if x.strip()]
        
        # 构建新的options（带correct属性）
        new_options = []
        for idx, opt_text in enumerate(option_items):
            is_correct = idx in answer_indices
            new_options.append(f"                    {{ text: '{opt_text}', correct: {str(is_correct).lower()} }}")
        
        # 提取score
        score_match = re.search(r'score:\s*(\d+)', q_block)
        score = score_match.group(1) if score_match else '10'
        
        # 提取explanation
        explanation_match = re.search(r'explanation:\s*[\'"](.*?)[\'"]', q_block, re.DOTALL)
        explanation = explanation_match.group(1) if explanation_match else ''
        
        # 构建question对象
        q_obj = f"""            {{
                type: '{q_type}',
                options: [
{chr(10).join(new_options)}
                ],
                answer: [{', '.join(map(str, answer_indices))}],
                score: {score},
                explanation: '{explanation}'
            }}"""
        
        result_questions.append(q_obj)
    
    return ',\n'.join(result_questions)

def fix_html_structure(html_content):
    """修复HTML结构问题"""
    # 问题1：修复footer-support位置
    # 找到</html>之后的footer-support，将其移到</body>之前
    footer_pattern = r'</html>\s*<div class="footer-support">\s*技术支持：闫胜君视光工作室\s*</div>'
    footer_match = re.search(footer_pattern, html_content, re.DOTALL)
    if footer_match:
        # 移除错误的footer
        html_content = html_content.replace(footer_match.group(0), '</html>')
        # 在</body>前添加正确的footer
        html_content = html_content.replace('</body>', '    \n    <!-- 底部技术支持署名 -->\n    <div class="footer-support">\n        技术支持：闫胜君视光工作室\n    </div>\n\n</body>')
    
    return html_content

def fix_file(filepath):
    """修复单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 步骤1：修复HTML结构
    content = fix_html_structure(content)
    
    # 步骤2：提取并修复JavaScript
    # 找到<script>标签
    script_start = content.find('<script>')
    if script_start == -1:
        print(f"  [跳过] 未找到<script>标签")
        return False
    
    script_end = content.find('</script>', script_start)
    if script_end == -1:
        print(f"  [跳过] 未找到</script>标签")
        return False
    
    # 提取JavaScript内容
    js_content = content[script_start+8:script_end]
    
    # 检查是否已经是标准格式
    if 'function showReference' in js_content and "'correct':" in js_content:
        print(f"  [跳过] 已经是标准格式")
        return False
    
    # 提取并转换choiceQuestions数据
    new_questions_data = extract_choice_questions(js_content)
    if new_questions_data is None:
        print(f"  [跳过] 无法提取choiceQuestions数据")
        return False
    
    # 生成新的JavaScript
    new_js = STANDARD_JS_FUNCTIONS.replace('%CHOICE_QUESTIONS_DATA%', new_questions_data)
    
    # 替换原JavaScript
    content = content[:script_start] + new_js + content[script_end+9:]
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [成功] 已修复")
    return True

def main():
    files_to_fix = [f'day{i}.html' for i in range(177, 189)]  # day177-day188
    
    print("=" * 60)
    print("自动修复day177-day188.html格式")
    print("=" * 60)
    
    fixed_count = 0
    skip_count = 0
    error_count = 0
    
    for filename in files_to_fix:
        filepath = os.path.join('d:\\365培训', filename)
        if not os.path.exists(filepath):
            print(f"\n[跳过] 文件不存在: {filename}")
            skip_count += 1
            continue
        
        print(f"\n处理: {filename}")
        try:
            result = fix_file(filepath)
            if result:
                fixed_count += 1
            else:
                skip_count += 1
        except Exception as e:
            print(f"  [错误] {e}")
            error_count += 1
    
    print("\n" + "=" * 60)
    print(f"处理完成:")
    print(f"  成功修复: {fixed_count} 个")
    print(f"  跳过: {skip_count} 个")
    print(f"  错误: {error_count} 个")
    print("=" * 60)

if __name__ == '__main__':
    main()
