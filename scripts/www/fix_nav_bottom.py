#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复nav-bottom格式
将 "← 上一天" / "后一天 →" 改为 "← 第X天" / "第Y天 →"
"""

import os
import re

def fix_nav_bottom(content, day_num):
    """修复单个文件的nav-bottom格式"""
    # 计算前一天和后一天
    prev_day = day_num - 1 if day_num > 1 else 365
    next_day = day_num + 1 if day_num < 365 else 1
    
    # 替换 "← 上一天" 为 "← 第X天"
    # 匹配模式: <a href="dayXXX.html" class="nav-arrow">← 上一天</a>
    pattern_prev = r'<a href="day(\d+)\.html" class="nav-arrow">← 上一天</a>'
    replacement_prev = f'<a href="day{prev_day:03d}.html" class="nav-arrow">← 第{prev_day}天</a>'
    content = re.sub(pattern_prev, replacement_prev, content)
    
    # 也匹配可能的变体: "←上一天" (无空格)
    pattern_prev2 = r'<a href="day(\d+)\.html" class="nav-arrow">←上一天</a>'
    content = re.sub(pattern_prev2, replacement_prev, content)
    
    # 替换 "后一天 →" 为 "第Y天 →"
    # 匹配模式: <a href="dayXXX.html" class="nav-arrow">后一天 →</a>
    pattern_next = r'<a href="day(\d+)\.html" class="nav-arrow">后一天 →</a>'
    replacement_next = f'<a href="day{next_day:03d}.html" class="nav-arrow">第{next_day}天 →</a>'
    content = re.sub(pattern_next, replacement_next, content)
    
    # 也匹配可能的变体: "后一天→" (无空格)
    pattern_next2 = r'<a href="day(\d+)\.html" class="nav-arrow">后一天→</a>'
    content = re.sub(pattern_next2, replacement_next, content)
    
    # 替换 "后一天→" (右箭头在文字前的情况，不太可能但有备无患)
    pattern_next3 = r'<a href="day(\d+)\.html" class="nav-arrow">后一天→</a>'
    content = re.sub(pattern_next3, replacement_next, content)
    
    return content

def main():
    print("=" * 60)
    print("批量修复nav-bottom格式")
    print("=" * 60)
    print()
    
    # 获取所有dayXXX.html文件
    files = [f for f in os.listdir('.') if re.match(r'^day\d+\.html$', f)]
    files.sort(key=lambda x: int(re.match(r'day(\d+)', x).group(1)))
    
    print(f"找到 {len(files)} 个文件")
    print()
    
    success_count = 0
    error_count = 0
    
    for filename in files:
        try:
            # 提取天数
            day_num = int(re.match(r'day(\d+)', filename).group(1))
            
            # 读取文件
            filepath = os.path.join('.', filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修复nav-bottom
            new_content = fix_nav_bottom(content, day_num)
            
            # 如果内容有变化，写回文件
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                success_count += 1
                print(f"  [OK] {filename} (第{day_num}天)")
            else:
                # 没变化，可能是格式已经正确
                print(f"  [SKIP] {filename} (无变化或格式已正确)")
                
        except Exception as e:
            error_count += 1
            print(f"  [ERROR] {filename}: {e}")
    
    print()
    print("=" * 60)
    print(f"修复完成: 成功 {success_count} 个, 失败 {error_count} 个")
    print("=" * 60)

if __name__ == '__main__':
    main()
