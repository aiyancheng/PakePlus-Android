import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE5 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第5周_实战跟岗训练"

def insert_before_nav(filepath, extra_html):
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    nav_idx = c.rfind('<div class="nav-footer"')
    if nav_idx == -1:
        nav_idx = c.rfind('</div>\n</body>')
    if nav_idx == -1:
        nav_idx = c.rfind('</body>')
    new_c = c[:nav_idx] + extra_html + '\n\n  ' + c[nav_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    return new_c.count('\n') + 1

END34 = """  <p style="text-align:center;color:#2980b9;font-weight:600;margin:12px 0">每一次成功处理投诉，都是你赢得终身客户的机会。</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:12px">— Day 34 · 客诉处理实战 · 完成 —</p>

"""

END35 = """  <p style="text-align:center;color:#2980b9;font-weight:600;margin:12px 0">五周积累，是独立接单的底气。带上自信，迎接第6周！</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:12px">— Day 35 · 第5周总结 · 完成 —</p>

"""

for fn, extra in [("Day_34_学习内容.html", END34), ("Day_35_学习内容.html", END35)]:
    fp = os.path.join(BASE5, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
