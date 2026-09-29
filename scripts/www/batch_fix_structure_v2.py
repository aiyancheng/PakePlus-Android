#!/usr/bin/env python3
"""
批量修复HTML文件结构问题 - 简化版
直接字符串替换，不做复杂解析
"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 修复1: nav类名为nav-bottom
    content = content.replace('class="nav-buttons"', 'class="nav-bottom"')
    content = content.replace('class="footer-nav"', 'class="nav-bottom"')
    content = content.replace('class="nav-btn"', 'class="nav-arrow"')
    content = content.replace('class="nav-btn center"', 'class="nav-home"')
    
    # 修复2: essay按钮onclick拼写错误
    # 从 onclick="showReference('essayBtnessayAnswer1', 'essayAnswer1')" 
    # 改为 onclick="showReference('essayBtn1', 'essayAnswer1')"
    content = re.sub(
        r"onclick=\"showReference\(['\"]essayBtnessayAnswer1['\"],\s*['\"]essayAnswer1['\"]\)\"",
        "onclick=\"showReference('essayBtn1', 'essayAnswer1')\"",
        content
    )
    content = content.replace('id="essayBtnessayAnswer1"', 'id="essayBtn1"')
    
    # 修复3: showReference函数旧格式改新格式
    old_fn = '''        // 显示参考答案
        function showReference(btnId, answerId) {
            const answerDiv = document.getElementById(answerId);
            if (answerDiv.style.display === 'block') {
                answerDiv.style.display = 'none';
                btn.textContent = '查看参考答案';
            } else {
                answerDiv.style.display = 'block';
                btn.textContent = '隐藏参考答案';
            }
        }'''
    
    new_fn = '''        // ========== 问答题：显示参考答案 ==========
        function showReference(btnId, answerId) {
            const answerDiv = document.getElementById(answerId);
            const btn = document.getElementById(btnId);
            if (answerDiv.classList.contains('show')) {
                answerDiv.classList.remove('show');
                btn.textContent = '📖 查看参考答案';
            } else {
                answerDiv.classList.add('show');
                btn.textContent = '🙈 隐藏参考答案';
            }
        }'''
    
    if old_fn in content:
        content = content.replace(old_fn, new_fn)
    
    # 修复4: score-display结构
    old_score = '<div class="score-display" id="scoreDisplay"></div>'
    new_score = '''<div class="score-display" id="scoreDisplay">
                <div class="score-number" id="scoreNumber">0分</div>
                <div class="score-text" id="scoreText">本次练习成绩</div>
            </div>'''
    content = content.replace(old_score, new_score)
    
    # 修复5: footer-support位置（在</html>之后 -> 移到</body>之前）
    bad_pattern = '\n</html>\n<!-- 底部技术支持署名 -->\n<div class="footer-support">\n    技术支持：闫胜君视光工作室\n</div>\n'
    if bad_pattern in content:
        content = content.replace(bad_pattern, '\n</html>\n')
        # 在</body>前插入footer-support
        content = content.replace('</body>', '    <!-- 底部技术支持署名 -->\n    <div class="footer-support">\n        技术支持：闫胜君视光工作室\n    </div>\n\n</body>')
    
    # 检查是否有修改
    if content == original:
        return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

if __name__ == '__main__':
    files = []
    for i in list(range(74, 85)) + list(range(177, 189)):
        files.append(f'd:/365培训/day{i:03d}.html')
    
    print(f'开始修复 {len(files)} 个文件...')
    fixed = 0
    for f in files:
        if not os.path.exists(f):
            print(f'  [!] {f} 不存在')
            continue
        try:
            if fix_file(f):
                print(f'  [+] {os.path.basename(f)} 已修复')
                fixed += 1
            else:
                print(f'  [-] {os.path.basename(f)} 无变化')
        except Exception as e:
            print(f'  [!] {os.path.basename(f)} 错误: {e}')
    
    print(f'\n完成！修复了 {fixed} 个文件')
