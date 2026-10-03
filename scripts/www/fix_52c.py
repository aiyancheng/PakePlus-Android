import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第8周_结业冲刺与毕业考核\Day_52_学习内容.html"
with open(fp, encoding='utf-8') as f:
    c = f.read()

extra = """  <!-- 结尾鼓励语 -->
  <p style="text-align:center;color:#c0392b;font-weight:600;margin:16px 0">每一次高难度的挑战，都是你成为顶尖顾问的必经之路。</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:16px">— 第8周 Day 52 · 极端情境挑战 —</p>

"""

nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + c[nav_idx:]
with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_c)
print("Day_52:", new_c.count('\n')+1, "行")
