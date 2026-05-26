#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动修复day177-day188.html文件的格式问题
问题：
1. footer-support div位置错误（在</html>之后）
2. JavaScript格式不符合day001.html标准（缺少correct属性，函数实现不同）
3. HTML中某些class名称错误
"""

import re
import os

def fix_file(filepath):
    """修复单个文件的格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 问题1：修复footer-support位置（在</html>之后）
    # 找到</html>之后的footer-support，将其移到</body>之前
    footer_pattern = r'</html>\s*<div class="footer-support">\s*技术支持：闫胜君视光工作室\s*</div>'
    footer_match = re.search(footer_pattern, content, re.DOTALL)
    if footer_match:
        # 移除错误的footer
        content = content.replace(footer_match.group(0), '</html>')
        # 在</body>前添加正确的footer
        content = content.replace('</body>', '    </div>\n\n    <!-- 底部技术支持署名 -->\n    <div class="footer-support">\n        技术支持：闫胜君视光工作室\n    </div>\n\n</body>')
    
    # 问题2：修复JavaScript中的choiceQuestions格式
    # 2.1 为每个选项添加correct属性
    def add_correct_to_options(match):
        """为options数组中的每个对象添加correct属性"""
        options_str = match.group(0)
        # 找到answer数组
        answer_pattern = r'answer:\s*\[(.*?)\]'
        answer_match = re.search(answer_pattern, content[max(0, match.start()-500):match.end()+100])
        if not answer_match:
            return options_str
        
        answer_indices = [int(x.strip()) for x in answer_match.group(1).split(',') if x.strip()]
        
        # 为每个option添加correct属性
        def replace_option(m):
            idx = int(m.group(1))
            is_correct = idx in answer_indices
            # 检查是否已有correct或isCorrect属性
            if 'correct:' in m.group(0) or 'isCorrect:' in m.group(0):
                return m.group(0)  # 已有属性，不修改
            # 添加correct属性
            return m.group(0).replace('{ text:', '{ text:', 1).replace(' }', f', correct: {"true" if is_correct else "false"} }}')
        
        # 这个正则表达式可能不准确，让我用更简单的方法
        return options_str
    
    # 更简单的方法：直接重写整个JavaScript部分
    # 找到<script>标签开始的位置
    script_start = content.find('<script>')
    if script_start == -1:
        print(f"  [跳过] 未找到<script>标签: {filepath}")
        return False
    
    script_end = content.find('</script>', script_start)
    if script_end == -1:
        print(f"  [跳过] 未找到</script>标签: {filepath}")
        return False
    
    # 提取JavaScript内容
    js_content = content[script_start+8:script_end]
    
    # 检查是否已经是day001.html格式（有correct属性）
    if "'correct':" in js_content or '"correct":' in js_content:
        print(f"  [跳过] 已经是正确格式: {filepath}")
        return False
    
    # 需要重写JavaScript
    # 提取choiceQuestions数据
    choice_questions_match = re.search(r'const choiceQuestions = \[(.*?)\];', js_content, re.DOTALL)
    if not choice_questions_match:
        print(f"  [跳过] 未找到choiceQuestions: {filepath}")
        return False
    
    # 由于自动转换复杂，我们跳过这个文件，让它保持原样
    # 或者我们可以尝试一个更简单的方法：直接替换整个文件
    print(f"  [需要手动修复] JavaScript格式不正确: {filepath}")
    return False

def main():
    files_to_fix = [f'day{i}.html' for i in range(177, 189)]  # day177-day188
    
    print("=" * 60)
    print("自动修复day177-day188.html格式")
    print("=" * 60)
    
    fixed_count = 0
    skip_count = 0
    manual_count = 0
    
    for filename in files_to_fix:
        filepath = os.path.join('d:\\365培训', filename)
        if not os.path.exists(filepath):
            print(f"[跳过] 文件不存在: {filename}")
            skip_count += 1
            continue
        
        print(f"\n处理: {filename}")
        result = fix_file(filepath)
        
        if result == True:
            fixed_count += 1
        elif result == False:
            # 需要检查具体情况
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查footer位置
            if '</html>' in content and 'footer-support' in content.split('</html>')[1] if len(content.split('</html>')) > 1 else False:
                print(f"  [问题] footer位置错误")
                manual_count += 1
            elif 'toggleReference' in content:
                print(f"  [问题] JavaScript使用toggleReference（需要改为showReference）")
                manual_count += 1
            else:
                skip_count += 1
    
    print("\n" + "=" * 60)
    print(f"处理完成:")
    print(f"  自动修复: {fixed_count} 个")
    print(f"  需要手动修复: {manual_count} 个")
    print(f"  跳过: {skip_count} 个")
    print("=" * 60)

if __name__ == '__main__':
    main()
