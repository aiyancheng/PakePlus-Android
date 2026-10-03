import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE1 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第1周_文化与制度启蒙"
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

GREEN_TIP = """  <div class="tip-box">
    <div class="label">💡 每日行动建议</div>
    <p>学习不仅仅是看内容。今天的任务：把今天学到的一个知识点，用自己的话解释给师傅或同事听。能说出来才是真的学会了。</p>
  </div>"""

BLUE_TIP = """  <div class="tip-box" style="background:#e3f2fd;border-left:4px solid #2196F3;">
    <div class="label" style="color:#1565c0;">💡 学以致用</div>
    <p>看完今天的内容后，找机会观察师傅接待一位客户，注意他/她是如何运用今天学到的知识点的。然后问师傅：这次接待中，最关键的判断点是什么？</p>
  </div>"""

# 针对每个文件的补充内容
EXTRA2 = {}

# Day_04: 行为规范与职场礼仪 (199行，差1行)
EXTRA2[(BASE1, "Day_04_学习内容.html")] = """  <!-- 补充结尾 -->
  <div class="summary-box" style="margin-top:24px">
    <h3>✅ 本日行动确认</h3>
    <ul>
      <li>□ 今日接待客户时，主动使用了至少2个礼仪规范</li>
      <li>□ 工作期间未使用手机处理私事</li>
      <li>□ 与同事保持了专业、友好的沟通态度</li>
    </ul>
  </div>

"""

# Day_05: 奖惩制度与安全规定 (187行，差13行)
EXTRA2[(BASE1, "Day_05_学习内容.html")] = """  <div class="section">
    <h2>💼 实际操作：安全风险自查清单</h2>
    <p>每日开店前，进行以下安全自查：</p>
    <table class="rule-table">
      <thead><tr><th>检查项目</th><th>正常状态</th><th>发现问题时</th></tr></thead>
      <tbody>
        <tr><td>展示柜锁闭状态</td><td>全部上锁，无异常</td><td>立即告知店长，不私自处理</td></tr>
        <tr><td>收银机备用金</td><td>与前日记录一致</td><td>立即上报，等待核查</td></tr>
        <tr><td>消防通道</td><td>无遮挡，通畅</td><td>清理遮挡物，告知店长</td></tr>
        <tr><td>设备运行状态</td><td>验光仪器正常开机</td><td>联系技术维修，勿自行拆装</td></tr>
      </tbody>
    </table>
  </div>

"""

# Day_08: 眼睛结构与视觉原理 (182行，差18行)
EXTRA2[(BASE2, "Day_08_学习内容.html")] = """  <div class="section">
    <h2>🎯 本日实践任务</h2>
    <p>今天，请做以下两件事来巩固所学：</p>
    <ol style="padding-left:20px;margin-bottom:14px;">
      <li style="margin-bottom:8px;">找一面镜子，闭上一只眼看不同距离的物体（先看近处，再看远处），感受眼睛调节时的细微变化——这就是晶状体在工作</li>
      <li style="margin-bottom:8px;">用自己的话，向一位家人或朋友解释"近视是怎么形成的"，看对方能否听懂。如果对方有疑问，思考如何优化你的解释方式</li>
    </ol>
    <div class="analogy-box"><div class="title">🎯 记忆口诀</div>
    <p>近视眼轴长，光聚网膜前，凹镜来矫正；<br>
远视眼轴短，光聚网膜后，凸镜来矫正；<br>
散光曲率差，光无法聚点，柱镜来矫正；<br>
老花弹力减，近处看不清，正镜来补偿。</p></div>
  </div>

"""

# Day_10: 镜框知识 (180行，差20行)
EXTRA2[(BASE2, "Day_10_学习内容.html")] = """  <div class="section">
    <h2>🛍️ 镜框展示陈列技巧</h2>
    <p>好的陈列能让客户更容易找到中意的款式，提升成单率：</p>
    <ul>
      <li>按照颜色或材质分区陈列，视觉更整洁</li>
      <li>主推款放在视线高度（通常1.2-1.6米区间）</li>
      <li>高价款与低价款错开陈列，形成价格锚定</li>
      <li>定期更新陈列顺序，避免客户"看腻了"</li>
    </ul>
    <h3>📌 试戴礼仪</h3>
    <ul>
      <li>递给客户前先用布擦拭镜架</li>
      <li>请客户坐下后帮助佩戴，而非直接递给对方</li>
      <li>附近准备镜子，方便客户自行观察效果</li>
      <li>试戴完毕的镜架及时收回清洁，放回原位</li>
    </ul>
  </div>

"""

# Day_11: 验配流程 (179行，差21行)
EXTRA2[(BASE2, "Day_11_学习内容.html")] = """  <div class="section">
    <h2>🔧 仪器设备日常维护</h2>
    <p>验光仪器是门店的核心资产，正确维护能延长使用寿命并保证测量精度：</p>
    <table class="rule-table">
      <thead><tr><th>设备</th><th>日常维护要点</th><th>注意事项</th></tr></thead>
      <tbody>
        <tr><td>电脑验光仪</td><td>每日开机校准，镜头用专用棉签清洁</td><td>不可用手触摸镜头</td></tr>
        <tr><td>综合验光仪</td><td>使用后将度数归零，镜片清洁保护</td><td>移动时小心轻放</td></tr>
        <tr><td>裂隙灯</td><td>灯泡定期更换，镜头防尘</td><td>不可直视光源</td></tr>
        <tr><td>视力表</td><td>灯管定期更换，亮度均匀</td><td>检查视力表距离是否准确（5米）</td></tr>
      </tbody>
    </table>
    <p>发现仪器异常，立即报告，不自行拆卸修理。</p>
  </div>

"""

# Day_12: 镜片知识深化 (165行，差35行)
EXTRA2[(BASE2, "Day_12_学习内容.html")] = """  <div class="section">
    <h2>📊 镜片推荐决策树</h2>
    <p>面对客户时，用以下逻辑快速确定推荐方向：</p>
    <table class="rule-table">
      <thead><tr><th>客户情况</th><th>关键问题</th><th>推荐方向</th></tr></thead>
      <tbody>
        <tr><td>普通近视（-6以内）</td><td>预算+用眼场景</td><td>根据度数选折射率，按需加防蓝光/防污</td></tr>
        <tr><td>高度近视（-6以上）</td><td>厚度要求</td><td>1.74超薄镜片，非球面设计</td></tr>
        <tr><td>40岁以上+看近困难</td><td>是否同时需要看远？</td><td>单光老花镜或渐进多焦点镜片</td></tr>
        <tr><td>儿童配镜</td><td>是否已散瞳验光？度数稳定吗？</td><td>建议防控镜片，不建议超高折射率（影响通透性）</td></tr>
        <tr><td>驾驶员</td><td>开车频率如何？</td><td>偏光太阳镜或变色近视镜</td></tr>
      </tbody>
    </table>
    <div class="tip-box"><div class="label">💡 不确定时怎么办</div><p>遇到复杂情况（高度散光、特殊处方、眼病史），不要贸然推荐，诚实说"我帮您请验光师看一下"，再由专业人员判断。谦虚求助远好于专业错误。</p></div>
  </div>

"""

# Day_13: 处方解读 (172行，差28行)
EXTRA2[(BASE2, "Day_13_学习内容.html")] = """  <div class="section">
    <h2>📐 瞳距测量方法</h2>
    <p>瞳距（PD）是配镜精度的关键参数，测量误差会导致戴镜不适：</p>
    <h3>📌 瞳距尺测量步骤</h3>
    <ol style="padding-left:20px;margin-bottom:14px;">
      <li style="margin-bottom:6px;">嘱咐客户平视前方，注视5米外的视标</li>
      <li style="margin-bottom:6px;">将瞳距尺紧贴眉弓，右端"0"刻度对准右眼瞳孔中心</li>
      <li style="margin-bottom:6px;">读取左眼瞳孔中心对应的刻度，即为双眼瞳距</li>
      <li style="margin-bottom:6px;">重复测量3次，取平均值</li>
      <li style="margin-bottom:6px;">单眼瞳距：分别测量左右眼瞳孔到鼻梁中线的距离</li>
    </ol>
    <div class="refraction-box" style="background:#e3f2fd;border-color:#bbdefb;">
      <div class="label" style="color:#1565c0;">📏 正常参考值</div>
      <p>成人平均瞳距：男性约64mm，女性约62mm<br>单眼瞳距通常左右各约31-32mm，但不一定完全对称</p>
    </div>
    <div class="tip-box"><div class="label">⚠️ 注意</div><p>渐进镜和高度数镜片对瞳距要求更严格，误差不超过±1mm。儿童测量时需特别注意，因为他们不容易长时间保持注视。</p></div>
  </div>

"""

# Day_14: 第2周总结 (197行，差3行)
EXTRA2[(BASE2, "Day_14_学习内容.html")] = """  <!-- 第2周完成标记 -->
  <p style="text-align:center;color:#2196F3;font-weight:600;margin:16px 0">恭喜完成第2周学习！下周将进入实操技能训练阶段。</p>
  <p style="text-align:center;color:#aaa;font-size:.85rem;margin-bottom:16px">— 第2周 · 光学与产品知识 · 全部完成 —</p>

"""

print("补充第1周不足文件...")
for fn in ["Day_04_学习内容.html", "Day_05_学习内容.html"]:
    key = (BASE1, fn)
    if key not in EXTRA2:
        continue
    fp = os.path.join(BASE1, fn)
    lines = insert_before_nav(fp, EXTRA2[key])
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")

print("\n补充第2周不足文件...")
for fn in ["Day_08_学习内容.html", "Day_10_学习内容.html", "Day_11_学习内容.html",
           "Day_12_学习内容.html", "Day_13_学习内容.html", "Day_14_学习内容.html"]:
    key = (BASE2, fn)
    if key not in EXTRA2:
        continue
    fp = os.path.join(BASE2, fn)
    lines = insert_before_nav(fp, EXTRA2[key])
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
