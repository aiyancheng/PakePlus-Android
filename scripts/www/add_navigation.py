#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为眼镜门店培训课程HTML文件添加导航按钮
- 为学习内容文件添加：← 返回前一天练习题 / 今日练习题 → (或下一天)
- 为练习题文件添加：← 返回学习内容 / 下一天学习内容 →
"""

import os
import re

BASE = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'

# 颜色主题映射（按天数范围）
def get_color(day):
    if day <= 7: return ('#667eea', '#764ba2')
    elif day <= 14: return ('#11998e', '#38ef7d')
    elif day <= 21: return ('#f7971e', '#ffd200')
    elif day <= 28: return ('#fa709a', '#fee140')
    elif day <= 35: return ('#4facfe', '#00f2fe')
    elif day <= 42: return ('#43e97b', '#38f9d7')
    elif day <= 49: return ('#f093fb', '#f5576c')
    else: return ('#a18cd1', '#fbc2eb')

def make_nav_css(c1, c2):
    return f"""
  .nav-footer {{ display: flex; justify-content: space-between; align-items: center; padding: 20px 0 30px; gap: 12px; }}
  .nav-btn {{ display: inline-flex; align-items: center; padding: 12px 24px; border-radius: 30px; font-size: 14px; font-weight: 600; text-decoration: none; transition: all 0.25s; color: white; background: linear-gradient(135deg, {c1}, {c2}); }}
  .nav-btn:hover {{ opacity: 0.85; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
  .nav-btn.outline {{ background: white; color: {c1}; border: 2px solid {c1}; }}
  .nav-btn.outline:hover {{ background: #f9f9f9; }}"""

def make_nav_html(left_href, left_text, right_href, right_text):
    return f"""
  <div class="nav-footer">
    <a href="{left_href}" class="nav-btn outline">{left_text}</a>
    <a href="{right_href}" class="nav-btn">{right_text}</a>
  </div>"""

def add_nav_to_file(filepath, nav_css, nav_html):
    """向文件添加导航"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有导航
    if 'nav-footer' in content:
        print(f"  [已有导航，跳过]: {os.path.basename(filepath)}")
        return False
    
    # 添加CSS（插入到</style>前）
    if '</style>' in content:
        content = content.replace('</style>', nav_css + '\n</style>', 1)
    
    # 添加导航按钮（插入到</body>前）
    if '</body>' in content:
        content = content.replace('</body>', nav_html + '\n</body>', 1)
    else:
        content += nav_html
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [已添加导航]: {os.path.basename(filepath)}")
    return True

# 周文件夹映射
week_folders = {
    range(22, 29): '第4周_销售话术与中期考核',
    range(29, 36): '第5周_实战跟岗训练',
    range(36, 43): '第6周_独立接单训练',
    range(43, 50): '第7周_综合提升训练',
    range(50, 57): '第8周_结业冲刺与毕业考核',
}

def get_folder(day):
    for r, folder in week_folders.items():
        if day in r:
            return folder
    return None

def get_filepath(day, ftype):
    """ftype: '学习内容' or '练习题' or '中期考核' or '结业考核'"""
    folder = get_folder(day)
    if not folder:
        return None
    return os.path.join(BASE, folder, f'Day_{day:02d}_{ftype}.html')

# 检查文件是否存在
def file_exists(path):
    return path and os.path.exists(path)

# 处理特殊文件名
special_names = {
    28: '中期考核',
}

def get_display_name(day):
    return special_names.get(day, None)

# 批量处理第4周 Day22-27 学习内容
print("=== 处理第4周 学习内容 ===")
for day in range(22, 28):
    c1, c2 = get_color(day)
    nav_css = make_nav_css(c1, c2)
    
    filepath = get_filepath(day, '学习内容')
    if not file_exists(filepath):
        print(f"  [不存在]: Day_{day:02d}_学习内容.html")
        continue
    
    # 导航：← 前一天练习题(如果存在) / 今日练习题 →
    prev_day = day - 1
    prev_folder = get_folder(prev_day)
    prev_folder_cur = get_folder(day)
    
    if prev_folder == prev_folder_cur:
        left_href = f'Day_{prev_day:02d}_练习题.html'
    else:
        left_href = f'../{"第3周_专业技能训练" if day==22 else ""}/Day_{prev_day:02d}_练习题.html'
    
    left_text = f'← Day {prev_day} 练习题'
    right_href = f'Day_{day:02d}_练习题.html'
    right_text = f'Day {day} 练习题 →'
    
    nav_html = make_nav_html(left_href, left_text, right_href, right_text)
    add_nav_to_file(filepath, nav_css, nav_html)

# 处理第4周 Day27 学习内容
print("\n=== 处理第4周 Day27 学习内容 ===")
day = 27
c1, c2 = get_color(day)
filepath = get_filepath(day, '学习内容')
if file_exists(filepath):
    nav_css = make_nav_css(c1, c2)
    nav_html = make_nav_html(
        f'Day_{day-1:02d}_练习题.html', f'← Day {day-1} 练习题',
        f'Day_{day:02d}_练习题.html', f'Day {day} 练习题 →'
    )
    add_nav_to_file(filepath, nav_css, nav_html)

# 处理第5-8周所有文件
print("\n=== 处理第5-8周 所有文件 ===")
for day in range(29, 57):
    folder = get_folder(day)
    if not folder:
        continue
    
    c1, c2 = get_color(day)
    nav_css = make_nav_css(c1, c2)
    
    # 处理学习内容文件
    study_file = get_filepath(day, '学习内容')
    if file_exists(study_file):
        prev_day = day - 1
        prev_folder = get_folder(prev_day)
        
        if prev_folder == folder:
            left_href = f'Day_{prev_day:02d}_练习题.html'
        elif prev_day == 28:
            left_href = f'../第4周_销售话术与中期考核/Day_28_中期考核.html'
        else:
            prev_f = get_folder(prev_day)
            left_href = f'../{prev_f}/Day_{prev_day:02d}_练习题.html'
        
        left_text = f'← Day {prev_day}'
        right_href = f'Day_{day:02d}_练习题.html'
        right_text = f'Day {day} 练习题 →'
        
        nav_html = make_nav_html(left_href, left_text, right_href, right_text)
        add_nav_to_file(study_file, nav_css, nav_html)
    
    # 处理练习题文件
    quiz_file = get_filepath(day, '练习题')
    if file_exists(quiz_file):
        next_day = day + 1
        next_folder = get_folder(next_day)
        
        left_href = f'Day_{day:02d}_学习内容.html'
        left_text = f'← 返回学习内容'
        
        if next_folder == folder:
            right_href = f'Day_{next_day:02d}_学习内容.html'
            right_text = f'Day {next_day} 学习内容 →'
        elif next_day <= 56:
            right_href = f'../{next_folder}/Day_{next_day:02d}_学习内容.html'
            right_text = f'Day {next_day} 学习内容 →'
        else:
            right_href = f'../第8周_结业冲刺与毕业考核/结业考核.html'
            right_text = '结业考核 →'
        
        nav_html = make_nav_html(left_href, left_text, right_href, right_text)
        add_nav_to_file(quiz_file, nav_css, nav_html)

print("\n✅ 批量导航添加完成！")
