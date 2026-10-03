#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量为眼镜门店培训课程HTML文件添加导航按钮（只处理缺少nav-footer的文件）"""

import os

BASE = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'

# 颜色主题
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
    return (
        '\n  .nav-footer { display: flex; justify-content: space-between; align-items: center; '
        'padding: 20px 0 30px; gap: 12px; }\n'
        f'  .nav-btn {{ display: inline-flex; align-items: center; padding: 12px 24px; '
        f'border-radius: 30px; font-size: 14px; font-weight: 600; text-decoration: none; '
        f'transition: all 0.25s; color: white; background: linear-gradient(135deg, {c1}, {c2}); }}\n'
        f'  .nav-btn:hover {{ opacity: 0.85; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}\n'
        f'  .nav-btn.outline {{ background: white; color: {c1}; border: 2px solid {c1}; }}\n'
        f'  .nav-btn.outline:hover {{ background: #f9f9f9; }}'
    )

def make_nav_html(left_href, left_text, right_href, right_text):
    return (
        '\n<div class="container">\n'
        '  <div class="nav-footer">\n'
        f'    <a href="{left_href}" class="nav-btn outline">{left_text}</a>\n'
        f'    <a href="{right_href}" class="nav-btn">{right_text}</a>\n'
        '  </div>\n'
        '</div>'
    )

def add_nav(filepath, nav_css, nav_html):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'nav-footer' in content:
        print(f'  [已有导航，跳过] {os.path.basename(filepath)}')
        return False
    # 添加CSS
    if '</style>' in content:
        content = content.replace('</style>', nav_css + '\n</style>', 1)
    # 添加导航HTML
    if '</body>' in content:
        content = content.replace('</body>', nav_html + '\n</body>', 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  [已添加] {os.path.basename(filepath)}')
    return True

# 文件夹映射
WEEK_MAP = {
    range(15, 22): '第3周_专业技能训练',
    range(22, 29): '第4周_销售话术与中期考核',
    range(29, 36): '第5周_实战跟岗训练',
    range(36, 43): '第6周_独立接单训练',
    range(43, 50): '第7周_综合提升训练',
    range(50, 57): '第8周_结业冲刺与毕业考核',
}

def get_folder(day):
    for r, folder in WEEK_MAP.items():
        if day in r: return folder
    return None

def get_path(day, ftype):
    folder = get_folder(day)
    if not folder: return None
    return os.path.join(BASE, folder, f'Day_{day:02d}_{ftype}.html')

def exists(p): return p and os.path.exists(p)

# ========== 第3周 Day17-21 学习内容 ==========
print('\n=== 第3周 Day17-21 学习内容 ===')
for day in range(17, 22):
    c1, c2 = get_color(day)
    fp = get_path(day, '学习内容')
    if not exists(fp): continue
    # 学习内容导航：← 前一天练习题 / 今日练习题 →
    if day == 17:
        left = ('Day_16_练习题.html', '← Day 16 练习题')
    else:
        left = (f'Day_{day-1:02d}_练习题.html', f'← Day {day-1} 练习题')
    right = (f'Day_{day:02d}_练习题.html', f'Day {day} 练习题 →')
    add_nav(fp, make_nav_css(c1, c2), make_nav_html(left[0], left[1], right[0], right[1]))

# ========== 第4周 Day22-27 学习内容 ==========
print('\n=== 第4周 Day22-27 学习内容 ===')
for day in range(22, 28):
    c1, c2 = get_color(day)
    fp = get_path(day, '学习内容')
    if not exists(fp): continue
    if day == 22:
        left = ('../第3周_专业技能训练/Day_21_练习题.html', '← Day 21 练习题')
    else:
        left = (f'Day_{day-1:02d}_练习题.html', f'← Day {day-1} 练习题')
    right = (f'Day_{day:02d}_练习题.html', f'Day {day} 练习题 →')
    add_nav(fp, make_nav_css(c1, c2), make_nav_html(left[0], left[1], right[0], right[1]))

# ========== 第5-8周 所有文件 ==========
for week_range, week_name in [
    (range(29, 36), '第5周_实战跟岗训练'),
    (range(36, 43), '第6周_独立接单训练'),
    (range(43, 50), '第7周_综合提升训练'),
    (range(50, 57), '第8周_结业冲刺与毕业考核'),
]:
    print(f'\n=== {week_name} ===')
    for day in week_range:
        c1, c2 = get_color(day)
        folder = get_folder(day)

        # 学习内容
        fp = get_path(day, '学习内容')
        if exists(fp):
            prev = day - 1
            prev_folder = get_folder(prev)
            if prev_folder == folder:
                left = (f'Day_{prev:02d}_练习题.html', f'← Day {prev} 练习题')
            elif prev == 28:
                left = ('../第4周_销售话术与中期考核/Day_28_中期考核.html', '← 中期考核')
            else:
                left = (f'../{prev_folder}/Day_{prev:02d}_练习题.html', f'← Day {prev} 练习题')
            right = (f'Day_{day:02d}_练习题.html', f'Day {day} 练习题 →')
            add_nav(fp, make_nav_css(c1, c2), make_nav_html(left[0], left[1], right[0], right[1]))

        # 练习题
        qt_name = '练习题'
        # Day 56 特殊：练习题 -> 结业考核
        fp_quiz = get_path(day, qt_name)
        if not exists(fp_quiz):
            # 尝试结业考核文件名
            alt = os.path.join(BASE, '第8周_结业冲刺与毕业考核', 'Day_56_结业考核.html')
            if exists(alt):
                fp_quiz = alt
                qt_name = '结业考核'

        if exists(fp_quiz):
            left = (f'Day_{day:02d}_学习内容.html', '← 返回学习内容')
            nxt = day + 1
            nxt_folder = get_folder(nxt)
            if nxt_folder == folder:
                right = (f'Day_{nxt:02d}_学习内容.html', f'Day {nxt} 学习内容 →')
            elif nxt <= 56:
                right = (f'../{nxt_folder}/Day_{nxt:02d}_学习内容.html', f'Day {nxt} 学习内容 →')
            else:
                right = ('../课程总览.html', '🎓 课程总览')
            add_nav(fp_quiz, make_nav_css(c1, c2), make_nav_html(left[0], left[1], right[0], right[1]))

# Day_56 结业考核（如果单独存在）
fp56 = os.path.join(BASE, '第8周_结业冲刺与毕业考核', 'Day_56_结业考核.html')
if exists(fp56):
    c1, c2 = get_color(56)
    add_nav(fp56, make_nav_css(c1, c2), make_nav_html(
        'Day_56_学习内容.html', '← 返回学习内容',
        '../课程总览.html', '🎓 课程总览'
    ))

print('\n✅ 全部完成！')
