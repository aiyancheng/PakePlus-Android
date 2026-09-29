#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动化修复类型B文件（缺少标准JavaScript函数）
类型B特征：
- 使用choiceQuestions数组
- 但initChoiceQuestions()实现不同（用<input>）
- 缺少toggleOption()和getSelectedIndices()
- showReference()签名不同
"""

import re
import sys

def fix_type_b_file(filepath):
    """修复单个类型B文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 修复JavaScript部分
        # 找到<script>标签内的内容
        script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
        if not script_match:
            print(f"  [WARN] 未找到<script>标签: {filepath}")
            return False
        
        script_content = script_match.group(1)
        
        # 2. 提取choiceQuestions数组
        choice_questions_match = re.search(r'const choiceQuestions = (\[.*?\]);', script_content, re.DOTALL)
        if not choice_questions_match:
            print(f"  [WARN] 未找到choiceQuestions数组: {filepath}")
            return False
        
        choice_questions_str = choice_questions_match.group(1)
        
        # 3. 重写JavaScript部分为day001.html标准格式
        new_script_content = f'''    <script>
        // 选择题数据
        const choiceQuestions = {choice_questions_str};

        // 初始化选择题
        function initChoiceQuestions() {{
            const containers = document.querySelectorAll('.choice-question');
            containers.forEach((container, idx) => {{
                const q = choiceQuestions[idx];
                if (!q) return;
                
                const optionsList = container.querySelector('.options-list');
                optionsList.innerHTML = '';
                
                q.options.forEach((opt, optIdx) => {{
                    const li = document.createElement('li');
                    li.className = 'option-item';
                    li.textContent = opt.text;
                    li.setAttribute('data-index', optIdx);
                    li.onclick = () => toggleOption(li, idx, optIdx);
                    optionsList.appendChild(li);
                }});
            }});
        }}

        // 切换选项
        function toggleOption(li, qIdx, optIdx) {{
            const container = li.parentElement.parentElement;
            const q = choiceQuestions[qIdx];
            
            if (q.type === 'single') {{
                container.querySelectorAll('.option-item').forEach(el => el.classList.remove('selected'));
                li.classList.add('selected');
            }} else {{
                li.classList.toggle('selected');
            }}
        }}

        // 获取选中的索引
        function getSelectedIndices(container) {{
            return Array.from(container.querySelectorAll('.option-item.selected'))
                .map(el => parseInt(el.getAttribute('data-index')))
                .sort();
        }}

        // 提交判分
        function submitAll() {{
            let totalScore = 0;
            const containers = document.querySelectorAll('.choice-question');
            
            containers.forEach((container, idx) => {{
                const q = choiceQuestions[idx];
                if (!q) return;
                
                const selected = getSelectedIndices(container);
                const correct = [...q.answer].sort();
                const feedback = container.querySelector('.feedback');
                
                if (JSON.stringify(selected) === JSON.stringify(correct)) {{
                    feedback.innerHTML = '<div class="feedback-correct">回答正确！得分 +' + q.score + '分</div>';
                    totalScore += q.score;
                }} else {{
                    const correctText = q.answer.map(i => q.options[i].text).join('、');
                    feedback.innerHTML = `<div class="feedback-wrong">回答错误。正确答案：${{correctText}}<br>解析：${{q.explanation}}</div>`;
                }}
            }});
            
            const totalScoreElement = document.getElementById('scoreDisplay');
            if (totalScoreElement) {{
                totalScoreElement.innerHTML = `<h3>总分：${{totalScore}} / 30 分</h3><p>选择题正确率：${{totalScore / 30 * 100}}%</p>`;
            }}
        }}

        // 显示参考答案
        function showReference(btn, refId) {{
            const answerDiv = document.getElementById(refId);
            if (answerDiv.style.display === 'block') {{
                answerDiv.style.display = 'none';
                btn.textContent = '查看参考答案';
            }} else {{
                answerDiv.style.display = 'block';
                btn.textContent = '隐藏参考答案';
            }}
        }}

        // 页面加载时初始化
        window.onload = function() {{
            initChoiceQuestions();
        }};
    </script>'''
        
        # 替换整个<script>标签内容
        content = re.sub(r'<script>.*?</script>', new_script_content, content, flags=re.DOTALL)
        
        # 4. 修复练习题区HTML结构（如果有多余的<input>标签）
        # 删除练习题区中的<input>标签
        content = re.sub(r'<input[^>]*>', '', content)
        
        # 5. 修复showReference调用（从showReference(btnId, answerId)改为showReference(this, 'answerId')）
        content = re.sub(r"showReference\('([^']+)',\s*'([^']+)'\)", r"showReference(this, '\2')", content)
        
        # 6. 修复底部结构（技术支持署名和nav-bottom应该在</div>之后）
        # 找到</div>\n</body>模式，在其中插入技术支持和nav-bottom
        # 这个比较复杂，先跳过，手动处理
        
        # 写回文件
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [OK] 已修复: {filepath}")
            return True
        else:
            print(f"  [WARN] 内容未变化: {filepath}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] 错误: {filepath} - {str(e)}")
        return False

def main():
    """主函数"""
    # 类型B文件列表
    type_b_files = [
        'day071.html', 'day072.html', 'day073.html', 'day074.html',
        'day075.html', 'day076.html', 'day077.html', 'day078.html',
        'day079.html', 'day080.html', 'day081.html', 'day082.html',
        'day083.html', 'day084.html', 'day177.html',
        'day332.html', 'day333.html', 'day334.html', 'day335.html',
        'day339.html', 'day340.html'
    ]
    
    print("=" * 60)
    print("类型B文件自动化修复脚本")
    print("=" * 60)
    print()
    
    success_count = 0
    fail_count = 0
    
    for filename in type_b_files:
        filepath = f"d:/365培训/{filename}"
        print(f"处理: {filename}")
        if fix_type_b_file(filepath):
            success_count += 1
        else:
            fail_count += 1
        print()
    
    print("=" * 60)
    print(f"修复完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    print("=" * 60)

if __name__ == '__main__':
    main()
