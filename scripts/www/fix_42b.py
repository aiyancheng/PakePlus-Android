import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练\Day_42_学习内容.html'
with open(fp, encoding='utf-8') as f:
    c = f.read()

# 在最后的 </div>\n</body> 前插入空行占位内容
extra = '''  <!-- 第6周训练完成标记 -->
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-top:8px">— 第6周 · 独立接单训练 · 全部完成 —</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:8px">下周目标：成为客户主动信任的专业顾问 💪</p>

'''

nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + c[nav_idx:]
with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_c)
print('Day_42:', new_c.count('\n')+1, '行')
