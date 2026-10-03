#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终修复Day_55_练习题.html
"""
import re
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 文件路径
file_path = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第8周_结业冲刺与毕业考核\Day_55_练习题.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 删除错误的考核说明（在考试信息内部的）
# 找到考试信息部分
exam_info_start = content.find('<div class="exam-info">')
exam_info_end = content.find('</div>', content.find('</div>', content.find('</div>', exam_info_start + 1) + 1) + 1) + 6

if exam_info_start != -1 and exam_info_end != -1:
    exam_info = content[exam_info_start:exam_info_end]
    
    # 删除第一个考核说明（第76-83行部分）
    exam_info = exam_info.replace(
        '  <div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-left: 4px solid #ff9800; margin-bottom: 25px;">\n    <div style="text-align: center; padding: 12px;">\n      <strong style="color: #e65100;">📝 考核说明：</strong>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">本次为综合模拟考核，请认真作答。</p>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">完成所有题目后，点击"提交模拟考核"按钮，系统将自动评分并显示所有题目的参考答案。</p>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">点击"重新开始"可重置考核，重新练习。</p>\n    </div>\n  </div>\n\n  <div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-left: 4px solid #ff9800;">\n    <div style="text-align: center; padding: 12px;">\n      <strong style="color: #e65100;">📝 考核说明：</strong>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">本次为综合模拟考核，请认真作答。</p>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">完成所有题目后，点击"提交模拟考核"按钮，系统将自动评分并显示所有题目的参考答案。</p>\n      <p style="margin: 8px 0; color: #555; font-size: 14px;">点击"重新开始"可重置考核，重新练习。</p>\n    </div>\n  </div>\n\n      <div class="value">20题</div>',
        '      <div class="value">20题</div>'
    )
    
    # 更新内容
    content = content[:exam_info_start] + exam_info + content[exam_info_end:]

# 2. 在考试信息后插入正确的考核说明
exam_info_end = content.find('</div>', content.find('<div class="exam-info">')) + 6
if exam_info_end != -1:
    # 检查是否已经有考核说明
    if content.find('<div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-left: 4px solid #ff9800;', exam_info_end) == -1:
        note = '''
  <div class="section" style="background: linear-gradient(135deg, #fff3e0, #ffe0b2); border-left: 4px solid #ff9800; margin-bottom: 25px;">
    <div style="text-align: center; padding: 12px;">
      <strong style="color: #e65100;">📝 考核说明：</strong>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">本次为综合模拟考核，请认真作答。</p>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">完成所有题目后，点击"提交模拟考核"按钮，系统将自动评分并显示所有题目的参考答案。</p>
      <p style="margin: 8px 0; color: #555; font-size: 14px;">点击"重新开始"可重置考核，重新练习。</p>
    </div>
  </div>
'''
        content = content[:exam_info_end] + note + content[exam_info_end:]

# 3. 修复不完整的按钮HTML
# 查找并修复所有不完整的按钮
for i in range(1, 21):
    # 查找类似 '<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border-color:#ddd;cursor:default;">\n    </div>'
    pattern = f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border-color:#ddd;cursor:default;">\\s*</div>'
    
    # 修复单选题的按钮 (1-10)
    if i <= 10:
        replacement = f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border:2px solid #ddd;border-radius:20px;padding:6px 16px;font-size:13px;text-align:center;margin-top:10px;cursor:default;">✓ 提交考核后查看答案</div>'
    else:
        # 修复简答题的按钮 (11-20)
        replacement = f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border:2px solid #ddd;border-radius:20px;padding:6px 16px;font-size:13px;text-align:center;margin-top:10px;cursor:default;">✓ 提交考核后查看参考答案</div>'
    
    content = content.replace(f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border-color:#ddd;cursor:default;">\n    </div>', replacement)
    content = content.replace(f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border-color:#ddd;cursor:default;">\n  </div>', replacement)
    content = content.replace(f'<div class="show-answer-btn" style="background:#f8f9fa;color:#888;border-color:#ddd;cursor:default;">', replacement)

# 4. 移除可能残留的onclick属性
content = content.replace('onclick="toggleAnswer', 'style="cursor:default"')

# 5. 确保JavaScript中showAllAnswers函数调用正确
# 检查calculateScore函数中是否有showAllAnswers调用
if 'calculateScore()' in content:
    # 确保在计算分数后调用showAllAnswers
    if 'showAllAnswers();' not in content[content.find('calculateScore()'):content.find('function resetAll()')]:
        # 在calculateScore函数末尾添加调用
        pattern = r'(board\.scrollIntoView\(\{ behavior: \'smooth\' \}\);)'
        replacement = r'\1\n  \n  // 提交考核后显示所有题目的参考答案\n  showAllAnswers();'
        content = re.sub(pattern, replacement, content, count=1)

# 6. 检查并修复showAllAnswers函数
# 如果函数存在但需要改进
if 'function showAllAnswers()' in content:
    # 找到showAllAnswers函数
    func_start = content.find('function showAllAnswers()')
    func_end = content.find('function hideAllAnswers()', func_start)
    
    if func_start != -1 and func_end != -1:
        # 创建改进的函数
        improved_func = '''function showAllAnswers() {
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
}'''
        
        # 替换函数
        content = content[:func_start] + improved_func + content[func_end:]

# 7. 移除toggleAnswer函数，因为不再需要
if 'function toggleAnswer(id)' in content:
    toggle_start = content.find('function toggleAnswer(id)')
    toggle_end = content.find('function calculateScore()')
    if toggle_start != -1 and toggle_end != -1:
        # 移除这个函数
        content = content[:toggle_start] + content[toggle_end:]

# 保存修改
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 最终修复完成！")
print("修复内容：")
print("1. 删除了错误的考核说明")
print("2. 在正确位置添加了考核说明")
print("3. 修复了不完整的按钮HTML")
print("4. 移除了不再需要的toggleAnswer函数")
print("5. 确保提交考核后显示所有参考答案")