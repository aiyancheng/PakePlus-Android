import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才\第6周_独立接单训练"

def insert_before_nav(filepath, extra_html):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    # 找到 nav-footer div 的起始位置
    nav_idx = content.rfind('<div class="nav-footer"')
    if nav_idx == -1:
        nav_idx = content.rfind('</div>\n</body>')
    if nav_idx == -1:
        nav_idx = len(content) - 20
    new_content = content[:nav_idx] + extra_html + '\n\n  ' + content[nav_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return new_content.count('\n') + 1

# Day_39 额外内容
EXTRA_39 = """  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🧓 老年人特殊眼病知识</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">眼镜店员工需了解常见老年眼病，以便及时建议客户就医，同时体现专业性：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2980b9;color:#fff"><th style="padding:10px 14px;text-align:left">眼病</th><th style="padding:10px 14px;text-align:left">主要症状</th><th style="padding:10px 14px;text-align:left">处理建议</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">白内障</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">视物模糊、夜间眩光、颜色变黄</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">建议就医，手术后再来配镜</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">青光眼</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">视野缩小、眼压高、头痛</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">立即就医，不可延误</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">老年黄斑变性</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">中心视力下降，直线看起来弯曲</td><td style="padding:10px 14px;border-bottom:1px solid #d0e8f5">就医，防蓝光可作为辅助</td></tr>
      <tr style="background:#eaf4fc"><td style="padding:10px 14px">干眼症</td><td style="padding:10px 14px">眼干、异物感、视力波动</td><td style="padding:10px 14px">建议就医，同时减少屏幕时间</td></tr>
    </table>
    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:10px 14px;border-radius:0 8px 8px 0;color:#856404;margin:10px 0">
      ⚠️ 发现客户视力问题异常，切勿轻易配镜。真诚建议先就医是专业负责的表现，客户会更信任你，反而更可能成为长期顾客。
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🎁 中老年客户的转介绍策略</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">中老年客户口碑传播能力强，圈子粘性高，一个满意的老年客户可以带来5-10个转介绍。</p>
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">自然转介绍话术</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">在服务接近尾声、客户表示满意时：</p>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em"><em>"阿姨，如果您身边有朋友也需要配镜，欢迎带过来，我们一定好好招待！您还可以告诉他们，说是老顾客介绍的，我们会给一个小优惠作为答谢。"</em></p>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">（同时递上名片或二维码）</p>
    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 记住：不要在客户刚进门或服务还没建立信任时就请求转介绍，那会显得功利。在客户满意后自然提出，效果最好。
    </div>
  </div>

"""

# Day_42 额外内容
EXTRA_42 = """  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">🎯 本周最佳实践案例分析</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">案例一：价格异议的成功化解</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">某员工遇到客户说"网上同款便宜500"，成功应对：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">首先认同：<em>"您说得对，网上确实有更便宜的"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">然后区分：<em>"但验光和装配需要专业设备，网上镜片参数不一定准确"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">最后升华：<em>"而且我们提供两年免费调整维护，一副眼镜戴2-3年，总价值其实更划算"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">结果：客户当场成单，选择了更高端的镜片</li>
    </ul>

    <h3 style="color:#2980b9;font-size:1rem;margin-top:18px">案例二：儿童配镜的家长沟通</h3>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">小学生家长对防控镜片价格犹豫，员工的处理：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">拿出数据：<em>"临床研究显示可延缓近视进展60%"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">算账给看：<em>"每年多花500元防控，比将来高度近视去做手术（数万元）划算得多"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">激活情感：<em>"孩子的眼睛是用一辈子的"</em></li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">结果：家长选择防控镜片，并预约了半年后复查</li>
    </ul>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">📚 第7周学习预习清单</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">利用今天周测结束后的时间，预习第7周内容：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">□ 了解高端镜片品牌（蔡司、依视路、豪雅）的产品线和差异</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">□ 思考：如何让客户从普通配镜升级到高端配镜？</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">□ 回顾本周遇到的最困难情况，设想下次如何更好应对</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">□ 整理本周新增客户档案，确保信息完整</li>
    </ul>

    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 每一周的结束，都是下一周成长的起点。完成周测，做好复盘，带着总结进入第7周！
    </div>
  </div>

  <h2 style="color:#1a5276;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #2980b9">💭 成长心态：给自己的一封信</h2>
  <div style="background:#eaf4fc;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #d0e8f5">
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">六周前，你还是一个对眼镜行业一无所知的新人；今天，你已经能够独立接单、处理异议、服务特殊客群。</p>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">在眼镜行业，真正的高手不仅仅是"卖眼镜的人"，而是一个<strong>帮助客户守护视力健康的专业顾问</strong>。</p>
    <p style="line-height:1.8;color:#555;margin-bottom:12px;font-size:0.95em">记住三句话：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">🔑 <strong>专业是底气</strong>——你懂越多，客户越信任你</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">❤️ <strong>真诚是基础</strong>——站在客户角度思考，而不只是完成销售</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px">📈 <strong>坚持是关键</strong>——每天进步一点点，一年后的你会感谢今天的积累</li>
    </ul>
  </div>

"""

fp39 = os.path.join(BASE, "Day_39_学习内容.html")
fp42 = os.path.join(BASE, "Day_42_学习内容.html")

lines39 = insert_before_nav(fp39, EXTRA_39)
lines42 = insert_before_nav(fp42, EXTRA_42)

print(f"Day_39: {lines39} 行")
print(f"Day_42: {lines42} 行")
