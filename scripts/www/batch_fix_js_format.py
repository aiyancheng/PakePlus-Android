#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复day074-day084的JavaScript格式
为choiceQuestions.options添加correct: false/true属性
"""

import re
import os

def fix_choice_questions_js(html_content):
    """修复HTML内容中的choiceQuestions JavaScript"""
    
    # 找到JavaScript中的choiceQuestions数组
    # 使用更智能的方法：找到数组开始和结束
    
    # 方法：找到 "const choiceQuestions = [" 的位置
    start_marker = 'const choiceQuestions = ['
    start_idx = html_content.find(start_marker)
    if start_idx == -1:
        return html_content, False
    
    # 找到匹配的 "]" - 需要处理嵌套
    array_start = start_idx + len(start_marker)
    bracket_count = 1
    pos = array_start
    
    while pos < len(html_content) and bracket_count > 0:
        char = html_content[pos]
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
        pos += 1
    
    # pos现在在 "]" 之后（即数组结束位置+1）
    array_end = pos  # 指向 "]" 后面的位置
    
    # 提取数组内容（包括开始的 "[" 和结束的 "]"）
    array_full = html_content[start_idx:array_end]  # 从 "const choiceQuestions = [" 到 "]"
    
    # 实际上我需要更精确：从 "[" 开始到匹配的 "]" 结束
    # 重新计算
    bracket_start = html_content.find('[', start_idx)
    bracket_count = 1
    bracket_pos = bracket_start + 1
    
    while bracket_pos < len(html_content) and bracket_count > 0:
        char = html_content[bracket_pos]
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
        bracket_pos += 1
    
    array_content_start = bracket_start
    array_content_end = bracket_pos  # 指向 "]" 之后的位置
    
    original_array = html_content[array_content_start:array_content_end]
    
    # 现在解析这个数组，为每个option添加correct属性
    # 使用正则找到所有 answer: [...] 
    answer_pattern = r'answer:\s*\[(.*?)\]'
    answers = re.findall(answer_pattern, original_array)
    
    if not answers:
        return html_content, False
    
    # 处理数组字符串，为每个选项添加correct
    # 找到所有 question 对象（以 { 开头，} 结尾，包含 type:）
    # 更简单：直接处理 options 数组
    
    modified_array = original_array
    
    # 用正则找到所有 options: [ ... ] 块
    options_pattern = r'options:\s*\[(.*?)\]'
    
    # 但这样只能拿到内容，我需要替换整个 options 数组
    # 让我用不同的方法：逐字符解析
    
    # 实际上，我可以用一个更简单的方法：
    # 1. 找到所有 { text: '...' } 
    # 2. 判断这个option是否在answer中
    
    # 但这需要知道每个option的索引...很复杂
    
    # 让我换一个思路：直接字符串替换
    # 对于每个 question，我知道 answer 数组
    # 我可以把每个 options 数组中的 { text: '...' } 替换为 { text: '...', correct: false/true }
    
    # 找到所有独立的 question 块
    question_blocks = re.split(r'(?=\{\s*type:)', original_array[1:-1])  # 跳过开头的 [
    
    new_questions = []
    for q_block in question_blocks:
        if not q_block.strip():
            continue
        
        # 找到这个question的answer
        answer_match = re.search(r'answer:\s*\[(.*?)\]', q_block)
        if not answer_match:
            new_questions.append(q_block)
            continue
        
        answer_str = answer_match.group(1)
        if answer_str.strip():
            correct_indices = [int(x.strip()) for x in answer_str.split(',')]
        else:
            correct_indices = []
        
        # 找到 options 数组
        options_match = re.search(r'options:\s*\[', q_block)
        if not options_match:
            new_questions.append(q_block)
            continue
        
        # 从 options:[ 之后开始，找到匹配的 ]
        opt_start = options_match.end()
        bracket_count = 1
        opt_pos = opt_start
        
        while opt_pos < len(q_block) and bracket_count > 0:
            char = q_block[opt_pos]
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
            opt_pos += 1
        
        options_full = q_block[options_match.start():opt_pos]
        
        # 现在 options_full 是 "options: [ ... ]"
        # 我需要为其中的每个 { text: '...' } 添加 correct
        
        # 找到所有 option 对象
        opt_content_start = options_full.index('[') + 1
        opt_content_end = len(options_full) - 1  # 最后一个 ] 之前
        opt_content = options_full[opt_content_start:opt_content_end]
        
        # 分割每个选项
        # 选项以 { 开头，以 }, 或 } 结尾（最后一个可能没有,）
        opt_objects = []
        current_obj = ''
        brace_count = 0
        
        for char in opt_content:
            if char == '{' and brace_count == 0:
                if current_obj.strip():
                    opt_objects.append(current_obj)
                current_obj = char
                brace_count = 1
            elif char == '{':
                current_obj += char
                brace_count += 1
            elif char == '}':
                current_obj += char
                brace_count -= 1
                if brace_count == 0:
                    opt_objects.append(current_obj)
                    current_obj = ''
            else:
                current_obj += char
        
        # 现在 opt_objects 包含了所有选项的字符串表示
        # 为每个添加 correct
        new_opt_objects = []
        for idx, opt_str in enumerate(opt_objects):
            is_correct = idx in correct_indices
            # 检查是否已经有 correct:
            if 'correct:' in opt_str:
                # 已经有 correct，跳过
                new_opt_objects.append(opt_str)
            else:
                # 添加 correct
                # 在 } 之前添加 , correct: false/true
                new_opt = opt_str.rstrip().rstrip('}').rstrip()
                if new_opt.endswith(','):
                    new_opt = new_opt.rstrip(',')
                new_opt += ', correct: ' + ('true' if is_correct else 'false') + ' }'
                new_opt_objects.append(new_opt)
        
        # 重新组装 options
        new_options_content = ',\n                    '.join(new_opt_objects)
        new_options_full = 'options: [\n                    ' + new_options_content + '\n                ]'
        
        # 替换原 question 块中的 options
        new_q_block = q_block[:options_match.start()] + new_options_full + q_block[opt_pos:]
        new_questions.append(new_q_block)
    
    # 重新组装数组
    new_array = '[' + '\n'.join(new_questions) + '\n    ]'
    
    # 替换原HTML中的数组
    new_html = html_content[:array_content_start] + new_array + html_content[array_content_end:]
    
    return new_html, True

# 主程序
files_to_fix = [f'd:/365培训/day{i:03d}.html' for i in range(74, 85)]  # day074-day084

fixed_count = 0
for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"文件不存在: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, success = fix_choice_questions_js(content)
    
    if success:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] 已修复: {os.path.basename(filepath)}")
        fixed_count += 1
    else:
        print(f"[WARN] 无法修复: {os.path.basename(filepath)}")

print(f"\n总共修复了 {fixed_count} 个文件")
