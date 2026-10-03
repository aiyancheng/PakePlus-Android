import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE4 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第4周_销售话术与中期考核"
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

FINALS = {
    (BASE4, "Day_26_学习内容.html"): """  <!-- 补充 -->
  <div class="section">
    <h2>📝 今日要点总结</h2>
    <ul>
      <li>✅ 连带销售的时机：客户成单后、客户提到其他用途时</li>
      <li>✅ 会员建档是积累复购资源的核心手段，每单必须引导开通</li>
      <li>✅ 连带不是强买强卖，而是发现客户未被满足的需求</li>
    </ul>
  </div>

""",
    (BASE4, "Day_27_学习内容.html"): """  <div class="section">
    <h2>📝 今日总结</h2>
    <ul>
      <li>✅ 投诉是礼物——能收到投诉，说明客户还愿意与你沟通</li>
      <li>✅ 处理投诉的第一步：控制情绪，不要让自己也变得激动</li>
      <li>✅ 解决方案要具体、可执行，不能含糊承诺</li>
      <li>✅ 投诉处理好后，主动跟进客户，确认满意度</li>
    </ul>
    <p style="margin-top:12px;color:#4CAF50;font-weight:600">今日任务：与师傅模拟一次投诉场景，练习完整的处理流程。</p>
  </div>

""",
    (BASE5, "Day_31_学习内容.html"): """  <!-- 补充 -->
  <div class="card" style="background:white;border-radius:12px;padding:24px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:18px;color:#333;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #11998e">📝 今日总结</h2>
    <ul style="padding-left:20px;line-height:1.8">
      <li>FAB法则是产品介绍的骨架，情感化表达是灵魂</li>
      <li>每个产品推介前，先想：客户最在乎什么？</li>
      <li>练习是关键，今天就找机会向一位客户完整演练一遍</li>
    </ul>
  </div>

""",
    (BASE5, "Day_32_学习内容.html"): """  <div class="card" style="background:white;border-radius:12px;padding:24px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:18px;color:#333;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #11998e">📝 今日总结</h2>
    <ul style="padding-left:20px;line-height:1.8">
      <li>协助验光不只是打下手，更是学习专业技能的宝贵机会</li>
      <li>主觉验光的7个步骤，跟岗中仔细观察每一步的目的</li>
      <li>记录每次跟岗的观察，积累属于自己的学习笔记</li>
      <li>结束后主动向验光师请教：今天这个案例有什么特殊之处？</li>
    </ul>
  </div>

""",
    (BASE5, "Day_34_学习内容.html"): """  <div class="card" style="background:white;border-radius:12px;padding:24px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:18px;color:#333;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #11998e">📝 今日总结</h2>
    <ul style="padding-left:20px;line-height:1.8">
      <li>HEART原则：倾听→同理→致歉→解决→感谢，五步处理所有投诉</li>
      <li>情绪管理是投诉处理的第一关，你的冷静是化解冲突的关键</li>
      <li>记录每次投诉案例，分析原因，防止同类问题再次发生</li>
      <li>超预期解决投诉，是将投诉客户转化为忠实客户的最佳时机</li>
    </ul>
  </div>

""",
    (BASE5, "Day_35_学习内容.html"): """  <!-- 额外补充 -->
  <div style="background:linear-gradient(135deg,#2980b9,#1a5276);color:#fff;border-radius:10px;padding:20px 24px;margin-top:16px;text-align:center">
    <p style="font-size:1.1rem;font-weight:600;margin-bottom:8px">🌟 第5周跟岗训练圆满完成！</p>
    <p style="opacity:.9">你已经完成了从观察到参与的第一步。下周，独立面对每一位客户，展现你的成长！</p>
  </div>

""",
}

for (base, fn), extra in FINALS.items():
    fp = os.path.join(base, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
