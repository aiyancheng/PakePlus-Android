import sys
sys.stdout.reconfigure(encoding='utf-8')

fp = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第8周_结业冲刺与毕业考核\Day_52_学习内容.html"
with open(fp, encoding='utf-8') as f:
    c = f.read()

extra = """  <h2 style="color:#c0392b;margin-top:32px">🛡️ 高难度场景中的自我保护</h2>
  <div style="background:#fef0ef;border-radius:10px;padding:18px 22px;margin:16px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">当场景升级到难以独自处理时，需要懂得自我保护和团队协作：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px"><strong>语言记录</strong>：重要对话请求客户确认，关键承诺形成书面记录</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px"><strong>及时汇报</strong>：遇到投诉第一时间报告店长，不要私自解决</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px"><strong>证据保全</strong>：保留验光记录、工单、沟通记录</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px"><strong>情绪隔离</strong>：下班后学会把工作中的负面情绪放下，保持身心健康</li>
    </ul>
    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 记住：每一次成功处理高难度场景，都是你职业能力的一次升华。不回避困难，才能真正成长。
    </div>
  </div>

"""

nav_idx = c.rfind('<div class="nav-footer"')
new_c = c[:nav_idx] + extra + c[nav_idx:]
with open(fp, 'w', encoding='utf-8') as f:
    f.write(new_c)
print("Day_52:", new_c.count('\n')+1, "行")
