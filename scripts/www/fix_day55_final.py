#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复Day_55_练习题.html，正确修改参考答案显示逻辑
"""
import re
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 文件路径
file_path = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第8周_结业冲刺与毕业考核\Day_55_练习题.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修复1: 正确修复考核说明的插入位置
# 先删除之前错误插入的内容
if '<div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2);' in content:
    # 找到错误插入的内容并删除
    pattern = r'<div class="section" style="background: linear-gradient\(135deg, #fff3e0, #ffe0b2\);[\s\S]*?</div>\s*</div>\s*</div>\s*<div class="value">20题</div>'
    # 用正则表达式替换
    content = re.sub(pattern, '<div class="value">20题</div>', content)

# 在考试信息后正确插入考核说明
exam_info_end = content.find('</div>', content.find('<div class="exam-info">')) + 6
if exam_info_end != -1:
    new_note = '''
  <div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-left: 4px solid #ff9800; margin-bottom: 25px;">
    <div style="text-align: center; padding: 12px;">
      <strong style="color: #e65100;">📝 考核说明：</strong>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">本次为综合模拟考核，请认真作答。</p>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">完成所有题目后，点击"提交模拟考核"按钮，系统将自动评分并显示所有题目的参考答案。</p>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">点击"重新开始"可重置考核，重新练习。</p>
    </div>
  </div>
'''
    content = content[:exam_info_end] + new_note + content[exam_info_end:]

# 修复2: 正确替换所有"查看答案"和"查看参考答案"按钮
# 单选题的按钮
for i in range(1, 11):
    # 查找类似 <button class="show-answer-btn" onclick="toggleAnswer('ans_q1')">查看答案</button>
    pattern = f'<button class="show-answer-btn" onclick="toggleAnswer\\([\'"]ans_q{i}[\'"]\\)">查看答案</button>'
    replacement = f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border:2px solid #ddd;border-radius:20px;padding:6px 16px;font-size:13px;text-align:center;margin-top:10px;">✓ 提交考核后查看答案</div>'
    content = re.sub(pattern, replacement, content)

# 简答题的按钮 (11-20)
for i in range(11, 21):
    pattern = f'<button class="show-answer-btn" onclick="toggleAnswer\\([\'"]ans_q{i}[\'"]\\)">查看参考答案</button>'
    replacement = f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border:2px solid #ddd;border-radius:20px;padding:6px 16px;font-size:13px;text-align:center;margin-top:10px;">✓ 提交考核后查看参考答案</div>'
    content = re.sub(pattern, replacement, content)

# 修复3: 移除或修复之前不完整的替换
# 查找并修复类似 '✓ 提交模拟考核后查看参考答案</div>(\'ans_q11\')">查看参考答案</button>' 的不完整替换
pattern = r'✓ 提交模拟考核后查看参考答案</div>\([\'"].*?[\'"]\)">查看参考答案</button>'
content = re.sub(pattern, '', content)

pattern2 = r'✓ 提交模拟考核后查看参考答案</div>\([\'"].*?[\'"]\)">查看答案</button>'
content = re.sub(pattern2, '', content)

# 修复4: 确保JavaScript中的calculateScore函数包含showAllAnswers调用
if 'function calculateScore()' in content:
    if 'showAllAnswers();' not in content:
        # 在分数计算后添加showAllAnswers调用
        pattern = r'(document\.getElementById\(\'analysisSection\'\)\.style\.display = \'block\';\s*[\s\S]*?board\.scrollIntoView)'
        replacement = r'\1\n  \n  // 新功能：提交考核后显示所有题目的参考答案\n  showAllAnswers();\n  '
        content = re.sub(pattern, replacement, content, count=1)

# 修复5: 添加showAllAnswers函数（如果不存在）
if 'function showAllAnswers()' not in content:
    # 在script结束前添加函数
    script_end = content.rfind('</script>')
    if script_end != -1:
        show_all_function = '''
function showAllAnswers() {
  // 显示所有单选题的答案 (1-10)
  for(let i = 1; i <= 10; i++) {
    const ansBox = document.getElementById('ans_q' + i);
    if(ansBox) {
      ansBox.style.display = 'block';
    }
  }
  
  // 显示所有简答题的答案 (11-20)
  for(let i = 11; i <= 20; i++) {
    const ansBox = document.getElementById('ans_q' + i);
    if(ansBox) {
      ansBox.style.display = 'block';
    }
  }
  
  // 在反馈信息中添加提示
  const feedbackText = document.getElementById('feedbackText');
  if(feedbackText) {
    feedbackText.innerHTML += '<br><br><strong>📖 考核完成！所有题目参考答案已显示在下方，请仔细对照学习。</strong>';
  }
}

function hideAllAnswers() {
  // 重置时隐藏所有答案
  for(let i = 1; i <= 20; i++) {
    const ansBox = document.getElementById('ans_q' + i);
    if(ansBox) {
      ansBox.style.display = 'none';
    }
  }
}

// 修改resetAll函数，重置时也隐藏所有答案
const originalResetAll = window.resetAll || function(){};
window.resetAll = function() {
  originalResetAll();
  hideAllAnswers();
};
'''
        content = content[:script_end] + show_all_function + content[script_end:]

# 修复6: 确保selectOption函数不自动显示答案
# 查找并移除interactive-options-type-c-patch部分
patch_start = content.find('/* interactive-options-type-c-patch */')
if patch_start != -1:
    patch_end = content.find('\n</script>', patch_start)
    content = content[:patch_start] + content[patch_end:]

# 保存修改
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ 文件修复完成：{file_path}")
print("修复内容：")
print("1. 修正了考核说明的插入位置")
print("2. 正确替换了所有'查看答案'按钮")
print("3. 修复了不完整的按钮替换")
print("4. 确保提交考核后显示所有参考答案")
print("5. 添加了showAllAnswers和hideAllAnswers函数")
print("6. 移除了自动显示答案的补丁代码")