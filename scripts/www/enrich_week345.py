import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE3 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第3周_专业技能训练"
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

EXTRAS = {}

# ---- Day_15: 验光辅助操作入门 (170行) ----
EXTRAS[(BASE3, "Day_15_学习内容.html")] = """  <div class="section">
    <h2>🔬 电脑验光仪操作详解</h2>
    <h3>📌 操作前准备</h3>
    <ul>
      <li>检查仪器是否正常开机，打印纸是否充足</li>
      <li>调整椅子高度，使客户下巴自然放置于托架</li>
      <li>确认房间光线适中，不过亮也不过暗</li>
    </ul>
    <h3>📌 测量步骤</h3>
    <ol style="padding-left:20px;margin-bottom:14px;">
      <li style="margin-bottom:6px;">嘱咐客户放松，注视仪器内的目标图案（通常是气球/热气球）</li>
      <li style="margin-bottom:6px;">调整焦距，使目标图案清晰对焦</li>
      <li style="margin-bottom:6px;">按下测量键，自动测量3次取均值</li>
      <li style="margin-bottom:6px;">先测右眼，遮盖左眼；再测左眼，遮盖右眼</li>
      <li style="margin-bottom:6px;">打印数据，核对并签名</li>
    </ol>
    <div class="tip-box" style="background:#fff3e0;border-left:4px solid #FF9800;">
      <div class="label" style="color:#e65100;">💡 注意事项</div>
      <p>电脑验光仅是初始参考，不能直接作为配镜处方。需要后续进行主觉验光确认。告知客户"这是初步检测，后面还需要您配合进一步确认"。</p>
    </div>
  </div>

  <div class="section">
    <h2>📐 视力表使用规范</h2>
    <ul>
      <li>视力表距离：国际标准5米（或镜像5米）</li>
      <li>检查环境：光线充足均匀，无眩光</li>
      <li>先查裸眼视力，再查矫正视力</li>
      <li>从较大字符向下，找到能辨认的最小行</li>
      <li>每行字符辨认率大于50%才计入该行视力</li>
    </ul>
    <p>视力记录：如能辨认0.8行但不能全部辨认0.9行，记录为0.8。</p>
  </div>

"""

# ---- Day_16: 镜架调整与整形技术 (188行) ----
EXTRAS[(BASE3, "Day_16_学习内容.html")] = """  <div class="section">
    <h2>🔧 常见镜架问题与解决方案</h2>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <thead><tr style="background:#FF9800;color:#fff"><th style="padding:10px 14px;text-align:left">问题</th><th style="padding:10px 14px;text-align:left">原因</th><th style="padding:10px 14px;text-align:left">解决方法</th></tr></thead>
      <tbody>
        <tr><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">镜架歪斜</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">两腿不对称</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">调整镜腿张开角度至对称</td></tr>
        <tr style="background:#fff3e0"><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">鼻梁压鼻</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">鼻托间距过窄</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">用专用工具调宽鼻托间距</td></tr>
        <tr><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">镜腿夹耳</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">镜腿弯曲点太前</td><td style="padding:10px 14px;border-bottom:1px solid #ffe0b2">加热后将弯曲点向后移</td></tr>
        <tr style="background:#fff3e0"><td style="padding:10px 14px">镜片松动</td><td style="padding:10px 14px">螺丝松弛</td><td style="padding:10px 14px">用眼镜螺丝刀拧紧，或更换新螺丝</td></tr>
      </tbody>
    </table>
    <div class="tip-box" style="background:#fff3e0;border-left:4px solid #FF9800;">
      <div class="label" style="color:#e65100;">⚠️ 材质注意</div>
      <p>板材（醋酸纤维）镜架：需用热风枪加热软化后调整，不可冷折，否则容易断裂。金属镜架：可直接调整，力度要小，分多次完成，避免突然用力折断。</p>
    </div>
  </div>

"""

# ---- Day_23: 产品介绍话术 (185行) ----
EXTRAS[(BASE4, "Day_23_学习内容.html")] = """  <div class="card">
    <h2>🎭 FAB话术练习场景</h2>
    <p>FAB是产品介绍的黄金公式：<strong>Feature（特性）→ Advantage（优势）→ Benefit（利益）</strong></p>
    <h3>练习案例1：1.67超薄镜片</h3>
    <ul>
      <li><strong>F</strong>：折射率1.67，比普通1.56高出很多</li>
      <li><strong>A</strong>：同等度数下，镜片厚度减少约30-40%</li>
      <li><strong>B</strong>：您戴起来镜片更薄更美观，旁人看不出度数，整体颜值大幅提升</li>
    </ul>
    <h3>练习案例2：渐进多焦点镜片</h3>
    <ul>
      <li><strong>F</strong>：一片镜片包含远中近三个视区</li>
      <li><strong>A</strong>：不需要摘镜换镜，一副搞定所有距离的视力需求</li>
      <li><strong>B</strong>：您开车、用电脑、看手机都不需要换眼镜，出门也不用带两副，非常方便</li>
    </ul>
    <h3>练习案例3：防蓝光镜片</h3>
    <ul>
      <li><strong>F</strong>：镜片含特殊涂层，过滤380-440nm有害蓝光</li>
      <li><strong>A</strong>：长时间看屏幕不容易疲劳，睡前接触蓝光减少，睡眠质量改善</li>
      <li><strong>B</strong>：您每天用电脑这么多小时，下班后眼睛不酸涩，回家还有精神陪家人</li>
    </ul>
  </div>

"""

# ---- Day_24: 价格异议处理话术 (182行) ----
EXTRAS[(BASE4, "Day_24_学习内容.html")] = """  <div class="card">
    <h2>🎯 话术优化对比练习</h2>
    <p>同样的内容，不同的表达方式，效果差距巨大：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <thead><tr style="background:#43e97b;color:#fff"><th style="padding:10px 14px;text-align:left">情景</th><th style="padding:10px 14px;text-align:left">弱话术（❌）</th><th style="padding:10px 14px;text-align:left">强话术（✅）</th></tr></thead>
      <tbody>
        <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">客户嫌贵</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"这个价格已经很便宜了"</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"这副镜片您至少用3年，平均每天只要X元，而且用的是XX品牌，质量有保障"</td></tr>
        <tr style="background:#f0fff0"><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">客户问能否打折</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"打折是不行的"</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"价格这边已经是最优惠了，不过我可以帮您申请一个专属礼品，另外我们有2年免费保养服务"</td></tr>
        <tr><td style="padding:10px 14px">客户说要考虑</td><td style="padding:10px 14px">"好的，您慢慢考虑"</td><td style="padding:10px 14px">"我理解，这是大事。有什么顾虑我帮您解答？这款库存不多，我帮您暂时预留一下？"</td></tr>
      </tbody>
    </table>
    <div style="background:#e8f5e9;border-left:4px solid #43e97b;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:14px">
      💡 好的话术不是背稿，而是真心站在客户角度，找到对他们最有价值的角度来表达。
    </div>
  </div>

"""

# ---- Day_26: 连带销售与会员维护 (181行) ----
EXTRAS[(BASE4, "Day_26_学习内容.html")] = """  <div class="section">
    <h2>🎁 连带销售实战技巧</h2>
    <h3>📌 连带销售时机识别</h3>
    <ul>
      <li>客户成单后心情好的时刻——是推荐的最佳时机</li>
      <li>客户提到其他场景需求（开车、运动、户外）</li>
      <li>客户子女或同伴在场，可顺势服务</li>
    </ul>
    <h3>📌 会员积分运用技巧</h3>
    <p>在结账时自然引入会员：</p>
    <p><em>"您今天消费满XX元，如果成为我们会员，可以获得XXX积分，下次使用相当于优惠了XX元。您今天就开通吗？只需要手机号就可以。"</em></p>
    <div style="background:#e8f5e9;border-left:4px solid #4CAF50;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:14px">
      💡 会员不只是打折工具，更是建立客户档案、实现精准回访的重要手段。每位建档会员的价值远超一次性消费。
    </div>
  </div>

"""

# ---- Day_27: 投诉处理与危机公关 (174行) ----
EXTRAS[(BASE4, "Day_27_学习内容.html")] = """  <div class="section">
    <h2>💼 投诉预防：从根源减少投诉</h2>
    <p>最好的投诉处理，是让投诉不发生。以下环节是投诉高发区：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <thead><tr style="background:#4CAF50;color:#fff"><th style="padding:10px 14px;text-align:left">易出问题环节</th><th style="padding:10px 14px;text-align:left">常见投诉</th><th style="padding:10px 14px;text-align:left">预防措施</th></tr></thead>
      <tbody>
        <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">验光</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">度数不准，戴了头晕</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">充分主觉验光，试戴确认，详细记录</td></tr>
        <tr style="background:#f0fff0"><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">加工</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">参数错误，瞳距偏差</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">工单填写仔细，加工前核对</td></tr>
        <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">取镜</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">未当场确认，问题发现晚</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">取镜时必须当面试戴确认</td></tr>
        <tr style="background:#f0fff0"><td style="padding:10px 14px">承诺不兑现</td><td style="padding:10px 14px">说好的服务没做到</td><td style="padding:10px 14px">谨慎承诺，做到才说，超预期兑现</td></tr>
      </tbody>
    </table>
  </div>

"""

# ---- Day_31: FAB法则演练 (183行) ----
EXTRAS[(BASE5, "Day_31_学习内容.html")] = """  <div class="card" style="background:white;border-radius:12px;padding:30px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:20px;color:#333;margin-bottom:18px;padding-bottom:12px;border-bottom:2px solid #11998e">🎭 FAB实战升级：情感化表达</h2>
    <p>技术FAB只说产品，情感FAB连接客户内心。对比：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#11998e;color:#fff"><th style="padding:10px 14px;text-align:left">层次</th><th style="padding:10px 14px;text-align:left">示例</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">技术FAB</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"这款镜片折射率1.67，比普通镜片薄40%"</td></tr>
      <tr style="background:#f0fff8"><td style="padding:10px 14px">情感FAB</td><td style="padding:10px 14px">"这款镜片和您现在的相比，薄了将近一半。想象一下，朋友同事看到您的眼镜，根本猜不到您是高度近视——这种自信，是普通镜片给不了的。"</td></tr>
    </table>
    <div style="background:#e8f5f0;border-left:4px solid #11998e;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:14px">
      💡 情感FAB的关键：用客户能感受到的具体场景替代抽象参数，让他们自己想象拥有产品后的美好状态。
    </div>
  </div>

"""

# ---- Day_32: 验光流程实操 (178行) ----
EXTRAS[(BASE5, "Day_32_学习内容.html")] = """  <div class="card" style="background:white;border-radius:12px;padding:30px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:20px;color:#333;margin-bottom:18px;padding-bottom:12px;border-bottom:2px solid #11998e">📋 跟岗观察清单</h2>
    <p>在协助验光师接待时，记录以下观察点，有助于快速提升：</p>
    <ul style="padding-left:20px;line-height:1.8">
      <li>验光师如何向客户解释验光过程？用了哪些通俗比喻？</li>
      <li>遇到儿童/老年/高度数客户，验光师如何调整策略？</li>
      <li>验光结果与客户预期不符时，如何沟通？</li>
      <li>主觉验光中哪一步花时间最长？为什么？</li>
      <li>取镜时验光师如何进行质量确认？</li>
    </ul>
    <div style="background:#e8f5f0;border-left:4px solid #11998e;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:14px">
      💡 每次跟岗后，把观察记录整理成笔记，一个月后回看，你会发现自己进步的轨迹。
    </div>
  </div>

"""

# ---- Day_33: 制单与交付 (191行) ----
EXTRAS[(BASE5, "Day_33_学习内容.html")] = """  <div class="card" style="background:white;border-radius:12px;padding:30px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:20px;color:#333;margin-bottom:18px;padding-bottom:12px;border-bottom:2px solid #11998e">✅ 取镜验收标准流程</h2>
    <ol style="padding-left:20px;line-height:1.8">
      <li style="margin-bottom:6px;">核对工单：镜片度数、轴向、瞳距与工单一致</li>
      <li style="margin-bottom:6px;">外观检查：无划痕、气泡、压纹、色差</li>
      <li style="margin-bottom:6px;">光学检测：焦度计测量确认度数偏差在允许范围内（国标±0.25D）</li>
      <li style="margin-bottom:6px;">镜架检查：无变形，镜腿开合顺畅，螺丝紧固</li>
      <li style="margin-bottom:6px;">客户试戴：请客户佩戴并走动，确认舒适度和视力效果</li>
      <li style="margin-bottom:6px;">使用说明：告知清洁方法、保养注意事项、保修政策</li>
    </ol>
    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:14px;color:#856404">
      ⚠️ 不要省略取镜验收环节。"我看着没问题"不是专业，用焦度计测量数据才是专业。每一步都有意义。
    </div>
  </div>

"""

# ---- Day_34: 客诉处理实战 (168行) ----
EXTRAS[(BASE5, "Day_34_学习内容.html")] = """  <div class="card" style="background:white;border-radius:12px;padding:30px;margin-bottom:24px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
    <h2 style="font-size:20px;color:#333;margin-bottom:18px;padding-bottom:12px;border-bottom:2px solid #11998e">🔄 投诉转化：从危机到机会</h2>
    <p>研究表明：投诉被妥善处理的客户，比从未投诉的客户忠诚度更高。</p>
    <h3 style="font-size:16px;color:#444;margin:18px 0 10px">处理投诉的HEART原则</h3>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#11998e;color:#fff"><th style="padding:10px 14px;text-align:left">字母</th><th style="padding:10px 14px;text-align:left">含义</th><th style="padding:10px 14px;text-align:left">具体行动</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0"><strong>H</strong>ear</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">倾听</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">不打断，听完客户所有不满</td></tr>
      <tr style="background:#f0fff8"><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0"><strong>E</strong>mpathize</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">同理</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">"我理解您的感受……"</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0"><strong>A</strong>pologize</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">致歉</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">为不好的体验道歉（不等于承认错误）</td></tr>
      <tr style="background:#f0fff8"><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0"><strong>R</strong>esolve</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">解决</td><td style="padding:10px 14px;border-bottom:1px solid #e0f0e0">提出具体可行的解决方案</td></tr>
      <tr><td style="padding:10px 14px"><strong>T</strong>hank</td><td style="padding:10px 14px">感谢</td><td style="padding:10px 14px">"感谢您告诉我们，帮助我们做得更好"</td></tr>
    </table>
  </div>

"""

# ---- Day_35: 跟岗总结与成长复盘 (161行) ----
EXTRAS[(BASE5, "Day_35_学习内容.html")] = """  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📊 第5周技能达标检验</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">检验自己本周实践效果：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">技能点</th><th style="padding:10px 14px;text-align:left">本周实践了吗？</th><th style="padding:10px 14px;text-align:left">自评</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">FAB产品介绍</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□是 □否</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□流畅 □卡顿 □未尝试</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">协助验光接待</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□是 □否</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□流畅 □卡顿 □未尝试</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">工单填写与取镜</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□是 □否</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□流畅 □卡顿 □未尝试</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px">处理一次投诉/异议</td><td style="padding:10px 14px">□是 □否</td><td style="padding:10px 14px">□成功 □部分成功 □失败</td></tr>
    </table>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🚀 进入第6周：独立接单训练</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">第5周你完成了跟岗实战，第6周将正式进入独立接单训练：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">你将独立接待客户，而不只是协助</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">遇到困难可以求助，但要先独立尝试</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">每天记录成功和失败案例，持续改进</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">目标：完成至少10次完整的独立接单</li>
    </ul>
    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 跟岗是学习，独立接单是成长。从今天起，开始真正的蜕变！
    </div>
  </div>

"""

print("处理第3周文件...")
for fn, extra in [(k[1], v) for k, v in EXTRAS.items() if k[0]==BASE3]:
    fp = os.path.join(BASE3, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")

print("\n处理第4周文件...")
for fn, extra in [(k[1], v) for k, v in EXTRAS.items() if k[0]==BASE4]:
    fp = os.path.join(BASE4, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")

print("\n处理第5周文件...")
for fn, extra in [(k[1], v) for k, v in EXTRAS.items() if k[0]==BASE5]:
    fp = os.path.join(BASE5, fn)
    lines = insert_before_nav(fp, extra)
    status = "✅" if lines >= 200 else "⚠️ "
    print(f"  {status} {fn}: {lines} 行")
