#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动生成365天培训HTML文件（day016-day365）
根据培训大纲自动生成每个主题的完整HTML文件
"""

import os
import re
from pathlib import Path

# 培训大纲文件路径
OUTLINE_FILE = r"d:\365培训\365天培训大纲.md"
# 输出目录
OUTPUT_DIR = r"d:\365培训"

def read_outline():
    """读取培训大纲文件，提取day016-day365的主题"""
    with open(OUTLINE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式提取所有天数和主题
    # 格式：| 第X天 | 主题 |
    pattern = r'\|\s*第(\d+)天\s*\|\s*(.+?)\s*\|'
    matches = re.findall(pattern, content)
    
    # 转换为字典：{day_num: topic}
    outline = {}
    for day_num, topic in matches:
        day_num = int(day_num)
        topic = topic.strip()
        outline[day_num] = topic
    
    return outline

def generate_html_template(day_num, topic, prev_day=None, next_day=None):
    """生成单个HTML文件的模板内容"""
    
    # 确定模块名称
    if 1 <= day_num <= 90:
        module_name = "产品知识"
    elif 91 <= day_num <= 180:
        module_name = "销售技巧"
    elif 181 <= day_num <= 270:
        module_name = "验光与视力健康"
    else:
        module_name = "客户服务与沟通"
    
    # JavaScript代码块（单独字符串，避免与Python f-string冲突）
    js_code = """
        // 选择题判分函数
        function checkSingle(btn, correctAnswer) {
            const card = btn.closest('.question-card');
            const selected = card.querySelector('input[type="radio"]:checked');
            const feedback = card.querySelector('.feedback');
            
            if (!selected) {
                alert('请先选择一个答案！');
                return;
            }
            
            const isCorrect = selected.value === correctAnswer;
            feedback.style.display = 'block';
            feedback.className = 'feedback ' + (isCorrect ? 'correct' : 'wrong');
            feedback.innerHTML = isCorrect 
                ? '✅ 回答正确！' 
                : '❌ 回答错误。正确答案是 <strong>' + correctAnswer + '</strong>。';
            
            // 禁用所有选项
            card.querySelectorAll('input[type="radio"]').forEach(input => input.disabled = true);
            btn.disabled = true;
        }
        
        function checkMulti(btn, correctAnswers) {
            const card = btn.closest('.question-card');
            const checked = Array.from(card.querySelectorAll('input[type="checkbox"]:checked')).map(el => el.value);
            const feedback = card.querySelector('.feedback');
            
            if (checked.length === 0) {
                alert('请至少选择一个答案！');
                return;
            }
            
            const isCorrect = JSON.stringify(checked.sort()) === JSON.stringify(correctAnswers.sort());
            feedback.style.display = 'block';
            feedback.className = 'feedback ' + (isCorrect ? 'correct' : 'wrong');
            feedback.innerHTML = isCorrect 
                ? '✅ 回答正确！' 
                : '❌ 回答错误。正确答案是 <strong>' + correctAnswers.join(', ') + '</strong>。';
            
            // 禁用所有选项
            card.querySelectorAll('input[type="checkbox"]').forEach(input => input.disabled = true);
            btn.disabled = true;
        }
        
        // 问答题答案切换
        function toggleAnswer(btn) {
            const answerDiv = btn.nextElementSibling;
            if (answerDiv.style.display === 'none') {
                answerDiv.style.display = 'block';
                btn.textContent = '隐藏参考答案';
            } else {
                answerDiv.style.display = 'none';
                btn.textContent = '查看参考答案';
            }
        }
    """
    
    # 底部导航HTML
    prev_link = f'<a href="day{prev_day:03d}.html" class="nav-btn prev-btn">← 第{prev_day}天</a>' if prev_day else '<span class="nav-btn disabled">已是第一天</span>'
    next_link = f'<a href="day{next_day:03d}.html" class="nav-btn next-btn">第{next_day}天 →</a>' if next_day else '<span class="nav-btn disabled">已是最后一天</span>'
    
    # 生成HTML内容（使用format方法，避免f-string与JavaScript冲突）
    html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第{day_num}天 | {module_name}：{topic}</title>
    <link rel="stylesheet" href="training-styles.css">
</head>
<body>
    <div class="container">
        <!-- 顶部导航 -->
        <header class="page-header">
            <div class="header-left">
                <a href="index.html" class="back-link">← 返回目录</a>
                <span class="day-number">第{day_num}天</span>
            </div>
            <h1 class="page-title">{module_name}：{topic}</h1>
        </header>

        <!-- 学习内容区 -->
        <main class="learning-content">
            <div class="learning-card">
                <h2 class="card-title">📚 今日学习内容</h2>
                
                <div class="learning-section">
                    <h3>一、{topic} - 核心概念</h3>
                    <p>本节将详细介绍{topic}的基本概念、重要性和应用场景。</p>
                    <!-- 这里需要填充具体学习内容 -->
                    <p><em>注意：此内容为自动生成模板，需要根据实际主题填充详细学习内容。</em></p>
                </div>
                
                <div class="learning-section">
                    <h3>二、关键知识点</h3>
                    <p>以下是{topic}的关键知识点：</p>
                    <ul>
                        <li><strong>知识点1：</strong>待填充具体内容</li>
                        <li><strong>知识点2：</strong>待填充具体内容</li>
                        <li><strong>知识点3：</strong>待填充具体内容</li>
                    </ul>
                </div>
                
                <div class="learning-section">
                    <h3>三、实际应用</h3>
                    <p>{topic}在实际工作中的应用场景和案例分析。</p>
                    <!-- 这里需要填充实际应用内容 -->
                </div>
                
                <div class="learning-section summary-card">
                    <h3>📝 今日学习小结</h3>
                    <p>今天我们学习了{topic}的相关知识，重点掌握了：</p>
                    <ul>
                        <li>核心概念和理解</li>
                        <li>关键知识点和应用场景</li>
                        <li>实际工作中的操作方法</li>
                    </ul>
                    <p>请务必完成下方的练习题，巩固今天的学习成果。</p>
                </div>
            </div>
        </main>

        <!-- 练习题区 -->
        <section class="practice-section">
            <h2 class="section-title">✏️ 今日练习题</h2>
            
            <!-- 选择题 -->
            <div class="choice-questions">
                <h3 class="question-group-title">一、选择题（单选/多选）</h3>
                
                <div class="question-card" data-type="single" data-answer="A">
                    <p class="question-text">1. 关于{topic}，以下说法正确的是？（单选题）</p>
                    <div class="options">
                        <label class="option-item">
                            <input type="radio" name="q1" value="A">
                            <span class="option-text">选项A：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="radio" name="q1" value="B">
                            <span class="option-text">选项B：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="radio" name="q1" value="C">
                            <span class="option-text">选项C：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="radio" name="q1" value="D">
                            <span class="option-text">选项D：待填充</span>
                        </label>
                    </div>
                    <button class="submit-btn" onclick="checkSingle(this, 'A')">提交答案</button>
                    <div class="feedback" style="display:none;"></div>
                </div>
                
                <div class="question-card" data-type="multi" data-answer="AB">
                    <p class="question-text">2. 关于{topic}，以下哪些说法是正确的？（多选题）</p>
                    <div class="options">
                        <label class="option-item">
                            <input type="checkbox" name="q2" value="A">
                            <span class="option-text">选项A：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="checkbox" name="q2" value="B">
                            <span class="option-text">选项B：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="checkbox" name="q2" value="C">
                            <span class="option-text">选项C：待填充</span>
                        </label>
                        <label class="option-item">
                            <input type="checkbox" name="q2" value="D">
                            <span class="option-text">选项D：待填充</span>
                        </label>
                    </div>
                    <button class="submit-btn" onclick="checkMulti(this, ['A','B'])">提交答案</button>
                    <div class="feedback" style="display:none;"></div>
                </div>
            </div>
            
            <!-- 问答题 -->
            <div class="essay-questions">
                <h3 class="question-group-title">二、问答题</h3>
                
                <div class="question-card">
                    <p class="question-text">3. 请简述{topic}的主要应用场景和注意事项。</p>
                    <textarea class="essay-input" rows="4" placeholder="请在此输入您的答案..."></textarea>
                    <button class="show-answer-btn" onclick="toggleAnswer(this)">查看参考答案</button>
                    <div class="answer-reference" style="display:none;">
                        <strong>参考答案：</strong>
                        <p>待填充参考答案内容...</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 底部导航 -->
        <footer class="page-footer">
            <div class="footer-nav">
                {prev_link}
                <a href="index.html" class="nav-btn index-btn">返回目录</a>
                {next_link}
            </div>
            <div class="footer-info">
                <p>眼镜门店员工晋级培训系统 · 第{day_num}天</p>
            </div>
        </footer>
    </div>

    <script>
    {js_code}
    </script>
</body>
</html>""".format(
        day_num=day_num,
        module_name=module_name,
        topic=topic,
        prev_link=prev_link,
        next_link=next_link,
        js_code=js_code
    )
    
    return html_content

def generate_all_html_files(test_mode=True, test_start=16, test_end=20):
    """生成所有HTML文件（day016-day365）"""
    print("开始读取培训大纲...")
    outline = read_outline()
    
    print(f"培训大纲共包含 {len(outline)} 个主题")
    
    if test_mode:
        print(f"[测试模式] 仅生成 day{test_start:03d}-day{test_end:03d} 共 {test_end-test_start+1} 个文件")
        start_day = test_start
        end_day = test_end
    else:
        print(f"[正式模式] 生成 day016-day365 共 {365-15} 个文件")
        start_day = 16
        end_day = 365
    
    # 生成HTML文件
    generated_count = 0
    skipped_count = 0
    error_count = 0
    
    for day_num in range(start_day, end_day + 1):
        try:
            # 检查是否已存在该文件
            filename = f"day{day_num:03d}.html"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            if os.path.exists(filepath):
                print(f"跳过 {filename}（已存在）")
                skipped_count += 1
                continue
            
            # 获取主题
            topic = outline.get(day_num, f"主题待定（第{day_num}天）")
            
            # 确定前一天和后一天
            prev_day = day_num - 1 if day_num > 1 else None
            next_day = day_num + 1 if day_num < 365 else None
            
            # 生成HTML内容
            html_content = generate_html_template(day_num, topic, prev_day, next_day)
            
            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            generated_count += 1
            if generated_count % 10 == 0:
                print(f"已生成 {generated_count} 个文件...")
        
        except Exception as e:
            print(f"[错误] 生成 day{day_num:03d}.html 时出错：{str(e)}")
            error_count += 1
    
    print(f"\n[完成] 共生成 {generated_count} 个新文件，跳过 {skipped_count} 个已存在的文件，错误 {error_count} 个。")

if __name__ == "__main__":
    generate_all_html_files()
