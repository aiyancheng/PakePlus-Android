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

def g_section(title, content):
    """绿色主题section"""
    return f"""  <div class="section">
    <h2>{title}</h2>
    {content}
  </div>
"""

def b_section(title, content):
    """蓝色主题section"""
    return f"""  <div class="section">
    <h2>{title}</h2>
    {content}
  </div>
"""

# ============ 第1周文件扩充内容 ============

EXTRA = {}

# ---- Day_03: 考勤制度与薪酬福利 (176行) ----
EXTRA[(BASE1, "Day_03_学习内容.html")] = g_section(
    "💡 第四部分：新员工常见疑问解答",
    """    <h3>📌 Q1：试用期有多长，转正需要满足什么条件？</h3>
    <p>试用期通常为1-3个月（视岗位而定），转正需满足：</p>
    <ul>
      <li>通过门店规定的培训考核（笔试+实操）</li>
      <li>出勤无重大违规记录</li>
      <li>由带教师傅/店长综合评估服务表现</li>
      <li>客户投诉记录清零或在可接受范围内</li>
    </ul>
    <div class="tip-box"><div class="label">💡 小贴士</div><p>转正面谈前，主动整理试用期的工作亮点和学习收获，展示你的成长，会给店长留下好印象。</p></div>

    <h3>📌 Q2：提成怎么算，公平吗？</h3>
    <p>提成通常基于个人确认的销售单据，系统记录清晰。有疑问时：</p>
    <ul>
      <li>每月发薪前可查看自己的销售记录</li>
      <li>发现差异及时与店长/HR核对，当月内解决</li>
      <li>新员工前期提成可能较低，随熟练度和客单价提升会明显增长</li>
    </ul>

    <h3>📌 Q3：节假日要上班吗？</h3>
    <p>眼镜门店属于零售行业，节假日通常是客流高峰，需要正常营业。相应的：</p>
    <ul>
      <li>法定节假日上班享有调休或加班补贴</li>
      <li>排班由店长统筹，尽量照顾员工需求</li>
      <li>春节等重要节假日，提前与店长沟通假期安排</li>
    </ul>
"""
) + """  <div class="summary-box" style="margin-top:24px">
    <h3>🔑 今日行动清单</h3>
    <ul>
      <li>□ 确认本门店的打卡方式（APP/指纹/刷卡）</li>
      <li>□ 记下店长的联系方式，了解紧急联系流程</li>
      <li>□ 询问师傅：本店目前的销售提成计算方式</li>
      <li>□ 了解试用期转正的具体考核内容</li>
    </ul>
  </div>

"""

# ---- Day_04: 行为规范与职场礼仪 (162行) ----
EXTRA[(BASE1, "Day_04_学习内容.html")] = g_section(
    "🌟 第三部分：主动服务意识培养",
    """    <p>礼仪规范是外在的"形"，主动服务意识是内在的"神"。真正优秀的门店员工不只是遵守规定，而是发自内心地想帮助客户。</p>
    
    <h3>📌 主动服务的具体表现</h3>
    <table class="rule-table">
      <thead><tr><th>场景</th><th>被动服务（仅做基本的）</th><th>主动服务（超出预期的）</th></tr></thead>
      <tbody>
        <tr><td>客户进门</td><td>站在原位问好</td><td>主动上前迎接，引导落座</td></tr>
        <tr><td>等待取镜</td><td>告知时间后让其等待</td><td>提供饮用水，介绍等待区</td></tr>
        <tr><td>客户询问</td><td>回答问题</td><td>回答问题后主动追问需求</td></tr>
        <tr><td>客户离开</td><td>道别</td><td>送至门口，提醒保养事宜</td></tr>
      </tbody>
    </table>

    <h3>📌 服务心态：把客户当家人</h3>
    <p>想象你正在为自己的父母或朋友配眼镜，你会怎么做？这种心态转变，是提升服务质量的最简单方法。</p>
    <div class="tip-box"><div class="label">💡 实践建议</div><p>每天接待第一位客户前，默默告诉自己："我今天要帮这位客户找到最适合他的解决方案。"这个小小的心理暗示，能显著改变你的服务态度。</p></div>
"""
) + g_section(
    "📋 第四部分：常见职场礼仪误区",
    """    <table class="rule-table">
      <thead><tr><th>误区</th><th>正确做法</th></tr></thead>
      <tbody>
        <tr><td>认为礼貌就是说"您好""谢谢"</td><td>礼貌是尊重的行动，不只是口头语</td></tr>
        <tr><td>只对消费多的客户热情</td><td>对每位进门的客户一视同仁</td></tr>
        <tr><td>私下议论同事或客户</td><td>保守职业机密，不在工作场所八卦</td></tr>
        <tr><td>工作时间刷手机</td><td>手机调静音，紧急事务在休息时间处理</td></tr>
        <tr><td>当着客户面与同事争论</td><td>意见分歧下班后私下沟通</td></tr>
      </tbody>
    </table>
"""
)

# ---- Day_05: 奖惩制度与安全规定 (141行) ----
EXTRA[(BASE1, "Day_05_学习内容.html")] = g_section(
    "🔒 第三部分：门店安全管理",
    """    <h3>📌 财务安全</h3>
    <ul>
      <li>收款后立即进行POS机确认，不接受私下转账（除非门店有明文规定）</li>
      <li>发现收银差额，及时上报，不自行处理</li>
      <li>每日收款登记，与系统记录核对</li>
      <li>不得将顾客资料（手机号、购买记录）用于私人用途</li>
    </ul>

    <h3>📌 商品安全</h3>
    <table class="rule-table">
      <thead><tr><th>场景</th><th>安全要求</th></tr></thead>
      <tbody>
        <tr><td>高价值陈列品</td><td>试戴时全程陪同，不离视线</td></tr>
        <tr><td>库存领取</td><td>按需领取，做好出库记录</td></tr>
        <tr><td>配镜工单</td><td>核对无误再制作，避免废镜纠纷</td></tr>
        <tr><td>成品镜存储</td><td>分类摆放，配件齐全，避免混淆</td></tr>
      </tbody>
    </table>

    <h3>📌 消防与应急</h3>
    <ul>
      <li>了解门店消防设备位置（灭火器、应急出口）</li>
      <li>熟悉紧急疏散路线，不堵塞通道</li>
      <li>遇到可疑人员或紧急状况，立即报告店长</li>
    </ul>
"""
) + g_section(
    "🏆 第四部分：奖励制度的积极运用",
    """    <p>了解奖励制度的目的，不只是为了"拿奖金"，而是用它指导自己每天的工作重点：</p>
    <div class="tip-box"><div class="label">💡 利用制度提升自我</div>
    <ul style="margin-top:8px;">
      <li>每月初查看门店本月的重点KPI（销售额目标、服务评分等）</li>
      <li>把KPI分解到每天：每天至少完成多少才能达到月目标？</li>
      <li>找到与自己差距最大的指标，重点改进</li>
      <li>主动向优秀同事请教，而不是等待培训</li>
    </ul>
    </div>
    <p style="margin-top:14px;">优秀员工和普通员工的差距，往往不在于能力，而在于是否<strong>主动把握每一次成长机会</strong>。</p>
"""
)

# ---- Day_06: 第1周 (180行) ----
EXTRA[(BASE1, "Day_06_学习内容.html")] = g_section(
    "🚀 第四部分：第2周学习预览与准备",
    """    <p>第1周，你了解了门店文化、制度规范和职场礼仪——这是成为合格员工的"地基"。</p>
    <p>从第2周开始，你将进入眼镜行业的专业知识学习：</p>
    <table class="rule-table">
      <thead><tr><th>第2周学习重点</th><th>与日常工作的关联</th></tr></thead>
      <tbody>
        <tr><td>眼睛结构与屈光原理</td><td>帮助客户理解他们的视力问题</td></tr>
        <tr><td>近视/远视/散光</td><td>解释配镜处方，推荐合适镜片</td></tr>
        <tr><td>镜片材料与镀膜</td><td>为客户选择最合适的镜片产品</td></tr>
        <tr><td>镜框材质与选型</td><td>帮客户找到最适合脸型的镜框</td></tr>
        <tr><td>验配基础流程</td><td>接待客户时的专业流程</td></tr>
      </tbody>
    </table>
    <div class="tip-box"><div class="label">💡 预习建议</div>
    <p>在进入第2周之前，可以先观察门店里的展示品：镜片的薄厚差异是怎么产生的？不同材质的镜框手感如何？带着问题去观察，学习效果会加倍。</p>
    </div>
"""
)

# ============ 第2周文件扩充内容 ============

B_TIP = lambda label, content: f"""    <div class="tip-box"><div class="label">{label}</div><p>{content}</p></div>"""

# ---- Day_08: 眼睛结构与视觉原理 (162行) ----
EXTRA[(BASE2, "Day_08_学习内容.html")] = b_section(
    "🌟 第四部分：用简单语言向客户解释眼睛问题",
    """    <p>专业知识要能"翻译"成客户能听懂的话，才有价值。以下是几个常见问题的通俗解释模板：</p>
    
    <h3>近视解释模板</h3>
    <div class="analogy-box"><div class="title">👁️ 向客户说明</div>
    <p>"您的眼睛就像一台相机，近视是因为相机的'焦距'太长了，光线聚焦在感光片前面而不是上面，所以远处的东西看起来就模糊了。近视眼镜相当于给这台相机加了一块调整焦距的滤镜，把光线拉回到合适的位置。"</p></div>

    <h3>散光解释模板</h3>
    <div class="analogy-box"><div class="title">👁️ 向客户说明</div>
    <p>"散光是因为您眼睛角膜的弯曲度不均匀——就像一个鸡蛋的侧面，水平和垂直方向的弯曲程度不一样。光线进来后没法聚成一个点，所以看东西会有重影或模糊。散光镜片专门针对这个不均匀进行补偿。"</p></div>

    <h3>老花解释模板</h3>
    <div class="analogy-box"><div class="title">👁️ 向客户说明</div>
    <p>"老花不是近视，它是眼睛里的'调焦弹簧'（晶状体）随年龄变硬了，弹性不够，很难聚焦在近处。就像橡皮筋用久了会失去弹力。老花镜就是帮您的眼睛'借一份力'，补偿这个失去的弹力。"</p></div>
""" + B_TIP("💡 沟通秘诀", "解释时配合手势（如用两手比喻焦点的位置），效果会更好。不要直接背定义，要让客户真正理解。")
)

# ---- Day_09: 镜片材料 (186行) ----
EXTRA[(BASE2, "Day_09_学习内容.html")] = b_section(
    "🛒 第四部分：镜片选购实战指南",
    """    <h3>📌 根据度数推荐折射率</h3>
    <table class="rule-table">
      <thead><tr><th>度数范围</th><th>推荐折射率</th><th>理由</th></tr></thead>
      <tbody>
        <tr><td>-2.00以内</td><td>1.56~1.60</td><td>度数低，镜片不厚，性价比最高</td></tr>
        <tr><td>-2.00 ~ -4.00</td><td>1.60~1.67</td><td>平衡厚度和价格的最佳区间</td></tr>
        <tr><td>-4.00 ~ -6.00</td><td>1.67~1.71</td><td>防止镜片过厚影响美观</td></tr>
        <tr><td>-6.00以上</td><td>1.71~1.74</td><td>高度近视必须用超高折射率，否则镜片很厚</td></tr>
      </tbody>
    </table>
    
    <h3>📌 镀膜选择建议</h3>
    <ul>
      <li><strong>防反射膜</strong>：所有人都建议加，减少视觉疲劳</li>
      <li><strong>防蓝光</strong>：长时间用电脑/手机的人强烈推荐</li>
      <li><strong>防污膜</strong>：孩子或容易沾指纹的人推荐</li>
      <li><strong>高硬度膜</strong>：树脂镜片必备，防划伤</li>
    </ul>
""" + B_TIP("💡 销售关键", "推荐镜片时，先问客户日常用眼场景（主要是看远/看近？用电脑多？开车多？），再针对性推荐，避免'一刀切'。")
)

# ---- Day_10: 镜框知识 (143行) ----
EXTRA[(BASE2, "Day_10_学习内容.html")] = b_section(
    "👓 第三部分：镜框选购导购实战",
    """    <h3>📌 脸型与镜框的匹配建议</h3>
    <table class="rule-table">
      <thead><tr><th>脸型</th><th>特征</th><th>推荐镜框形状</th><th>避免</th></tr></thead>
      <tbody>
        <tr><td>圆脸</td><td>脸部轮廓圆润</td><td>方形/矩形框，增加立体感</td><td>圆形框，会显脸更圆</td></tr>
        <tr><td>方脸</td><td>棱角分明，额头和颌骨宽</td><td>圆形/椭圆框，柔化线条</td><td>方形框，会强调棱角</td></tr>
        <tr><td>长脸</td><td>脸型较长，较窄</td><td>粗框/深色框，横向感强的</td><td>细框/窄框，会显脸更长</td></tr>
        <tr><td>心形脸</td><td>额宽颌窄</td><td>下半部分较宽的框型</td><td>额宽镜框，会夸大额头</td></tr>
        <tr><td>椭圆脸</td><td>标准比例</td><td>几乎所有款式都适合</td><td>几乎无禁忌</td></tr>
      </tbody>
    </table>

    <h3>📌 镜框尺寸说明</h3>
    <p>镜框上通常标注三个数字，如"52-18-140"，分别代表：</p>
    <ul>
      <li><strong>52</strong>：镜片宽度（mm），与瞳距相关</li>
      <li><strong>18</strong>：鼻梁宽度（mm），影响佩戴舒适度</li>
      <li><strong>140</strong>：镜腿长度（mm），适合不同头部大小</li>
    </ul>
""" + B_TIP("💡 导购小技巧", "让客户先描述自己的用途和风格偏好（商务/休闲/运动/时尚），再推荐3-5款而不是一下子展示全部，避免选择困难症。")
) + b_section(
    "🔧 第四部分：镜框调整基础",
    """    <p>新员工初期需要学会基础的镜框调整技巧，帮助客户获得最舒适的佩戴体验：</p>
    <ul>
      <li><strong>鼻托调整</strong>：两侧鼻托松紧一致，镜框水平，不压迫鼻梁</li>
      <li><strong>镜腿调整</strong>：镜腿弯曲角度要自然，不夹头，不松脱</li>
      <li><strong>整体水平</strong>：戴上后观察两侧是否对称，不歪斜</li>
    </ul>
    <div class="tip-box"><div class="label">⚠️ 注意</div><p>高温处理镜框前需确认材质，板材框可加热软化调整，金属框直接弯折；调整前先询问师傅，避免损坏镜框造成损失。</p></div>
"""
)

# ---- Day_11: 第2周知识 (157行) ----
EXTRA[(BASE2, "Day_11_学习内容.html")] = b_section(
    "🔬 补充内容：验配流程全貌预览",
    """    <p>在学习具体的技术细节之前，先了解完整的验配流程，有助于建立全局观：</p>
    <table class="rule-table">
      <thead><tr><th>步骤</th><th>内容</th><th>负责人</th></tr></thead>
      <tbody>
        <tr><td>① 接待问诊</td><td>了解客户需求、旧镜情况、用眼习惯</td><td>销售员工</td></tr>
        <tr><td>② 视力检查</td><td>裸眼视力+旧镜矫正视力</td><td>验光员</td></tr>
        <tr><td>③ 电脑验光</td><td>仪器初步测量屈光度</td><td>验光员</td></tr>
        <tr><td>④ 主觉验光</td><td>综合验光仪精确确认处方</td><td>验光员</td></tr>
        <tr><td>⑤ 镜片推荐</td><td>根据处方和需求推荐镜片类型</td><td>销售员工</td></tr>
        <tr><td>⑥ 镜框选型</td><td>帮助客户选择合适镜框</td><td>销售员工</td></tr>
        <tr><td>⑦ 开单制镜</td><td>确认参数，填写工单，送加工</td><td>验光员/员工</td></tr>
        <tr><td>⑧ 取镜验收</td><td>核对度数、瞳距，试戴确认</td><td>验光员/员工</td></tr>
        <tr><td>⑨ 售后跟进</td><td>适应期回访，保养服务</td><td>销售员工</td></tr>
      </tbody>
    </table>
""" + B_TIP("💡 全流程意识", "了解整个流程，你才能在接待时知道下一步是什么，而不是每次都要问同事，让客户感到专业。")
)

# ---- Day_12: 镜片知识深化 (138行) ----
EXTRA[(BASE2, "Day_12_学习内容.html")] = b_section(
    "🔬 补充：渐进镜与功能镜详解",
    """    <h3>渐进多焦点镜片</h3>
    <p>渐进镜是目前最先进的老视解决方案，镜片从上到下：</p>
    <ul>
      <li>上方区域：用于看远（开车、行走）</li>
      <li>中间区域：用于看中距离（电脑屏幕）</li>
      <li>下方区域：用于看近（阅读、手机）</li>
    </ul>
    <p>外观与普通眼镜相同，无明显分界线，兼顾美观和实用。</p>
    <div class="tip-box"><div class="label">⚠️ 适应期说明</div><p>渐进镜初次佩戴通常需要1-2周适应期，下楼梯时需低头习惯，转头而非转眼看侧方。告知客户坚持佩戴，一般1-2周后即可自然使用。</p></div>
    
    <h3>防蓝光镜片销售技巧</h3>
    <p>根据客户职业和用眼场景精准推荐：</p>
    <table class="rule-table">
      <thead><tr><th>客户类型</th><th>推荐理由</th><th>话术关键词</th></tr></thead>
      <tbody>
        <tr><td>上班族</td><td>8小时电脑工作</td><td>"保护眼睛，减少视疲劳"</td></tr>
        <tr><td>学生</td><td>网课/学习用电子设备</td><td>"保护发育中的眼睛"</td></tr>
        <tr><td>老年人</td><td>预防黄斑变性风险</td><td>"长远保护视力健康"</td></tr>
      </tbody>
    </table>
""" + B_TIP("💡 关键数据", "成年人平均每天看屏幕7-9小时，学生平均6小时以上。这个数据在推荐防蓝光时非常有说服力。")
)

# ---- Day_13: 第2周 (153行) ----
EXTRA[(BASE2, "Day_13_学习内容.html")] = b_section(
    "📝 补充：配镜处方解读练习",
    """    <p>能快速准确地读懂配镜处方，是眼镜店员工的基本功。以下是几道练习：</p>
    
    <h3>📌 处方案例分析</h3>
    <table class="rule-table">
      <thead><tr><th>处方</th><th>解读</th></tr></thead>
      <tbody>
        <tr><td>R: -3.50 DS<br>L: -4.00 DS<br>PD: 62mm</td><td>右眼近视350度，左眼近视400度，瞳距62mm，无散光，轻度近视，推荐1.67折射率镜片</td></tr>
        <tr><td>R: -6.00 / -1.50 × 180°<br>L: -5.50 / -1.00 × 170°</td><td>双眼高度近视合并散光，度数较深，推荐1.71-1.74超高折射率，减少镜片厚度</td></tr>
        <tr><td>R: +1.50 DS ADD +2.00<br>L: +1.00 DS ADD +2.00</td><td>轻度远视合并老视，需要渐进镜片，近附加+2.00D补偿老花</td></tr>
      </tbody>
    </table>
    <div class="tip-box"><div class="label">💡 练习方法</div><p>每次接待客户拿来处方时，先自己读一遍，再与验光师核对，积累经验。遇到不理解的缩写立即记录，下班后查阅。</p></div>
"""
)

# ---- Day_14: 第2周总结 (178行) ----
EXTRA[(BASE2, "Day_14_学习内容.html")] = b_section(
    "🚀 进入第3周：专业技能训练预览",
    """    <p>第2周，你建立了眼镜行业的光学知识体系。第3周将进入真正的技能实操训练：</p>
    <table class="rule-table">
      <thead><tr><th>第3周主题</th><th>学习目标</th></tr></thead>
      <tbody>
        <tr><td>验光仪器操作</td><td>能独立操作电脑验光仪，记录数据</td></tr>
        <tr><td>综合验光仪使用</td><td>了解综合验光仪的各个旋钮功能</td></tr>
        <tr><td>镜框调整技术</td><td>能对常见镜框进行基础调整</td></tr>
        <tr><td>接待话术实践</td><td>能完整走完接待流程，不卡顿</td></tr>
        <tr><td>处方单解读</td><td>快速准确读懂常见处方格式</td></tr>
      </tbody>
    </table>
    <div class="tip-box"><div class="label">💡 第3周心理准备</div><p>第3周会有很多动手操作，可能会犯错，这是正常的。记住：在真实接待中犯错的代价，远大于在练习中犯错的代价。所以要大胆练习，遇到问题立即向师傅请教。</p></div>
"""
)

print("开始处理第1周文件...")
for fn in ["Day_03_学习内容.html", "Day_04_学习内容.html", "Day_05_学习内容.html", "Day_06_学习内容.html"]:
    key = (BASE1, fn)
    if key not in EXTRA:
        continue
    fp = os.path.join(BASE1, fn)
    lines = insert_before_nav(fp, EXTRA[key])
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")

print("\n开始处理第2周文件...")
for fn in ["Day_08_学习内容.html", "Day_09_学习内容.html", "Day_10_学习内容.html", 
           "Day_11_学习内容.html", "Day_12_学习内容.html", "Day_13_学习内容.html", "Day_14_学习内容.html"]:
    key = (BASE2, fn)
    if key not in EXTRA:
        continue
    fp = os.path.join(BASE2, fn)
    lines = insert_before_nav(fp, EXTRA[key])
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
