import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'

def add_home_button(filepath):
    """在导航区中间增加返回首页按钮，支持多种导航结构"""
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    
    # 导航区域查找（多种可能的class名）
    nav_patterns = [
        r'<div[^>]*class="nav-footer"[^>]*>.*?</div>',
        r'<div[^>]*class="nav-footer.*?[^>]*>.*?</div>',
        r'<div[^>]*class="nav-bar"[^>]*>.*?</div>',
        r'<div[^>]*class="nav-bar.*?[^>]*>.*?</div>',
        r'<div[^>]*class=[\'"]nav-footer[\'"][^>]*>.*?</div>',
    ]
    
    nav_html = None
    nav_start = -1
    nav_end = -1
    
    for pattern in nav_patterns:
        match = re.search(pattern, c, re.DOTALL)
        if match:
            nav_html = match.group(0)
            nav_start = match.start()
            nav_end = match.end()
            break
    
    # 如果没找到，可能是简单的nav-footer
    if nav_start == -1:
        # 尝试查找简单的nav-footer
        nav_start = c.find('<div class="nav-footer"')
        if nav_start == -1:
            nav_start = c.find('<div class="nav-bar"')
        if nav_start == -1:
            # 查找无引号的情况
            nav_start = c.find('<div class=nav-footer')
            if nav_start == -1:
                nav_start = c.find('<div class=nav-bar')
        
        if nav_start != -1:
            nav_end = c.find('</div>', nav_start)
            if nav_end != -1:
                nav_end += 6
                nav_html = c[nav_start:nav_end]
    
    if nav_start == -1:
        # 对于没有导航的文件（如index.html），在body结尾前添加导航
        body_end = c.find('</body>')
        if body_end != -1:
            # 添加一个简单的导航栏
            new_nav = '\n<div class="nav-footer" style="margin:30px auto;padding:20px;text-align:center;">\n' + \
                      '  <a class="nav-btn" href="index.html" style="padding:10px 24px;background:#4CAF50;color:white;border-radius:8px;text-decoration:none;">🏠 返回首页</a>\n' + \
                      '</div>\n'
            new_c = c[:body_end] + new_nav + c[body_end:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print(f'  ➕ {os.path.basename(filepath)}: 添加了导航区')
            return True
        else:
            print(f'  ❌ {os.path.basename(filepath)}: 未找到导航区域')
            return False
    
    # 分析导航结构，插入首页按钮
    if 'nav-bar' in nav_html:
        # 第5-8周的结构：中间有页码，左右是按钮
        # 找到中间的页码位置
        if '第5周' in c or '第6周' in c or '第7周' in c or '第8周' in c:
            # 在这个结构中，我们需要添加一个首页按钮在左右按钮之间
            home_btn = '<a href="../index.html" class="nav-btn" style="background:#f0fdf9;color:#11998e;border:1px solid #a7f3d0;padding:8px 20px;border-radius:6px;text-decoration:none;font-size:14px;">🏠 首页</a>'
            
            # 检查是否已经有首页按钮
            if 'index.html' in nav_html or '课程总览' in nav_html or '首页' in nav_html:
                print(f'  ✔ {os.path.basename(filepath)}: 已有首页链接')
                return True
            
            # 在中间位置插入
            nav_parts = nav_html.split('</a>')
            if len(nav_parts) >= 2:
                new_nav = nav_parts[0] + '</a>\n    ' + home_btn + '\n    ' + '</a>'.join(nav_parts[1:])
            else:
                # 备份方案：直接添加
                new_nav = nav_html.replace('</div>', '\n    ' + home_btn + '\n  </div>')
    else:
        # 第1-4周的结构：两个按钮
        home_btn = '<a class="nav-btn outline" href="../index.html">🏠 首页</a>'
        
        # 检查是否已经有首页按钮
        if 'index.html' in nav_html or '课程总览' in nav_html or '首页' in nav_html:
            print(f'  ✔ {os.path.basename(filepath)}: 已有首页链接')
            return True
        
        # 在第一个按钮后插入
        first_a_end = nav_html.find('</a>')
        if first_a_end != -1:
            new_nav = nav_html[:first_a_end+4] + '\n    ' + home_btn + '\n    ' + nav_html[first_a_end+4:]
        else:
            # 备份方案：直接添加
            new_nav = nav_html.replace('</div>', '\n    ' + home_btn + '\n  </div>')
    
    # 应用修改
    new_c = c[:nav_start] + new_nav + c[nav_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    
    print(f'  ✅ {os.path.basename(filepath)}: 添加成功')
    return True

def process_week(week_dir):
    """处理一周内的所有文件"""
    count_ok = 0
    week_name = os.path.basename(week_dir)
    print(f'处理 {week_name} ...')
    
    for fname in sorted(os.listdir(week_dir)):
        if fname.endswith('.html') and ('Day' in fname or '总览' in fname or '考核' in fname):
            fp = os.path.join(week_dir, fname)
            if add_home_button(fp):
                count_ok += 1
    
    return count_ok

# 先处理index.html
index_files = [os.path.join(base, 'index.html'), os.path.join(base, '课程总览.html')]
for idx_file in index_files:
    if os.path.exists(idx_file):
        print(f'处理 {os.path.basename(idx_file)} ...')
        add_home_button(idx_file)

# 处理8周目录
weeks = [
    "第1周_文化与制度启蒙",
    "第2周_光学与产品知识",
    "第3周_专业技能训练",
    "第4周_销售话术与中期考核",
    "第5周_实战跟岗训练",
    "第6周_独立接单训练",
    "第7周_综合提升训练",
    "第8周_结业冲刺与毕业考核",
]

total_ok = 0
for week in weeks:
    week_dir = os.path.join(base, week)
    if os.path.exists(week_dir):
        ok = process_week(week_dir)
        total_ok += ok

print(f'\n总计处理 {total_ok} 个文件')
print('完成！所有学习内容和练习题文件均已添加"返回首页"按钮')
