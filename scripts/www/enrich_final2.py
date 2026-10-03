import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE2 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第2周_光学与产品知识"

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
    "Day_08_学习内容.html": """  <div class="summary-box">
    <h3>📝 今日要点回顾（完整版）</h3>
    <ul>
      <li>✅ 眼睛=精密相机：角膜+晶状体是镜头，视网膜是感光片</li>
      <li>✅ 近视：眼轴长，光聚前，凹镜矫正；远视：眼轴短，光聚后，凸镜矫正</li>
      <li>✅ 散光：角膜曲率不均，用柱镜矫正；老花：晶状体弹性减退，用正镜补偿</li>
      <li>✅ 能用通俗语言向客户解释视力问题，是专业服务的关键能力</li>
    </ul>
    <p style="margin-top:14px;color:#1565c0;font-weight:600">
      今日任务：用自己的话向师傅讲述一遍"近视是如何形成的"，听取反馈。
    </p>
  </div>

""",
    "Day_11_学习内容.html": """  <div class="summary-box" style="background:linear-gradient(135deg,#e3f2fd,#e8f5ff)">
    <h3 style="color:#1565c0">📝 今日要点总结</h3>
    <ul>
      <li>✅ 验配流程9步骤要熟悉，每步都有其关键意义</li>
      <li>✅ 仪器维护是日常工作的一部分，不可忽视</li>
      <li>✅ 遇到复杂案例及时请教，不轻易自行判断</li>
      <li>✅ 记录规范是保障服务质量和处理纠纷的基础</li>
    </ul>
    <p style="margin-top:14px;color:#1565c0;font-weight:600">
      今日任务：跟随师傅完整观察一次验配流程，记录你注意到的细节。
    </p>
  </div>

""",
    "Day_12_学习内容.html": """  <div class="summary-box" style="background:linear-gradient(135deg,#e3f2fd,#e8f5ff)">
    <h3 style="color:#1565c0">📝 今日要点总结</h3>
    <ul>
      <li>✅ 镜片推荐的核心：了解客户需求+度数，给出针对性方案</li>
      <li>✅ 渐进镜适合老视，重点是测量瞳高和适应期指导</li>
      <li>✅ 防蓝光针对特定人群，用数据说话更有说服力</li>
      <li>✅ 不确定时求助专业人员，而不是猜测</li>
    </ul>
    <p style="margin-top:14px;color:#1565c0;font-weight:600">
      今日任务：找出门店内销量最好的3款镜片，记录它们各自的核心卖点。
    </p>
  </div>

""",
    "Day_13_学习内容.html": """  <div class="summary-box" style="background:linear-gradient(135deg,#e3f2fd,#e8f5ff)">
    <h3 style="color:#1565c0">📝 今日要点总结</h3>
    <ul>
      <li>✅ 能快速正确解读处方中S/C/A/ADD/PD各参数含义</li>
      <li>✅ 瞳距测量：平视注视，测量3次取均值，误差小于±1mm</li>
      <li>✅ 处方解读是配镜质量控制的第一关，不能出错</li>
      <li>✅ 特殊处方（高度数、高散光）需要验光师参与确认</li>
    </ul>
    <p style="margin-top:14px;color:#1565c0;font-weight:600">
      今日任务：找5张不同类型的处方单（旧档案或师傅提供），逐一解读所有参数，师傅核对。
    </p>
  </div>

""",
}

for fn, extra in FINALS.items():
    fp = os.path.join(BASE2, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
