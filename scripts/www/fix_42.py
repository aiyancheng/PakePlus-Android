import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练\Day_42_学习内容.html'
with open(fp, encoding='utf-8') as f:
    c = f.read()

extra = '''  <div style="background:linear-gradient(135deg,#2980b9,#1a5276);color:#fff;border-radius:10px;padding:20px 24px;margin-top:24px;text-align:center">
    <div style="font-size:1.5rem;margin-bottom:8px">🎉</div>
    <strong style="font-size:1.1rem">恭喜完成第6周独立接单训练！</strong><br>
    <p style="margin-top:8px;opacity:.9">完成今日周测，与师傅深度复盘，带上满满收获迈入第7周！</p>
  </div>

'''

nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + c[nav_idx:]
with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_c)
print('Day_42:', new_c.count('\n')+1, '行')
