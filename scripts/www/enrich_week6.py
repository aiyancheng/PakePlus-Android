import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练"

# ===================== 各文件的扩充内容 =====================

EXTRA = {}

# ---------- Day_37 ----------
EXTRA["Day_37_学习内容.html"] = """
  <div class="nav-footer">
    <a href="Day_36_练习题.html" class="nav-btn outline">← Day 36 练习题</a>
    <a href="Day_37_练习题.html" class="nav-btn">Day 37 练习题 →</a>
  </div>

  <!-- 扩充：心理学角度深度解析 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🧩 深度解析：客户心理与价格感知</h2>
  <div class="card">
    <h3>锚定效应（Anchoring Effect）</h3>
    <p>人的大脑在做价格判断时，会以第一个听到的数字为"锚"。销售时可主动设置高锚点：</p>
    <ul>
      <li>先介绍旗舰款（3000元），再介绍目标款（1800元），客户会觉得1800元更划算</li>
      <li>报价时先说"市场价2500"，再说"我们今天特价1800"，成交感更强</li>
      <li>同类产品从高到低展示，而非从低到高</li>
    </ul>

    <h3>损失厌恶（Loss Aversion）</h3>
    <p>人们对"损失"的痛苦感是"同等收益"带来的快乐感的2倍。利用这一心理：</p>
    <div class="dialogue">
      <span class="staff">员工（错误说法）：</span>"这款镜片有防蓝光功能，很好用。"<br>
      <span class="staff">员工（正确说法）：</span>"不加防蓝光的话，每天8小时盯屏幕，视疲劳会越来越严重，睡眠质量也会下降——这个损失可不小。"
    </div>

    <h3>社会证明（Social Proof）</h3>
    <p>展示其他客户的选择，降低客户的决策风险感：</p>
    <p><em>"这款是我们门店今年卖得最好的，很多和您一样经常用电脑的客户都选了这个。"</em></p>
    <p><em>"上个月刚帮一位老师配了这款，她回来说戴着非常舒适，专门来致谢。"</em></p>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📋 价格谈判实战流程</h2>
  <div class="card">
    <table>
      <tr><th>步骤</th><th>动作</th><th>目的</th></tr>
      <tr><td>第①步</td><td>先确认需求，再报价</td><td>让客户对产品产生认同感后才谈价格</td></tr>
      <tr><td>第②步</td><td>报价时坦然，不主动降价</td><td>体现产品价值和自信</td></tr>
      <tr><td>第③步</td><td>客户提异议时，先认同再解释</td><td>"您说得有道理，确实不便宜……"缓和情绪</td></tr>
      <tr><td>第④步</td><td>用价值和场景重新定义价格</td><td>从"成本"转化为"投资"</td></tr>
      <tr><td>第⑤步</td><td>给出最终方案后沉默等待</td><td>让客户自己说话，不要填补沉默</td></tr>
    </table>

    <div class="warn">
      ⚠️ 常见失误：<br>
      • 客户刚说贵，立刻降价——严重损害产品信誉<br>
      • 不停解释产品特性，忽视客户真实顾虑<br>
      • 使用"能不能再便宜一点"这类开放式问题，给自己挖坑
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🎭 角色扮演练习</h2>
  <div class="card">
    <p>请两人一组，分别扮演"客户"和"员工"，练习以下场景，每个场景练习3分钟：</p>
    <ol>
      <li><strong>场景A</strong>：客户看上一副1200元的镜框，说"能不能便宜200？"——运用附加价值法</li>
      <li><strong>场景B</strong>：客户对比了一家网店，说"网上同款900元，你们凭什么卖1500？"——运用竞品对比法和服务价值强调</li>
      <li><strong>场景C</strong>：客户说"我先回去考虑一下"（准备离开）——运用紧迫感法和总结价值法挽留</li>
    </ol>
    <div class="tip">💡 角色扮演后互相给出反馈：哪句话最有说服力？哪里还可以改进？</div>
  </div>

  <div style="background:linear-gradient(135deg,#eaf4fc,#d0e8f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#1a5276">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>价格异议的本质是价值感知不足，而非真实价格问题</li>
      <li>六大技巧灵活运用，核心都是"转移焦点，从价格到价值"</li>
      <li>成交促进要自然，不是强迫，是帮助客户做出对他有利的决定</li>
      <li>每次异议处理都是练习机会，记录下来，不断优化话术</li>
    </ul>
  </div>
"""

# ---------- Day_38 ----------
EXTRA["Day_38_学习内容.html"] = """
  <!-- 扩充：儿童配镜深度内容 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🔬 儿童视力发育规律详解</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">年龄</th><th style="padding:10px 14px;text-align:left">正常视力范围</th><th style="padding:10px 14px;text-align:left">注意事项</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">0-3岁</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">0.1→0.6</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">视觉快速发育期，避免强光刺激</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">4-6岁</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">0.6→1.0</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">弱视治疗黄金期，发现问题须尽快干预</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">7-12岁</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">0.8→1.2</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">近视高发期，控制近距离用眼时间</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px">13-18岁</td><td style="padding:10px 14px">应达到1.0+</td><td style="padding:10px 14px">度数增长最快，每6个月复查一次</td></tr>
    </table>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">🚦 儿童远视储量（必须了解）</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">儿童天生具有一定远视储量，这是正常的。<strong>用完了远视储量才会发展为近视</strong>：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">3岁：正常远视储量约 +2.00D ~ +3.00D</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">6岁：正常远视储量约 +1.50D ~ +2.00D</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">9岁：正常远视储量约 +0.75D ~ +1.25D</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">12岁：正常远视储量约 +0.25D ~ +0.75D</li>
    </ul>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 家长问"孩子有远视，要不要配镜？"答：不一定。在正常储量范围内的远视不需要配镜，但储量过低则需要干预，避免近视提前发生。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🛡️ 近视防控产品详解</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">OK镜（角膜塑形镜）</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">夜间佩戴，通过对角膜的轻度塑形，白天裸眼视力改善，同时减缓眼轴增长（延缓近视进展约40-60%）。</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">适合年龄：8岁以上，度数-0.75D ~ -6.00D</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">需要专业验配和定期复查</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">价格较高（3000~8000元/年），但防控效果好</li>
    </ul>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">离焦镜片（防控近视镜片）</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">通过特殊设计的镜片（如蜂窝微透镜）在视网膜周边产生近视性离焦，从光学上控制眼轴增长。</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">代表产品：依视路星趣控、豪雅MiYOSMART</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">佩戴方式与普通眼镜相同，接受度高</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">临床研究显示：延缓近视进展约67%</li>
    </ul>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">低浓度阿托品滴眼液（0.01%）</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">医疗手段，需眼科医生处方，不在门店销售范围，但员工需了解，方便解答家长咨询并建议就医。</p>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">👨‍👩‍👧 家长沟通实战对话</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#e67e22;font-weight:600">家长：</span>"孩子才8岁，就近视了，是不是遗传的？"<br>
      <span style="color:#2980b9;font-weight:600">员工：</span>"遗传因素确实有影响，父母都近视的孩子风险会高一些。但更重要的是后天用眼习惯。研究发现每天户外活动2小时以上，可以大幅降低近视风险。现在配一副好眼镜，同时养成好习惯，可以有效控制度数增长。"
    </div>

    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#e67e22;font-weight:600">家长：</span>"配眼镜会不会让度数越来越深？"<br>
      <span style="color:#2980b9;font-weight:600">员工：</span>"这是一个很常见的误解。不配镜才会让度数加深得更快——孩子看不清楚就会凑近，用眼压力更大。正确的做法是及时配镜矫正，同时选择防控型镜片，帮助控制眼轴增长。"
    </div>

    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#e67e22;font-weight:600">家长：</span>"普通镜片和防控镜片差这么多钱，真的有效果吗？"<br>
      <span style="color:#2980b9;font-weight:600">员工：</span>"多项临床研究都证实了防控镜片的效果，平均可延缓近视进展约60%。孩子的眼睛一旦高度近视（超过600度）就会增加各种眼底疾病风险。从长远看，防控是最值得的投资。我可以给您看一下相关的数据对比……"
    </div>
  </div>

  <div style="background:linear-gradient(135deg,#eaf4fc,#d0e8f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#1a5276">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>儿童配镜核心：准确判断真性/假性近视，建议散瞳验光</li>
      <li>了解视力发育规律和远视储量概念，能有效引导家长正确认知</li>
      <li>近视防控产品知识是儿童配镜的核心竞争力</li>
      <li>家长沟通要专业、有耐心，多用科学依据增强说服力</li>
    </ul>
  </div>
"""

# ---------- Day_39 ----------
EXTRA["Day_39_学习内容.html"] = """
  <!-- 扩充：渐进镜深度内容 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🔍 渐进多焦点镜片深度解析</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">镜片区域划分</h3>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">区域</th><th style="padding:10px 14px;text-align:left">位置</th><th style="padding:10px 14px;text-align:left">功能</th><th style="padding:10px 14px;text-align:left">适合场景</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">远用区</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镜片上方</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">看远处</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">开车、看黑板、走路</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">中间区</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镜片中部</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">中距离视野</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">看电脑屏幕（60~80cm）</td></tr>
      <tr><td style="padding:10px 14px">近用区</td><td style="padding:10px 14px">镜片下方</td><td style="padding:10px 14px">看近处</td><td style="padding:10px 14px">读书、看手机（40cm左右）</td></tr>
    </table>

    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:10px 14px;border-radius:0 8px 8px 0;color:#856404;margin:10px 0">
      ⚠️ 渐进镜两侧有"像差区"，初戴者低头走路或快速转动头部时可能有轻微失真感，这是正常现象。建议分步适应：先坐着看（第1-2天）→ 再走动（第3-5天）→ 逐渐正常使用。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🎯 渐进镜验配关键步骤</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <ol style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>确认适应症</strong>：老视度数≥+0.75D，有远近视力需求，愿意接受适应期</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>测量瞳孔高度</strong>：在镜架上标记瞳孔位置（瞳高），这是渐进镜最关键的参数</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>选择镜片类型</strong>：根据老视度数、加光量、生活习惯推荐合适的渐进镜型号</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>试戴说明</strong>：取镜时详细演示如何使用（看远抬头、看近低头、侧方视物转头不转眼）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>跟进回访</strong>：一周后主动联系，了解适应情况，解答疑问</li>
    </ol>

    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 瞳孔高度测量不准确是渐进镜不舒适的最常见原因。必须让客户戴上镜架，直视前方，由验光师用标记笔精确标注瞳孔中心位置。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">💬 老年客户的特殊需求与沟通</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">常见担忧与解答</h3>
    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#e67e22;font-weight:600">客户：</span>"渐进镜那么贵，你说值不值？"<br>
      <span style="color:#2980b9;font-weight:600">员工：</span>"阿姨，您想想看，如果您每天要拿掉眼镜才能看手机，再戴上眼镜去看电视，换来换去多麻烦。渐进镜就是为了解决这个烦恼的——一副眼镜远近都能看，您出门也不用带两副了。很多阿姨配了之后说'早就应该配了'。"
    </div>

    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#e67e22;font-weight:600">客户：</span>"我朋友说戴渐进镜头晕，不敢配。"<br>
      <span style="color:#2980b9;font-weight:600">员工：</span>"头晕通常是因为瞳孔高度没测准，或者镜片质量差。我们这里有专业设备精确测量，而且有适应期保障——如果真的适应不了，我们会为您重新评估方案。您可以先试戴几分钟感受一下。"
    </div>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">关怀服务细节</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">取镜时当面演示镜片清洁方法（用专用布，避免干擦）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">告知定期复查时间（老视每年可能增加约+0.25D）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">送上联系方式，方便有问题随时来店</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">如有子女陪同，也对子女讲解护眼重要性，扩大影响力</li>
    </ul>
  </div>

  <div style="background:linear-gradient(135deg,#eaf4fc,#d0e8f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#1a5276">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>老视是生理现象，40岁后普遍发生，度数随年龄增长</li>
      <li>渐进镜是最优解，核心在于精准测量瞳高和详细适应指导</li>
      <li>中老年客户重视信任感，专业+耐心+关怀是成交的关键</li>
      <li>口碑效应强：服务好一位老年客户，往往能带来多位亲友转介绍</li>
    </ul>
  </div>
"""

# ---------- Day_40 ----------
EXTRA["Day_40_学习内容.html"] = """
  <!-- 扩充：太阳镜品质鉴别与场景销售 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🔎 太阳镜品质鉴别方法</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">现场鉴别偏光镜真伪</h3>
    <ol style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>水平旋转测试</strong>：将两片偏光镜叠放，旋转90°，如变暗则是真正偏光镜（偏振方向垂直时会阻光）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>屏幕测试</strong>：对着手机/电脑屏幕，旋转镜片，偏光镜会在某角度让屏幕变暗</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>标签确认</strong>：正规太阳镜应标注UV400或100% UV Protection</li>
    </ol>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">镜片光学质量检查</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">透过镜片看直线（如门框），如有弯曲变形说明光学质量差</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">逆光检查镜片，应无气泡、划痕、压纹等缺陷</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">进出室内应颜色一致（变色镜除外），无色差或白雾感</li>
    </ul>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🌈 镜片颜色与适用场景对照</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">镜片颜色</th><th style="padding:10px 14px;text-align:left">特点</th><th style="padding:10px 14px;text-align:left">适用场景</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">灰色</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">减光不失真，色彩还原最自然</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">日常通用、开车、强日照</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">茶/棕色</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">增强对比度，使景物更清晰</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">阴天、开车、运动</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">绿色</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">吸收紫外线同时柔化强光</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">高尔夫、草地运动</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">黄/橙色</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">增强低光环境下的清晰度</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">阴天、雾天、射击运动</td></tr>
      <tr><td style="padding:10px 14px">蓝/紫色</td><td style="padding:10px 14px">时尚装饰性强，防UV效果一般</td><td style="padding:10px 14px">时尚搭配，非专业防护</td></tr>
    </table>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🏃 运动眼镜与特殊场景眼镜</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">运动眼镜关键特性</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>镜框材质</strong>：TR-90（轻盈有弹性）、PC（抗冲击）、钛合金（轻量化）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>防滑设计</strong>：橡胶鼻托、内嵌防滑鼻梁、弯曲镜腿端头</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>可替换镜片</strong>：不同颜色镜片适应不同光线条件</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>防雾涂层</strong>：适合高强度运动、自行车、滑雪场景</li>
    </ul>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">驾驶专用眼镜</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">偏光镜：消除水面、路面的水平反射眩光</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">夜驾眼镜（黄色防眩光）：增强夜间对比度，减少迎面灯光散射</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">近视驾驶者推荐：近视太阳镜或变色近视镜</li>
    </ul>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 销售话术：<em>"您开车多吗？夏天阳光强烈，路面反光特别厉害，开车没有偏光镜真的很危险。我们这款偏光驾驶镜，不仅防紫外线，消除眩光的效果特别好，很多老司机的首选。"</em>
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">💎 防蓝光眼镜详解与销售话术</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">蓝光的双面性</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">蓝光并非全部有害：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>有益蓝光（480-500nm）</strong>：调节生物钟、提升注意力，适量接触有益</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>有害蓝光（380-440nm）</strong>：高能量，长期接触可能损伤视网膜黄斑，影响睡眠</li>
    </ul>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">防蓝光镜片主要过滤380-440nm的有害蓝光，保留有益蓝光。</p>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">目标客群话术</h3>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">客群</th><th style="padding:10px 14px;text-align:left">推荐切入点</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">程序员/设计师</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">每天盯屏8小时以上，防蓝光缓解视疲劳，下班眼睛还是亮的</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">学生/家长</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">孩子网课多，防蓝光保护发育中的眼睛，也帮助睡前不刷手机入睡更快</td></tr>
      <tr><td style="padding:10px 14px">中老年人</td><td style="padding:10px 14px">老年黄斑病变风险更高，防蓝光是预防性保护</td></tr>
    </table>
  </div>

  <div style="background:linear-gradient(135deg,#eaf4fc,#d0e8f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#1a5276">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>太阳镜核心功能是防紫外线，颜色深浅≠防护效果</li>
      <li>偏光镜适合驾驶和户外，掌握现场演示偏光效果的方法</li>
      <li>镜片颜色不同，适用场景不同，根据客户用途精准推荐</li>
      <li>防蓝光眼镜针对长时间屏幕用户，蓝光危害和益处都要了解</li>
      <li>交叉销售最佳时机：客户成单后心情最好的那一刻</li>
    </ul>
  </div>
"""

# ---------- Day_41 ----------
EXTRA["Day_41_学习内容.html"] = """
  <!-- 扩充：售后服务体系 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📱 客户档案管理系统</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">一份好的客户档案应包含</h3>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">信息类别</th><th style="padding:10px 14px;text-align:left">具体内容</th><th style="padding:10px 14px;text-align:left">用途</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">基本信息</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">姓名、联系方式、生日、职业</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">基础联系和生日关怀</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">配镜历史</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">每次的度数、镜片品牌、镜框、价格</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">度数变化追踪、复购参考</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">视力状况</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">近视/远视/散光度数，瞳距，特殊需求</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">下次配镜快速参考</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">偏好记录</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镜框风格（商务/时尚/休闲）、材质偏好</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">个性化推荐依据</td></tr>
      <tr><td style="padding:10px 14px">回访节点</td><td style="padding:10px 14px">上次配镜日期、下次复查提醒日期</td><td style="padding:10px 14px">主动回访计划</td></tr>
    </table>

    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 养成习惯：每接待一位客户，当天就完善档案，趁记忆新鲜。客户离开后补录的信息往往不完整。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📞 回访话术设计</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">取镜后3天回访（适应回访）</h3>
    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#2980b9;font-weight:600">员工：</span>"您好，王先生，我是XX眼镜店的小李，您上周四取的眼镜，不知道现在戴着感觉怎么样？适应了吗？<br>
      <em>（等待回应）</em><br>
      如果有任何不适，比如镜框松了、看某个距离不清楚，随时欢迎来店免费调整。我们希望您戴得舒舒服服的！"
    </div>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">配镜后6个月复查提醒</h3>
    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#2980b9;font-weight:600">员工：</span>"您好，李阿姨，我是XX眼镜店小张。您上半年在我们这里配了老花镜，不知道用得顺不顺手？您平时看书看手机清楚吗？<br>
      半年过去了，老花度数可能略有变化，建议您近期来我们这复查一下视力，顺便帮您的眼镜做个免费清洁保养，这个服务是我们一直提供的！"
    </div>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">节日关怀回访</h3>
    <div style="background:#f8f9fa;border-radius:10px;padding:16px 20px;margin:12px 0;border:1px solid #dee2e6">
      <span style="color:#2980b9;font-weight:600">员工（微信消息）：</span>"[节日] 节快乐！我是XX眼镜店小王，祝您和家人节日愉快、身体健康～ 有需要配镜或保养的，随时来找我，我帮您安排 😊"
    </div>

    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:10px 14px;border-radius:0 8px 8px 0;color:#856404;margin:10px 0">
      ⚠️ 回访注意：时间选择工作日下午2-5点或晚上7-9点；第一句话说明身份；保持简短（1-2分钟）；不要在回访中硬推销产品，主要是关怀。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🔧 常见售后问题处理</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">问题</th><th style="padding:10px 14px;text-align:left">原因分析</th><th style="padding:10px 14px;text-align:left">处理方式</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">眼镜松了/夹脸</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">鼻托或镜腿需调整</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">免费上门或到店调整，当场解决</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镜片有雾/发黄</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镀膜损伤或老化</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">检查是否在保修期内，说明镀膜维护方法</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">戴着头晕</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">度数不准/渐进镜适应期</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">先判断原因，必要时重新验光或调整</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">镜架断裂</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">外力损坏或质量问题</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">区分人为损坏与质量问题，按规定处理</td></tr>
      <tr><td style="padding:10px 14px">客户不满意要退款</td><td style="padding:10px 14px">多种原因</td><td style="padding:10px 14px">先耐心倾听，按政策处理，必要时升级店长</td></tr>
    </table>
  </div>

  <div style="background:linear-gradient(135deg,#eaf4fc,#d0e8f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#1a5276">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>完善的客户档案是长期经营的基础，每次接单就要记录</li>
      <li>主动回访是建立信任、促进复购的关键动作</li>
      <li>售后服务的核心是"快速响应+解决问题+留住客户"</li>
      <li>口碑转介绍往往来自售后体验，不仅仅是产品本身</li>
    </ul>
  </div>
"""

# ---------- Day_42 ----------
EXTRA["Day_42_学习内容.html"] = """
  <!-- 扩充：本周能力回顾与第7周备战 -->
  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">💡 独立接单核心能力体系</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">经过第6周的系统训练，一名合格的独立接单员工应具备以下能力：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">能力维度</th><th style="padding:10px 14px;text-align:left">具体表现</th><th style="padding:10px 14px;text-align:left">自评</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">接待流程</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">7步接待全程流畅，无明显卡顿</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">需求挖掘</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">能用开放式问题了解客户真实需求</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">产品推荐</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">能根据需求匹配合适镜片和镜框</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">异议处理</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">能应对价格/质量/比较等常见异议</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">特殊客群</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">儿童/老年客户能专业应对</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">交叉销售</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">每天至少尝试1次太阳镜/防蓝光推荐</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 达标 □ 需练习</td></tr>
      <tr><td style="padding:10px 14px">售后服务</td><td style="padding:10px 14px">主动回访，建立客户档案</td><td style="padding:10px 14px">□ 达标 □ 需练习</td></tr>
    </table>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📊 本周数据复盘表</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">请尽量回忆本周（Day 36-41）的实战数据，诚实填写：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">数据项</th><th style="padding:10px 14px;text-align:left">本周实际</th><th style="padding:10px 14px;text-align:left">与上周对比</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">独立接待客户数</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">___人</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 增加 □ 持平 □ 减少</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">成单数</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">___单</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 增加 □ 持平 □ 减少</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">平均客单价</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">¥___</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">□ 增加 □ 持平 □ 减少</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">交叉销售成功次数</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">___次</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">—</td></tr>
      <tr><td style="padding:10px 14px">遇到的最大挑战</td><td style="padding:10px 14px" colspan="2">___________________</td></tr>
    </table>

    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 带上这份复盘表，和师傅进行一次30分钟的深度1v1复盘，听取针对你个人的成长建议。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🚀 第7周预习：综合提升方向</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">第7周的训练将在第6周基础上进一步提升：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">🎯 <strong>高端产品销售</strong>：名牌镜框、高折射率超薄镜片、定制镜片的推荐逻辑</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">📈 <strong>客单价提升策略</strong>：从普通推荐到价值升级，如何合理引导客户提升消费</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">🤝 <strong>大客户/企业客户开发</strong>：团体配镜、企业客户维护</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">📱 <strong>线上口碑与社群运营</strong>：如何通过社交媒体扩大门店影响力</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">🏆 <strong>综合能力考核</strong>：模拟真实接待场景的全程考核</li>
    </ul>

    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 完成第6周，你已经从"需要人带"成长为"能独立作战"。第7周目标：成为"被客户主动信任"的专业顾问！
    </div>
  </div>
"""

# ===================== 处理函数 =====================

def enrich_file(filepath, extra_html):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    # 在 nav-footer 之前插入（如果已有nav-footer），否则在 </div>\n</body> 前插入
    if 'nav-footer' in extra_html:
        # 替换已有的 nav-footer（如果有的话）
        target = '</div>\n</body>'
        if target not in content:
            target = '</div>\r\n</body>'
        if target not in content:
            # 找到最后一个 </div> 之前插入
            last_div = content.rfind('</div>')
            new_content = content[:last_div] + extra_html + '\n' + content[last_div:]
        else:
            new_content = content.replace(target, extra_html + '\n</div>\n</body>', 1)
    else:
        # 在 nav-footer 之前插入
        nav_idx = content.rfind('<div class="nav-footer"')
        if nav_idx == -1:
            nav_idx = content.rfind('</div>\n</body>')
            if nav_idx == -1:
                nav_idx = content.rfind('</body>')
        new_content = content[:nav_idx] + extra_html + '\n  ' + content[nav_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # 统计行数
    lines = new_content.count('\n') + 1
    return lines

# ===================== 执行 =====================
for filename, extra in EXTRA.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print(f"⚠️  文件不存在: {filename}")
        continue
    new_lines = enrich_file(filepath, extra)
    print(f"✅ {filename}: 现在 {new_lines} 行")
