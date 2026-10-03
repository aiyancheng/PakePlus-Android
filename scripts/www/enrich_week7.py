import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE7 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第7周_综合提升训练"
BASE8 = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第8周_结业冲刺与毕业考核"

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

# ---- Day_43: 验光技能深化 ----
EXTRAS[(BASE7, "Day_43_学习内容.html")] = """  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">🧪 验光实操常见问题解答</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <h3 style="color:#8e44ad;font-size:1rem;margin-top:18px">Q: 客户说"看哪个都差不多"怎么办？</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px">这通常意味着度数差异在其辨识阈值以下，或客户调节介入。处理方式：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">换用更小的视标行（0.8→1.0）来提高敏感度</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">重新雾视，让眼睛充分放松后再次检查</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">告知客户"不是找最清楚，而是找第一感觉"</li>
    </ul>

    <h3 style="color:#8e44ad;font-size:1rem;margin-top:18px">Q: 电脑验光和主觉验光结果差很多怎么处理？</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px">差异在±0.50D以内属正常范围。超过此范围需分析：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">客户调节痉挛（假性近视）：主觉验光通过雾视已消除调节，结果更准</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">角膜不规则：电脑验光误差更大，以主觉为准</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">以主觉验光为最终处方参考</li>
    </ul>

    <h3 style="color:#8e44ad;font-size:1rem;margin-top:18px">Q: 客户不适应新处方（戴了头晕）如何处置？</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">先核实是否真的头晕（区分"眼镜本身问题"和"适应期不适"）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">检查加工参数：瞳距、瞳高、轴向是否准确</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">若加工无误，考虑适当降低度数（如-0.25D），特别是高度数客户</li>
    </ul>
  </div>

  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">📋 验光记录单规范填写</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">规范的验光记录是配镜质量的保障，也是处理纠纷的证据：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#8e44ad;color:#fff"><th style="padding:10px 14px;text-align:left">必填项目</th><th style="padding:10px 14px;text-align:left">注意要点</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">客户姓名+联系方式</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">方便回访和档案建立</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px;border-bottom:1px solid #e8daef">裸眼视力（戴镜前）</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">远/近各记录一次</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">电脑验光数据</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">原始数据保留，不要修改</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px;border-bottom:1px solid #e8daef">主觉验光处方</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">双眼各项参数+瞳距</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">矫正视力（戴镜后）</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">记录最终矫正视力</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px">验光师签名</td><td style="padding:10px 14px">对处方负责，不可代签</td></tr>
    </table>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 每一步验光都认真记录，不仅保护客户，也保护自己。处理投诉时，完整的验光记录是最好的证据。
    </div>
  </div>

  <div style="background:linear-gradient(135deg,#f5eef8,#e8daef);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#6c3483">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>主觉验光7步骤要熟练，每步都有其目的和注意事项</li>
      <li>雾视是关键步骤，特别对青少年，不可省略</li>
      <li>散光轴向比度数更重要，要耐心精确确认</li>
      <li>验光记录规范填写，是专业性的体现</li>
    </ul>
  </div>

"""

# ---- Day_44: 高端产品销售 ----
EXTRAS[(BASE7, "Day_44_学习内容.html")] = """  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">💡 高端镜片技术术语详解</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#8e44ad;color:#fff"><th style="padding:10px 14px;text-align:left">术语</th><th style="padding:10px 14px;text-align:left">解释</th><th style="padding:10px 14px;text-align:left">销售价值</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">非球面设计</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">镜片边缘像差更小，视野更清晰</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">强调"整片清晰"</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px;border-bottom:1px solid #e8daef">个性化定制</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">根据客户的眼睛参数专属设计</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">强调"专属定制"</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">高折射率</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">1.67/1.71/1.74 折射率，同度数镜片更薄</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">强调"更薄更美观"</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px;border-bottom:1px solid #e8daef">高硬度镀膜</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">表面硬度测试通常达到HB或更高</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">强调"耐磨耐用"</td></tr>
      <tr><td style="padding:10px 14px">超级疏水疏油膜</td><td style="padding:10px 14px">镜片表面不易沾灰、指纹，易清洁</td><td style="padding:10px 14px">强调"方便清洁"</td></tr>
    </table>
  </div>

  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">🎯 高端客户画像与接触策略</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <h3 style="color:#8e44ad;font-size:1rem;margin-top:18px">高端消费意愿的信号</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">主动询问"有没有更好的？"</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">职业为医生、律师、设计师、高管等</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">穿着讲究，配件为名牌</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">度数较高（>-4.00D）或有特殊用眼需求</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">之前已配过高端产品，来换镜</li>
    </ul>

    <h3 style="color:#8e44ad;font-size:1rem;margin-top:18px">高端客户的购买决策逻辑</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px">高端客户通常不以价格为核心判断，而是：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">重视"专业建议"——你越专业，他越信任</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">重视"解决方案"——能否解决他的视力问题</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">重视"品牌和背书"——蔡司、依视路等品牌本身就是信任状</li>
    </ul>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 面对高端客户，不要过多讲价格，多讲技术差异和使用体验。他们需要的是"被专业顾问服务"的感觉。
    </div>
  </div>

  <div style="background:linear-gradient(135deg,#f5eef8,#e8daef);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#6c3483">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>高端品牌各有特色，蔡司（个性化定制）、依视路（渐进技术）、豪雅（性价比高）</li>
      <li>三步推介法：痛点→解决方案→体验邀请</li>
      <li>数字和品牌背书是最有说服力的工具</li>
      <li>识别高端消费信号，主动升级推荐，提升客单价</li>
    </ul>
  </div>

"""

# ---- Day_47: 顾客心理 ----
EXTRAS[(BASE7, "Day_47_学习内容.html")] = """  <h2 style="color:#8e44ad;margin-top:32px">🎭 不同性格客户的接待策略</h2>
  <table style="width:100%;border-collapse:collapse;margin:16px 0">
    <tr style="background:#8e44ad;color:#fff"><th style="padding:10px 14px;text-align:left">性格类型</th><th style="padding:10px 14px;text-align:left">识别特征</th><th style="padding:10px 14px;text-align:left">接待策略</th></tr>
    <tr><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">果断型</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">说话直接，时间感强，快速做决定</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">简洁明了，直接给出最佳方案，不绕弯子</td></tr>
    <tr style="background:#fbf6ff"><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">分析型</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">问问题多，喜欢比较，不急于决定</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">提供数据和专业依据，耐心解答，不催促</td></tr>
    <tr><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">社交型</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">健谈，注重关系，易受影响</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">建立关系，分享故事，利用社会证明</td></tr>
    <tr style="background:#fbf6ff"><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">谨慎型</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">犹豫，担心出错，需要安全感</td><td style="padding:10px 14px;border-bottom:1px solid #e8d5f5">强调保障（退换政策、品牌信誉），给出明确承诺</td></tr>
  </table>

  <h2 style="color:#8e44ad;margin-top:32px">📊 门店客流与消费数据分析</h2>
  <div style="background:#f5eaff;border-left:4px solid #8e44ad;padding:14px 18px;margin:16px 0;border-radius:0 8px 8px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:8px">了解门店经营数据，有助于你理解哪些时间段、哪些产品是重点：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>高峰时段</strong>：周末、放学后（15:00-19:00）、节假日——提前做好准备</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>重点客群</strong>：学生（近视镜）、中老年（老花镜）、白领（防蓝光）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>高利润品类</strong>：高端镜片、渐进镜、太阳镜——重点推荐</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>复购周期</strong>：一般客户2-3年换镜，儿童6-12个月复查换镜</li>
    </ul>
  </div>

  <div style="background:linear-gradient(135deg,#f5eaff,#e8d5f5);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#6c3483">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>了解客户决策心理，能帮助你在正确时机说正确的话</li>
      <li>不同性格的客户需要不同的接待策略，灵活调整</li>
      <li>消费心理学工具：锚定、损失厌恶、社会证明，合理运用</li>
      <li>数据分析意识：了解门店经营规律，主动把握机会</li>
    </ul>
  </div>

"""

# ---- Day_48: 营销活动策划 ----
EXTRAS[(BASE7, "Day_48_学习内容.html")] = """  <h2 style="color:#e74c3c;margin-top:32px">📊 活动效果评估指标</h2>
  <div style="background:#fff0ec;border-radius:10px;padding:18px 22px;margin:14px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">活动结束后，需要评估效果以优化下次活动：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#e74c3c;color:#fff"><th style="padding:10px 14px;text-align:left">指标</th><th style="padding:10px 14px;text-align:left">计算方式</th><th style="padding:10px 14px;text-align:left">参考标准</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">客流增长率</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">(活动期客流-平日客流)/平日客流</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">优秀: >30%</td></tr>
      <tr style="background:#fff0ec"><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">活动转化率</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">成单人数/进店人数</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">正常: 20-40%</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">活动ROI</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">(活动销售额-活动成本)/活动成本</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6bc">健康: >3倍</td></tr>
      <tr style="background:#fff0ec"><td style="padding:10px 14px">新客比例</td><td style="padding:10px 14px">活动中新客占比</td><td style="padding:10px 14px">越高越好（说明活动拉新效果）</td></tr>
    </table>
  </div>

  <h2 style="color:#e74c3c;margin-top:32px">📱 社交媒体营销基础</h2>
  <div style="background:#fff0ec;border-radius:10px;padding:18px 22px;margin:14px 0">
    <h3 style="color:#c0392b;margin-top:18px">微信朋友圈内容策划</h3>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>产品知识类</strong>：科普近视、老花、防蓝光等眼科知识，建立专业形象</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>客户故事类</strong>（获客户同意后）：分享成功配镜案例，增强信任</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>活动通知类</strong>：门店促销、限时优惠，配上精美图片</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px"><strong>日常生活类</strong>：适当分享工作状态，增加亲近感</li>
    </ul>
    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:10px 14px;border-radius:0 8px 8px 0;color:#856404;margin:10px 0">
      ⚠️ 朋友圈内容注意：不要每天都是广告，否则会被屏蔽。比例建议：知识科普40%、生活内容30%、产品活动30%。
    </div>
  </div>

  <div style="background:linear-gradient(135deg,#fff0ec,#ffe0d8);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#c0392b">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>营销活动策划要有明确目标和可量化指标</li>
      <li>活动执行前做好准备：物料、话术、人员分工</li>
      <li>活动后必须复盘，总结经验为下次做准备</li>
      <li>社交媒体是低成本高效率的拉新工具，内容要专业+自然</li>
    </ul>
  </div>

"""

# ---- Day_49: 第7周 ----
EXTRAS[(BASE7, "Day_49_学习内容.html")] = """  <h2 style="color:#8e44ad;margin-top:32px">🏅 优秀员工的成长路径</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">在眼镜行业，优秀员工的职业发展通常遵循以下路径：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#8e44ad;color:#fff"><th style="padding:10px 14px;text-align:left">阶段</th><th style="padding:10px 14px;text-align:left">时间节点</th><th style="padding:10px 14px;text-align:left">核心标志</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">新手期</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">入职1-3个月</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">能独立完成基础接待，熟悉产品</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px;border-bottom:1px solid #e8daef">成熟期</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">3-12个月</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">稳定成单，客单价达标，有固定回头客</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #e8daef">专家期</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">1-3年</td><td style="padding:10px 14px;border-bottom:1px solid #e8daef">能处理复杂验光，培带新人，具备管理潜力</td></tr>
      <tr style="background:#f5eef8"><td style="padding:10px 14px">店长/主管</td><td style="padding:10px 14px">3年以上</td><td style="padding:10px 14px">团队管理、门店经营、目标达成</td></tr>
    </table>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 技能提升建议：考取验光员资格证（初级→中级→高级），这是专业晋升的重要加分项。
    </div>
  </div>

  <h2 style="color:#8e44ad;margin-top:32px">🔑 保持竞争力的持续学习方法</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>日常积累</strong>：每天接待中遇到的新问题，记录下来，查找答案</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>同行学习</strong>：关注行业公众号、参加厂商培训，了解新产品新技术</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>客户反馈</strong>：主动征询客户意见，不断优化服务流程</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>复盘习惯</strong>：每周回顾本周成功和失败案例，提炼经验</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>资格认证</strong>：考取验光员职业资格证，证明专业能力</li>
    </ul>
  </div>

  <div style="background:linear-gradient(135deg,#f5eef8,#e8daef);border-radius:10px;padding:20px 24px;margin-top:24px">
    <strong style="color:#6c3483">📝 今日总结</strong>
    <ul style="margin-top:10px;padding-left:18px;line-height:2">
      <li>成为优秀员工是一个持续积累的过程，没有捷径</li>
      <li>专业知识+销售技能+服务意识，三者缺一不可</li>
      <li>保持学习的习惯，行业在变化，知识需要更新</li>
      <li>良好的工作态度和职业操守，是长期发展的根基</li>
    </ul>
  </div>

"""

print("开始处理第7周文件...")
for (base, fn), extra in EXTRAS.items():
    if base != BASE7:
        continue
    fp = os.path.join(base, fn)
    if not os.path.exists(fp):
        print(f"  ⚠️  不存在: {fn}")
        continue
    lines = insert_before_nav(fp, extra)
    print(f"  ✅ {fn}: {lines} 行")

print("\n开始处理第8周文件...")

# ---- 第8周文件的主题 ----
# 先读取标题来确认主题
for fn in ["Day_52_学习内容.html", "Day_53_学习内容.html", "Day_54_学习内容.html"]:
    fp = os.path.join(BASE8, fn)
    if os.path.exists(fp):
        with open(fp, encoding='utf-8') as f:
            first50 = ''.join(f.readlines()[:10])
        print(f"  {fn} 前几行: {first50[:200]}")
