#!/usr/bin/env python3
"""
改进版批量修复HTML文件的格式问题
修复内容：
1. JavaScript函数体旧格式（showReference函数）
2. HTML结构问题（提交按钮、得分显示）
3. 底部技术支持署名位置错误
"""

import os
import re
import sys

def fix_javascript_showreference(content):
    """修复JavaScript中的showReference函数 - 改进版"""
    # 查找旧的showReference函数并替换为新版本
    # 模式1: function showReference(btnId, answerId) { ... answerDiv.style.display ... }
    pattern1 = r'function showReference\(btnId, answerId\)\s*\{[^}]*answerDiv\.style\.display[^}]*\}'
    
    replacement1 = '''function showReference(btnId, answerId) {
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
    
    # 使用re.sub进行替换，DOTALL标志让.匹配换行符
    new_content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
    
    # 如果上面没匹配到，尝试其他模式
    if new_content == content:
        # 模式2: 可能函数定义略有不同
        pattern2 = r'function showReference\(btnId, answerId\)\s*\{[^}]*btn\.textContent\s*=\s*[\'"]查看参考答案[\'"][^}]*\}'
        new_content = re.sub(pattern2, replacement1, content, flags=re.DOTALL)
    
    return new_content

def fix_html_submit_structure(content):
    """修复HTML中的提交按钮和得分显示结构"""
    # 模式1: 简单的提交按钮 + scoreDisplay div
    pattern1 = r'(<button class="submit-btn" onclick="submitAll\(\)">)[^<]*(</button>\s*<div id="scoreDisplay"></div>)'
    
    replacement1 = '''<div class="submit-area">
        <button class="submit-btn" onclick="submitAll()">📝 提交答案查看成绩</button>
    </div>

    <!-- 得分显示 -->
    <div class="score-display" id="scoreDisplay">
        <div class="score-number" id="scoreNumber">0分</div>
        <div class="score-text" id="scoreText">本次练习成绩</div>
    </div>'''
    
    new_content = re.sub(pattern1, replacement1, content)
    
    # 如果上面没匹配到，尝试其他模式
    if new_content == content:
        # 模式2: 可能有其他文本内容的提交按钮
        pattern2 = r'(<button class="submit-btn" onclick="submitAll\(\)">)[^<]*(</button>)'
        replacement2 = '''<div class="submit-area">
        <button class="submit-btn" onclick="submitAll()">📝 提交答案查看成绩</button>
    </div>

    <!-- 得分显示 -->
    <div class="score-display" id="scoreDisplay">
        <div class="score-number" id="scoreNumber">0分</div>
        <div class="score-text" id="scoreText">本次练习成绩</div>
    </div>'''
        
        # 只替换第一个匹配（提交按钮），不替换可能存在的其他button
        new_content = re.sub(pattern2, replacement2, content, count=1)
    
    return new_content

def fix_footer_position(content):
    """修复底部技术支持署名的位置"""
    # 查找 </body> 之后的 <div class="footer-support"> 并移动到 </body> 之前
    pattern = r'(</body>\s*</html>)\s*(<!-- 底部技术支持署名 -->\s*<div class="footer-support">\s*技术支持：闫胜君视光工作室\s*</div>)'
    
    replacement = r'\2\n\n\1'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 如果上面没匹配到，尝试其他模式
    if new_content == content:
        # 模式2: 可能格式略有不同
        pattern2 = r'(</body>)(\s*<!-- 底部技术支持署名 -->\s*<div class="footer-support">\s*技术支持：闫胜君视光工作室\s*</div>\s*</html>)'
        replacement2 = r'\2\n\n\1'
        new_content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)
    
    return new_content

def fix_multiple_issues(content):
    """修复多个问题"""
    original_content = content
    
    # 修复JavaScript showReference函数
    content = fix_javascript_showreference(content)
    
    # 修复HTML提交按钮结构
    content = fix_html_submit_structure(content)
    
    # 修复底部署名位置
    content = fix_footer_position(content)
    
    return content

def process_file(file_path):
    """处理单个文件"""
    print(f"处理文件: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 读取文件失败: {e}")
        return False
    
    original_content = content
    
    # 修复多个问题
    content = fix_multiple_issues(content)
    
    # 如果内容有变化，写回文件
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ 已修复")
            return True
        except Exception as e:
            print(f"  ✗ 写入文件失败: {e}")
            return False
    else:
        print(f"  - 无需修复")
        return False

def main():
    """主函数"""
    # 获取要处理的文件列表
    # 先处理已知有问题的文件
    problem_files = [
        "day087.html",  # 测试文件
        # 其他有问题文件将在测试成功后添加
    ]
    
    # 也可以处理所有day*.html文件
    html_files = []
    for i in range(1, 365):
        file_path = f"day{i:03d}.html"
        if os.path.exists(file_path):
            html_files.append(file_path)
    
    print(f"找到 {len(html_files)} 个HTML文件")
    print(f"先测试处理 {len(problem_files)} 个问题文件")
    
    # 先测试处理问题文件
    for file_path in problem_files:
        if os.path.exists(file_path):
            process_file(file_path)
    
    # 如果测试成功，询问是否处理所有文件
    print("\n测试完成。是否处理所有HTML文件？(y/n)")
    # 注意：在实际运行中，这里应该是交互式输入
    # 但在AI助手中，我们应该直接处理或者询问用户
    
    return 0

if __name__ == "__main__":
    sys.exit(main())