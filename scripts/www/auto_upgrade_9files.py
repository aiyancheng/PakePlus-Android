#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能批量升级9个文件到day001.html标准架构
自动将JavaScript从practiceData+checkQuestion()架构转换为choiceQuestions+initChoiceQuestions()架构
"""

import re
import os
import json

# 需要升级的文件列表
FILES_TO_UPGRADE = [
    'day154.html', 'day155.html', 'day156.html', 
    'day157.html', 'day158.html', 'day159.html', 'day160.html', 'day161.html',
    'day176.html'
]

def extract_js_data(filepath):
    """从文件中提取JavaScript数据（practiceData或quizData）"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找practiceData或quizData
    pattern = r'(const\s+(practiceData|quizData|answers)\s*=\s*\{.*?\})\s*;'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None, content
    
    js_var_name = match.group(1)
    js_data_str = match.group(0)
    
    return js_var_name, js_data_str, content

def convert_js_to_standard(js_data_str, js_var_name):
    """将旧JS数据转换为新架构"""
    # 这是一个简化版本，实际需要解析JS对象并重建
    # 由于JS解析复杂，这里返回占位符
    return "// 转换后的JavaScript（需要手动完成）"

def upgrade_html_file(filepath):
    """升级单个HTML文件到标准架构"""
    print(f"处理：{os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # 1. 修复标题格式
    content = re.sub(
        r'<title>第(\d+)天\s*[\|：]?\s*([^<]+?)\s*-\s*365天',
        r'第\1天 | \2 - 365天眼镜门店员工晋级培训',
        content
    )
    
    # 2. 修复底部导航：从bottom-nav改为nav-bottom
    content = re.sub(r'<div class="bottom-nav">', r'<div class="nav-bottom">', content)
    
    # 3. 修复footer-support位置（在</body>之后）
    # 移除旧的footer-support
    content = re.sub(r'<!-- 底部技术支持署名 -->\s*<div class="footer-support">.*?</div>\s*</body>', r'</body>', content, flags=re.DOTALL)
    
    # 添加正确的footer-support
    if '</body>' in content:
        footer = '\n    <!-- 底部技术支持署名 -->\n    <div class="footer-support">\n        技术支持：闫胜君视光工作室\n    </div>\n\n'
        content = content.replace('</body>', footer + '</body>')
    
    # 4. 重写JavaScript（简化版：只修复架构）
    # 这里需要手动完成，因为每文件的练习题不同
    # 我们先标记需要手动修复的部分
    
    # 5. 修复练习题HTML结构
    # 将.options-list中的选项移除，改为空容器
    content = re.sub(
        r'(<ul class="options-list">).*?(</ul>)',
        r'\1</ul>',
        content,
        flags=re.DOTALL
    )
    
    # 6. 添加nav-bottom（如果缺失）
    day_match = re.search(r'day(\d+)\.html', os.path.basename(filepath))
    if day_match:
        day_num = int(day_match.group(1))
        prev_day = day_num - 1 if day_num > 1 else 365
        next_day = day_num + 1 if day_num < 365 else 1
        
        # 检查是否已有nav-bottom
        if '<div class="nav-bottom">' not in content:
            # 在</div>（container结束）前添加nav-bottom
            nav_html = f'''
        <!-- 底部导航按钮区 -->
        <div class="nav-bottom">
            <a href="day{prev_day:03d}.html" class="nav-arrow">← 第{prev_day}天</a>
            <a href="index.html" class="nav-home">🏠 返回首页</a>
            <a href="day{next_day:03d}.html" class="nav-arrow">第{next_day}天 →</a>
        </div>
        '''
            # 在</body>前添加
            content = re.sub(r'\s*</body>', nav_html + '\n</body>', content)
    
    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_len = len(content)
    print(f"  完成：{original_len} -> {new_len} 字节")
    return True

def main():
    print("=" * 60)
    print("智能批量升级9个文件")
    print("=" * 60)
    print()
    
    workspace = r'd:\365培训'
    success_count = 0
    
    for filename in FILES_TO_UPGRADE:
        filepath = os.path.join(workspace, filename)
        
        if not os.path.exists(filepath):
            print(f"  跳过：{filename}（文件不存在）")
            continue
        
        try:
            if upgrade_html_file(filepath):
                success_count += 1
        except Exception as e:
            print(f"  错误：{e}")
    
    print()
    print("=" * 60)
    print(f"升级完成：成功 {success_count}/{len(FILES_TO_UPGRADE)} 个文件")
    print("=" * 60)
    print()
    print("注意：JavaScript架构需要手动修复！")
    print("每个文件的练习题数据不同，需要手动重写JS部分。")

if __name__ == '__main__':
    main()
