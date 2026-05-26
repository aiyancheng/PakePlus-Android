#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复格式问题脚本
修复内容：
1. 添加缺少的技术支持署名
2. 修复标题格式
3. 添加缺少的nav-bottom div
"""

import re
import os

TRAINING_DIR = r'd:\365培训'

def fix_file_format(file_path, day_num):
    """修复单个文件的格式问题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    modifications = []
    
    # 1. 修复缺少技术支持署名
    if '技术支持：闫胜君视光工作室' not in content:
        # 在</body>前添加署名
        if '</body>' in content:
            support_text = '\n    <!-- 底部技术支持署名 -->\n    <div style="text-align: center; padding: 20px; color: #999; font-size: 14px;">\n        技术支持：闫胜君视光工作室\n    </div>\n'
            content = content.replace('</body>', support_text + '</body>')
            modified = True
            modifications.append('添加技术支持署名')
    
    # 2. 修复标题格式
    title_pattern = r'<title>第{}天 \| .+ - 365天眼镜门店员工晋级培训</title>'.format(day_num)
    if not re.search(title_pattern, content):
        # 尝试修复标题
        old_title_match = re.search(r'<title>.*?</title>', content)
        if old_title_match:
            old_title = old_title_match.group(0)
            # 提取主题部分
            title_content = old_title_match.group(0)[7:-8]  # 去掉<title>和</title>
            
            # 尝试提取主题
            if '|' in title_content:
                parts = title_content.split('|')
                if len(parts) >= 2:
                    topic = parts[1].strip()
                    new_title = '<title>第{}天 | {} - 365天眼镜门店员工晋级培训</title>'.format(day_num, topic)
                    content = content.replace(old_title, new_title)
                    modified = True
                    modifications.append('修复标题格式')
            elif '-' in title_content:
                parts = title_content.split('-')
                if len(parts) >= 2:
                    topic = parts[1].strip()
                    new_title = '<title>第{}天 | {} - 365天眼镜门店员工晋级培训</title>'.format(day_num, topic)
                    content = content.replace(old_title, new_title)
                    modified = True
                    modifications.append('修复标题格式')
    
    # 3. 修复缺少nav-bottom div
    if '<div class="nav-bottom">' not in content:
        # 在</div> (container结束)前添加nav-bottom
        # 找到最后一个</div>之前的位置
        container_end = content.rfind('</div>\n</body>')
        if container_end == -1:
            container_end = content.rfind('</body>')
        
        if container_end != -1:
            prev_day = day_num - 1
            next_day = day_num + 1
            
            # 确保天数在1-365范围内
            prev_link = '<a href="day{:03d}.html" class="nav-arrow">← 第{}天</a>'.format(prev_day, prev_day) if prev_day >= 1 else ''
            next_link = '<a href="day{:03d}.html" class="nav-arrow">第{}天 →</a>'.format(next_day, next_day) if next_day <= 365 else ''
            
            nav_html = '\n\n        <!-- 底部导航按钮区 -->\n        <div class="nav-bottom">\n            {}\n            {}\n        </div>\n'.format(prev_link, next_link)
            
            content = content[:container_end] + nav_html + content[container_end:]
            modified = True
            modifications.append('添加nav-bottom div')
    
    # 保存修改
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, modifications
    
    return False, []

def main():
    print('开始批量修复格式问题...')
    print('')
    
    # 需要修复的文件列表（根据检查结果）
    problem_files = [
        'day008.html', 'day009.html', 'day010.html', 'day016.html',
        'day071.html', 'day072.html', 'day073.html', 'day074.html', 'day075.html',
        'day085.html', 'day086.html', 'day087.html', 'day088.html', 'day089.html',
        'day090.html', 'day091.html', 'day092.html', 'day093.html', 'day094.html',
        'day095.html', 'day096.html', 'day097.html', 'day098.html', 'day099.html',
        'day100.html', 'day101.html', 'day102.html', 'day103.html', 'day104.html',
        'day154.html', 'day155.html', 'day156.html', 'day157.html', 'day158.html',
        'day159.html', 'day160.html', 'day161.html', 'day176.html', 'day177.html',
        'day212.html', 'day213.html', 'day214.html', 'day215.html', 'day216.html',
        'day217.html', 'day218.html', 'day219.html', 'day220.html', 'day221.html',
        'day222.html', 'day223.html'
    ]
    
    fixed_count = 0
    fix_details = []
    
    for filename in problem_files:
        file_path = os.path.join(TRAINING_DIR, filename)
        if not os.path.exists(file_path):
            print(f'文件不存在: {filename}')
            continue
        
        # 提取天数
        day_match = re.search(r'day(\d+)\.html', filename)
        if not day_match:
            continue
        day_num = int(day_match.group(1))
        
        # 修复文件
        was_modified, modifications = fix_file_format(file_path, day_num)
        
        if was_modified:
            fixed_count += 1
            fix_details.append((filename, modifications))
            print(u'√ {0} (第{1}天): {2}'.format(filename, day_num, ', '.join(modifications)))
        else:
            print(u'* {0} (第{1}天): 无需修改或无法自动修复'.format(filename, day_num))
    
    print('')
    print('========== 修复完成 ==========')
    print(f'总共修复了 {fixed_count} 个文件')
    print('')
    
    # 保存详细报告
    report_path = os.path.join(TRAINING_DIR, 'format_fix_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('格式问题修复报告\n')
        f.write('生成时间: {}\n'.format(__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        f.write('\n')
        f.write('总共修复了 {} 个文件\n'.format(fixed_count))
        f.write('\n')
        f.write('========== 修复详情 ==========\n')
        
        for filename, modifications in fix_details:
            f.write('\n{}: {}\n'.format(filename, ', '.join(modifications)))
    
    print(f'详细报告已保存到: {report_path}')

if __name__ == '__main__':
    main()
