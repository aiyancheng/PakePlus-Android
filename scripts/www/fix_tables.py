#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有dayXXX.html文件中的表格格式
目标：将所有<table>标签添加class="comparison-table"
"""

import os
import re

TRAINING_DIR = r'd:\365培训'
DAY_PATTERN = re.compile(r'^day(\d+)\.html$')

def fix_file_tables(file_path):
    """修复单个文件的表格"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 查找所有<table标签
    table_pattern = re.compile(r'<table([^>]*)>')
    
    def replace_table(match):
        nonlocal modified
        attrs = match.group(1)
        
        # 检查是否已经有class="comparison-table"
        if 'class="comparison-table"' in attrs or "class='comparison-table'" in attrs:
            return match.group(0)  # 已经有正确的class
        
        modified = True
        
        # 检查是否已有class属性
        class_match = re.search(r'class\s*=\s*["\']([^"\']*)["\']', attrs)
        if class_match:
            # 已有class，替换为comparison-table
            new_attrs = re.sub(r'class\s*=\s*["\'][^"\']*["\']', 
                             'class="comparison-table"', attrs)
            return '<table' + new_attrs + '>'
        else:
            # 没有class，添加class="comparison-table"
            new_attrs = ' class="comparison-table"' + attrs
            return '<table' + new_attrs + '>'
    
    new_content = table_pattern.sub(replace_table, content)
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    print('开始修复表格格式...')
    print('目标: 所有<table>标签添加class="comparison-table"')
    print()
    
    files = []
    for f in os.listdir(TRAINING_DIR):
        if DAY_PATTERN.match(f):
            files.append(f)
    
    files.sort(key=lambda x: int(DAY_PATTERN.match(x).group(1)))
    
    print(f'找到 {len(files)} 个dayXXX.html文件')
    print()
    
    fixed_count = 0
    fixed_files = []
    
    for file in files:
        file_path = os.path.join(TRAINING_DIR, file)
        try:
            if fix_file_tables(file_path):
                fixed_count += 1
                fixed_files.append(file)
        except Exception as e:
            print(f'处理 {file} 时出错: {e}')
    
    print('========== 修复完成 ==========')
    print(f'总共修复了 {fixed_count} 个文件')
    print()
    
    if fixed_files:
        print('修复的文件列表（前20个）:')
        for i, f in enumerate(fixed_files[:20]):
            print(f'  - {f}')
        if len(fixed_files) > 20:
            print(f'  ... 还有 {len(fixed_files) - 20} 个文件')
    
    # 保存报告
    report_path = os.path.join(TRAINING_DIR, 'table_fix_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('表格格式修复报告\n')
        f.write('生成时间: ' + str(__import__('datetime').datetime.now()) + '\n')
        f.write('\n')
        f.write(f'总共修复了 {fixed_count} 个文件\n')
        f.write('\n')
        f.write('========== 修复的文件列表 ==========\n')
        f.write('\n')
        for file in fixed_files:
            f.write(file + '\n')
    
    print()
    print(f'详细报告已保存到: {report_path}')

if __name__ == '__main__':
    main()
