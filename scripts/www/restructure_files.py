#!/usr/bin/env python3
"""
重构day219-223.html文件，使其符合day001.html标准格式
主要修改：
1. 将<header class="page-header">改为<div class="page-header">
2. 将<main class="learning-card">改为<div class="learning-card">
3. 将<section class="section">改为<div class="learning-section">
4. 添加<div class="container">包裹层
5. 修复标题格式
6. 添加进度条完整结构
7. 修复day-number格式
8. 添加card-header结构
9. 修复summary-card结构
10. 修复底部导航格式
11. 调整footer-support位置
"""

import re
import os

def restructure_html(filepath):
    """重构单个HTML文件，使其符合day001.html标准格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. 提取day编号
    day_match = re.search(r'第(\d+)天', content)
    if not day_match:
        print(f"  ⚠️ 无法提取day编号: {filepath}")
        return False
    day_num = int(day_match.group(1))
    
    # 2. 提取标题
    title_match = re.search(r'<h1[^>]*>第\d+天[：:]\s*([^<]+)</h1>', content)
    if not title_match:
        # 尝试其他格式
        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    title = title_match.group(1).strip() if title_match else "未知标题"
    
    # 3. 重构HTML结构
    # 3.1 添加DOCTYPE和html标签（如果缺失）
    if not content.startswith('<!DOCTYPE html>'):
        content = '<!DOCTYPE html>\n' + content
    
    # 3.2 替换<html lang="zh-CN">（修复大小写）
    content = re.sub(r'<html lang="zh-CN">', '<html lang="zh-CN">', content)
    content = re.sub(r'<html lang="zh-cn">', '<html lang="zh-CN">', content)
    
    # 3.3 替换<head>中的viewport
    content = re.sub(r'initial-scale=1\.0', 'initial-scale=1.0', content)
    
    # 3.4 替换标题格式
    content = re.sub(r'<title>第(\d+)天 \| ([^<]+) - 365天眼镜门店员工晋级培训</title>', 
                    r'<title>第\1天 | \2 - 365天眼镜门店员工晋级培训</title>', content)
    
    # 如果标题格式不对，重写
    if '第' + str(day_num) + '天' in content and '|' not in content:
        # 需要重写标题
        old_title_pattern = r'<title>第\d+天 \| ([^<]+) - 365天眼镜门店员工晋级培训</title>'
        if not re.search(old_title_pattern, content):
            # 标题格式不正确，需要修复
            new_title = f'<title>第{day_num}天 | {title} - 365天眼镜门店员工晋级培训</title>'
            content = re.sub(r'<title>[^<]+</title>', new_title, content)
    
    # 3.5 添加container div（如果缺失）
    if '<div class="container">' not in content:
        # 在<body>后添加<div class="container">
        content = re.sub(r'<body>\s*', '<body>\n    <div class="container">\n', content, count=1)
        # 在</body>前添加</div>（关闭container）
        if '</div>\n\n<!-- 底部技术支持署名 -->' in content:
            # footer-support在container外面，需要调整
            content = re.sub(r'</div>\n\n<!-- 底部技术支持署名 -->', r'</div>\n\n<!-- 底部技术支持署名 -->', content)
        else:
            # 在</body>前添加</div>
            content = re.sub(r'\s*</body>', '\n    </div>\n\n<!-- 底部技术支持署名 -->\n<div class="footer-support">\n    技术支持：闫胜君视光工作室\n</div>\n\n</body>', content)
    
    # 3.6 替换<header class="page-header">为<div class="page-header">
    content = re.sub(r'<header class="page-header">', '<div class="page-header">', content)
    content = re.sub(r'</header>', '</div>', content, count=1)  # 只替换第一个</header>
    
    # 3.7 修复page-header内部结构
    # 替换<h1>第X天：标题</h1>为标准格式
    content = re.sub(r'<h1[^>]*>第(\d+)天[：:]\s*([^<]+)</h1>', 
                    r'<div class="day-number">第 \1 天</div>\n            <h1 class="page-title">\2</h1>', content)
    
    # 替换<p class="subtitle">为<div class="page-subtitle">
    content = re.sub(r'<p class="subtitle">([^<]+)</p>', r'<div class="page-subtitle">模块？：？ · 第？周</div>', content)
    
    # 3.8 添加进度条完整结构（如果缺失）
    if 'progress-bar-label' not in content:
        # 在progress-bar-container内添加label
        progress_bar_pattern = r'(<div class="progress-bar-container">)\s*(<div class="progress-bar"[^>]*>)'
        progress_bar_replacement = r'\1\n            <div class="progress-bar-label">\n                <span>培训进度</span>\n                <span>' + str(day_num) + '/365</span>\n            </div>\n            \2'
        content = re.sub(progress_bar_pattern, progress_bar_replacement, content)
    
    # 3.9 替换<main class="learning-card">为<div class="learning-card">
    content = re.sub(r'<main class="learning-card">', '<div class="learning-card">', content)
    content = re.sub(r'</main>', '</div>', content)  # 替换剩余的</main>
    
    # 3.10 添加card-header（如果缺失）
    if '<div class="card-header">' not in content:
        # 在learning-card后添加card-header
        content = re.sub(r'(<div class="learning-card">)\s*', 
                        r'\1\n            <div class="card-header">\n                <div class="card-icon">📚</div>\n                <div class="card-title">学习内容</div>\n            </div>\n\n', content)
    
    # 3.11 替换<section class="section">为<div class="learning-section">
    content = re.sub(r'<section class="section">', '<div class="learning-section">', content)
    content = re.sub(r'</section>', '</div>', content)  # 替换剩余的</section>
    
    # 3.12 替换<h2 class="section-title">为<h3>（在learning-section内）
    content = re.sub(r'<h2 class="section-title">([^<]+)</h2>', r'<h3>\1</h3>', content)
    
    # 3.13 修复summary部分
    if '<div class="summary-card">' not in content:
        # 查找小结部分并重构
        content = re.sub(r'<h2 class="section-title">[每日小结|每日总结][^<]*</h2>', 
                        r'<div class="summary-card">\n            <div class="summary-title">📝 今日小结</div>', content)
        # 查找</div></main>或类似结构来关闭summary-card
        content = re.sub(r'(</ul>\s*</div>\s*</div>)\s*', r'\1\n        </div>\n', content)
    
    # 3.14 修复底部导航
    content = re.sub(r'class="nav-arrow">← 上一天<', f'class="nav-arrow">← 第{day_num-1}天<', content)
    content = re.sub(r'class="nav-arrow">后一天 →<', f'class="nav-arrow">第{day_num+1}天 →<', content)
    
    # 3.15 确保footer-support在正确位置
    if '<div class="footer-support">' not in content:
        content += '\n\n<div class="footer-support">\n    技术支持：闫胜君视光工作室\n</div>\n'
    
    # 4. 写回文件
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """主函数"""
    files_to_fix = ['day219.html', 'day220.html', 'day221.html', 'day222.html', 'day223.html']
    
    print("开始重构文件...")
    print("目标：使这些文件符合day001.html标准格式")
    print()
    
    success_count = 0
    for filename in files_to_fix:
        filepath = os.path.join(r'd:\365培训', filename)
        if not os.path.exists(filepath):
            print(f"  ⚠️ 文件不存在: {filepath}")
            continue
        
        print(f"处理: {filename}")
        try:
            if restructure_html(filepath):
                print(f"  ✅ 已重构: {filename}")
                success_count += 1
            else:
                print(f"  ⚠️ 无需修改或失败: {filename}")
        except Exception as e:
            print(f"  ❌ 错误: {filename} - {e}")
    
    print()
    print(f"========== 重构完成 ==========")
    print(f"成功重构: {success_count}/{len(files_to_fix)} 个文件")
    print()
    print("注意：由于HTML结构复杂，自动重构可能无法完全符合标准。")
    print("建议手动检查这5个文件，确保格式正确。")

if __name__ == '__main__':
    main()
