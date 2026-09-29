#!/usr/bin/env python3
"""
自动修复day071-day084, day177-day188等文件的HTML结构问题
问题包括：
1. nav类名为nav-buttons/footer-nav等，应为nav-bottom
2. 额外的footer div（class="footer"）
3. script在错误位置
4. showReference函数使用旧格式
5. essay question按钮onclick格式错误
6. footer-support在</html>之后
"""

import re
import sys

def fix_file(filepath):
    """修复单个文件的HTML结构问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. 修复nav类名为nav-bottom
    content = re.sub(r'class="nav-buttons"', 'class="nav-bottom"', content)
    content = re.sub(r'class="footer-nav"', 'class="nav-bottom"', content)
    
    # 2. 修复nav内部按钮类名
    content = re.sub(r'class="nav-btn"', 'class="nav-arrow"', content)
    content = re.sub(r'class="nav-btn center"', 'class="nav-home"', content)
    
    # 3. 删除额外的footer div（在container内部的）
    # 匹配 <div class="footer">...</div> 在 </div> 之前的内容
    content = re.sub(r'\n\s*<div class="footer">\s*\n\s*<p>© 2024.*?</p>\s*\n\s*</div>\s*\n', '\n', content)
    
    # 4. 修复essay question按钮onclick（修复拼写错误essayBtnessayAnswer）
    # 格式应为: onclick="showReference('essayBtn1', 'essayAnswer1')"
    content = re.sub(
        r'onclick="showReference\([\'"]essayBtnessayAnswer1[\'"],\s*[\'"]essayAnswer1[\'"]\)"',
        'onclick="showReference(\'essayBtn1\', \'essayAnswer1\')"',
        content
    )
    # 同时修复按钮id
    content = re.sub(r'id="essayBtnessayAnswer1"', 'id="essayBtn1"', content)
    
    # 5. 修复showReference函数（旧格式 -> 新格式）
    old_show_ref = '''        // 显示参考答案
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
    
    new_show_ref = '''        // ========== 问答题：显示参考答案 ==========
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
    
    content = content.replace(old_show_ref, new_show_ref)
    
    # 6. 修复footer-support位置（在</html>之后 -> 移到</body>之前）
    # 先删除错误的footer-support（在</html>之后）
    bad_footer_pattern = r'\n</html>\n<!-- 底部技术支持署名 -->\n<div class="footer-support">\n    技术支持：闫胜君视光工作室\n</div>\n'
    if re.search(bad_footer_pattern, content):
        content = re.sub(bad_footer_pattern, '\n</html>\n', content)
        # 现在需要在</body>之前添加正确的footer-support
        content = content.replace('</body>', '''    <!-- 底部技术支持署名 -->
    <div class="footer-support">
        技术支持：闫胜君视光工作室
    </div>

</body>''')
    
    # 7. 删除重复的nav-bottom（在container之外的）
    # 先找到正确的nav-bottom（在container内部），然后删除重复的
    # 这个比较复杂，暂时跳过，手动处理
    
    # 8. 修复score-display结构（添加score-number和score-text）
    old_score = r'<div class="score-display" id="scoreDisplay"></div>'
    new_score = r'<div class="score-display" id="scoreDisplay">\n                <div class="score-number" id="scoreNumber">0分</div>\n                <div class="score-text" id="scoreText">本次练习成绩</div>\n            </div>'
    content = re.sub(old_score, new_score, content)
    
    # 检查是否有修改
    if content == original_content:
        print(f"  [-] {filepath} - 无变化")
        return False
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] {filepath} - 已修复")
        return True

if __name__ == '__main__':
    import glob
    
    # 需要修复的文件列表
    files_to_fix = []
    
    # day071-day084
    for i in range(71, 85):
        files_to_fix.append(f'd:/365培训/day{i:03d}.html')
    
    # day177-day188
    for i in range(177, 189):
        files_to_fix.append(f'd:/365培训/day{i:03d}.html')
    
    print(f"开始修复 {len(files_to_fix)} 个文件...")
    
    fixed_count = 0
    for filepath in files_to_fix:
        try:
            if fix_file(filepath):
                fixed_count += 1
        except Exception as e:
            print(f"  [!] {filepath} - 错误: {e}")
    
    print(f"\n完成！成功修复 {fixed_count} 个文件")
