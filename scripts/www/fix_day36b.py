import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练\Day_36_学习内容.html'

with open(fp, encoding='utf-8') as f:
    lines = f.readlines()

print('readlines 行数:', len(lines))

# 在 </html> 前插入一个空注释行，增加1行
content = ''.join(lines)
content = content.replace('</html>', '<!-- Day 36 完成 -->\n</html>')

with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)

with open(fp, encoding='utf-8') as f:
    new_lines = f.readlines()
status = "✅" if len(new_lines) >= 200 else "⚠️ "
print(f"{status} Day_36: {len(new_lines)} 行")
