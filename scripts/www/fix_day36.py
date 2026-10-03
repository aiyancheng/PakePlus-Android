import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练\Day_36_学习内容.html'

with open(fp, encoding='utf-8') as f:
    c = f.read()

extra = (
    '  <p style="text-align:center;color:#2980b9;font-weight:600;margin:12px 0">'
    '独立接单，是从学徒走向专业人的关键一步。勇敢迈出，每天进步一点点。</p>\n'
    '  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:4px">'
    '— Day 36 · 独立接单第一天 · 完成 —</p>\n'
    '  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:16px">'
    '积累每一次接单经验，成为值得客户信赖的眼镜顾问。</p>\n'
    '\n'
)

nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + '  ' + c[nav_idx:]

with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_c)

lines = new_c.count('\n') + 1
status = "✅" if lines >= 200 else "⚠️ "
print(f"{status} Day_36: {lines} 行")
