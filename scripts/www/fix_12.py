import sys; sys.stdout.reconfigure(encoding='utf-8')
fp = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第2周_光学与产品知识\Day_12_学习内容.html"
with open(fp, encoding='utf-8') as f: c = f.read()
extra = """  <p style="text-align:center;color:#2196F3;font-weight:600;margin:12px 0">第2周知识积累：镜片是帮助客户看清世界的工具，选对镜片就是给客户最大的服务。</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:12px">— Day 12 · 镜片知识深化 · 完成 —</p>

"""
nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + c[nav_idx:]
with open(fp, 'w', encoding='utf-8') as f: f.write(new_c)
print("Day_12:", new_c.count('\n')+1, "行")
