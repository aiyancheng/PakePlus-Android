#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复day072-day084的JavaScript格式
为choiceQuestions.options添加correct: false/true属性
"""

import re
import os

# 要修复的文件列表
files_to_fix = [f'day{i:03d}.html' for i in range(72, 85)]  # day072-day084

def fix_js_options(content, filename):
    """修复JavaScript中choiceQuestions的options格式"""
    
    # 找到JavaScript中的choiceQuestions数组
    # 使用正则表达式匹配choiceQuestions数组
    pattern = r'(const choiceQuestions\s*=\s*\[)(.*?)(\];\s*\n\s*//)'
    
    def replace_options(match):
        prefix = match.group(1)  # const choiceQuestions = [
        array_content = match.group(2)  # 数组内容
        suffix = match.group(3)  # ];\n// 
        
        # 处理每个题目
        # 找到所有题目对象
        questions = re.findall(r'\{\s*type:', array_content)
        
        # 更简单的方法：直接处理options数组
        # 将array_content按题目分割
        
        # 用正则找到所有options数组和对应的answer
        # 匹配模式：options: [\n { ... },\n { ... },\n ... ]
        
        # 先找到所有answer数组
        answer_pattern = r'answer:\s*\[(.*?)\]'
        answers = re.findall(answer_pattern, array_content)
        
        # 替换处理
        new_array_content = array_content
        
        # 处理每个options数组
        options_pattern = r'options:\s*\[(.*?)\]'
        
        def process_options(match):
            options_str = match.group(1)
            # 计算这个选项数组有多少个选项
            opt_matches = re.findall(r'\{', options_str)
            num_options = len(opt_matches)
            # 暂时无法知道哪些是正确答案，需要外部信息
            return match.group(0)  # 暂时返回原值
        
        # 这个方法太复杂了，换一个思路
        # 直接手动修复每个文件更快
        return None
    
    result = re.sub(pattern, replace_options, content, flags=re.DOTALL)
    return result

# 由于正则解析JavaScript太复杂，我改用直接读取并手动修复的方式
# 但这里我先输出需要修复的文件列表

print("需要修复的文件：")
for f in files_to_fix:
    filepath = os.path.join('d:\\365培训', f)
    if os.path.exists(filepath):
        print(f"  {f}")
    else:
        print(f"  {f} (文件不存在)")

print("\n由于JavaScript解析复杂，建议手动修复或使用更智能的方法。")
print("我将手动修复这些文件。")
