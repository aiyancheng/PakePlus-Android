#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复类型C文件：删除练习题区的<h4>标题标签
类型C文件：day016, day212-day218
问题：练习题区有<h4>标题（day001.html没有h4）
"""

import re
import os

# 类型C文件列表
type_c_files = [
    'day016.html',
    'day212.html', 'day213.html', 'day214.html', 'day215.html',
    'day216.html', 'day217.html', 'day218.html'
]

def fix_type_c_file(filepath):
    """修复单个类型C文件：删除练习题区的h4标签"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # 找到练习题区的开始位置
    practice_start = content.find('<div class="practice-section">')
    if practice_start == -1:
        print(f"  [WARN] 未找到practice-section，跳过")
        return False
    
    # 找到练习题区的结束位置（nav-bottom之前）
    nav_bottom_start = content.find('<div class="nav-bottom">', practice_start)
    if nav_bottom_start == -1:
        print(f"  [WARN] 未找到nav-bottom，跳过")
        return False
    
    # 只处理练习题区的内容
    practice_section = content[practice_start:nav_bottom_start]
    
    # 删除练习题区内的所有<h4>和</h4>标签
    # 注意：只删除练习题区内的，不删除学习内容区的
    modified_practice = re.sub(r'<h4[^>]*>.*?</h4>', '', practice_section, flags=re.DOTALL)
    
    # 检查是否有修改
    if modified_practice == practice_section:
        print(f"  [INFO] 练习题区内未找到h4标签")
        return False
    
    # 替换原内容
    new_content = content[:practice_start] + modified_practice + content[nav_bottom_start:]
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    modified_len = len(new_content)
    print(f"  [OK] 已修复（删除h4标签，文件大小：{original_len} -> {modified_len}字节）")
    return True

def main():
    workspace = r'd:\365培训'
    
    print("=" * 60)
    print("修复类型C文件：删除练习题区的<h4>标题标签")
    print("=" * 60)
    print()
    
    success_count = 0
    
    for filename in type_c_files:
        filepath = os.path.join(workspace, filename)
        print(f"处理：{filename}")
        
        if not os.path.exists(filepath):
            print(f"  [SKIP] 文件不存在，跳过")
            continue
        
        try:
            if fix_type_c_file(filepath):
                success_count += 1
        except Exception as e:
            print(f"  [ERROR] 错误：{e}")
    
    print()
    print("=" * 60)
    print(f"修复完成：成功 {success_count}/{len(type_c_files)} 个文件")
    print("=" * 60)

if __name__ == '__main__':
    main()
