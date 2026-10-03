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

# ---- Day_44 补充（第7周，高端产品销售）----
EXTRA_44 = """  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">💼 试戴营销法：让产品自己说话</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">研究表明，让客户试戴高端镜片15分钟，成交率提升60%以上。试戴的关键步骤：</p>
    <ol style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">提前告知差异点："等会您重点感受一下边缘清晰度和整体舒适感"</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">请客户先戴普通款，再换高端款，让对比感更直观</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">试戴时陪同引导："往左看，往右看，再转头看一下远处"</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">试戴结束后主动询问感受，不要沉默</li>
    </ol>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 试戴结束时使用"假设成交法"：<em>"我帮您按这个处方开单，镜框您就选刚才那个吗？"</em>
    </div>
  </div>

  <h2 style="color:#6c3483;font-size:1.15rem;margin-top:32px;padding-left:10px;border-left:4px solid #8e44ad">🛡️ 高端产品服务承诺</h2>
  <div style="background:#f5eef8;border-radius:10px;padding:18px 22px;margin:14px 0;border:1px solid #e8daef">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">高端产品的服务保障是重要的销售理由：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">品牌镜片通常附带1-2年防雾/防划承诺</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">门店配套免费清洗保养服务（每季度一次）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:4px">适应期保障（7-14天内不适可免费调整）</li>
    </ul>
  </div>

"""

# ---- Day_52: 极端情境挑战 ----
EXTRA_52 = """  <h2 style="color:#c0392b;margin-top:32px">📋 极端情境处理复盘表</h2>
  <div style="background:#fef0ef;border-radius:10px;padding:18px 22px;margin:16px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">每次遇到高难度场景后，建议用此表复盘：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#c0392b;color:#fff"><th style="padding:10px 14px;text-align:left">复盘维度</th><th style="padding:10px 14px;text-align:left">自问内容</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">情绪管理</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">我是否在客户激动时保持了冷静？有没有被情绪带跑？</td></tr>
      <tr style="background:#fffafa"><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">倾听质量</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">我有没有真正理解客户的核心诉求？还是只是听了表面？</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">解决方案</td><td style="padding:10px 14px;border-bottom:1px solid #f5c6c6">我提出的方案是否真正解决了客户的问题？</td></tr>
      <tr style="background:#fffafa"><td style="padding:10px 14px">结果</td><td style="padding:10px 14px">客户最终满意吗？下次遇到类似情况应如何改进？</td></tr>
    </table>
    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 每一次高难度情境都是成长的机会。处理得好，客户往往变成最忠实的粉丝；处理得差，才会真正流失。
    </div>
  </div>

  <h2 style="color:#c0392b;margin-top:32px">🎯 极端情境应对心态建设</h2>
  <div style="background:#fef0ef;border-radius:10px;padding:18px 22px;margin:16px 0">
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>换位思考</strong>：想象自己花了几千元买到不满意的眼镜，你会有什么感受？</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>攻击不代表否定</strong>：客户激动是因为失望，而非针对你个人</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>解决问题是第一位</strong>：不是赢得争论，而是让客户满意离开</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:8px"><strong>及时求援</strong>：超出自己权限时，第一时间请示上级，不要拖</li>
    </ul>
  </div>

"""

# ---- Day_53: 综合精讲 ----
EXTRA_53 = """  <h2 style="color:#2c3e50;margin-top:32px">🔗 视光学与销售的内在联系</h2>
  <div style="background:#f0f4f8;border-radius:10px;padding:18px 22px;margin:16px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">优秀的眼镜顾问不是"卖眼镜的"，而是"用专业解决视觉问题的人"：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2c3e50;color:#fff"><th style="padding:10px 14px;text-align:left">视光学知识</th><th style="padding:10px 14px;text-align:left">如何转化为销售能力</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">屈光不正原理</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">向客户解释为什么需要配镜，建立信任</td></tr>
      <tr style="background:#f8f9fa"><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">镜片光学特性</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">用技术差异支撑高端产品的价格</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">儿童视力发育</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">对家长的专业建议，促成防控产品销售</td></tr>
      <tr style="background:#f8f9fa"><td style="padding:10px 14px">老视机理</td><td style="padding:10px 14px">渐进镜推荐的专业依据</td></tr>
    </table>
    <div style="background:#d1ecf1;border-left:4px solid #17a2b8;padding:10px 14px;border-radius:0 8px 8px 0;color:#0c5460;margin:10px 0">
      💡 每学一个新的视光知识，都问自己："这个知识如何帮助我更好地服务客户、解决他们的视力问题？"
    </div>
  </div>

  <h2 style="color:#2c3e50;margin-top:32px">📝 结业前综合能力自检</h2>
  <div style="background:#f0f4f8;border-radius:10px;padding:18px 22px;margin:16px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">在结业考核前，请诚实自评以下能力：</p>
    <ul style="padding-left:20px;margin-bottom:14px">
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能向客户解释近视、远视、散光、老视的成因</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能独立完成主觉验光7步流程</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能按需推荐合适的镜片类型（折射率、功能）</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能应对常见的价格异议，不轻易降价</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能服务儿童和中老年特殊客群</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 能主动尝试交叉销售并有成功案例</li>
      <li style="line-height:1.8;color:#555;font-size:0.95em;margin-bottom:6px">□ 已建立10名以上客户的跟进档案</li>
    </ul>
    <div style="background:#d4edda;border-left:4px solid #28a745;padding:10px 14px;border-radius:0 8px 8px 0;color:#155724;margin:10px 0">
      ✅ 对不确定的项目，今天就找师傅再请教一遍，不留遗憾进入结业考核。
    </div>
  </div>

"""

# ---- Day_54: 结业前准备 ----
EXTRA_54 = """  <h2 style="color:#2c3e50;margin-top:32px">🎓 结业考核准备清单</h2>
  <div style="background:#f0f4f8;border-radius:10px;padding:18px 22px;margin:16px 0">
    <p style="line-height:1.8;color:#555;margin-bottom:12px">考核前最后确认，确保万无一失：</p>
    <table style="width:100%;border-collapse:collapse;margin:14px 0">
      <tr style="background:#2c3e50;color:#fff"><th style="padding:10px 14px;text-align:left">考核内容</th><th style="padding:10px 14px;text-align:left">准备要点</th><th style="padding:10px 14px;text-align:left">状态</th></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">理论笔试</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">复习光学基础、产品知识、制度规范</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">□ 已准备</td></tr>
      <tr style="background:#f8f9fa"><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">实操验光</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">7步主觉验光熟练度，记录规范</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">□ 已准备</td></tr>
      <tr><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">模拟接待</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">完整接待流程、异议处理话术</td><td style="padding:10px 14px;border-bottom:1px solid #dce1e7">□ 已准备</td></tr>
      <tr style="background:#f8f9fa"><td style="padding:10px 14px">综合答辩</td><td style="padding:10px 14px">8周学习总结，成长反思，未来计划</td><td style="padding:10px 14px">□ 已准备</td></tr>
    </table>
  </div>

  <h2 style="color:#2c3e50;margin-top:32px">💫 写给即将结业的自己</h2>
  <div style="background:linear-gradient(135deg,#2c3e50,#1a252f);color:#fff;border-radius:10px;padding:24px;margin:16px 0">
    <p style="line-height:1.9;margin-bottom:12px;opacity:.95">八周前，你还是一个对眼镜行业陌生的新人。</p>
    <p style="line-height:1.9;margin-bottom:12px;opacity:.95">今天，你已经掌握了眼睛的结构原理、主觉验光技能、各类镜片的特性与推荐逻辑、销售话术与异议处理、特殊客群的服务方法……</p>
    <p style="line-height:1.9;margin-bottom:16px;opacity:.95">这不是终点，而是一个新起点。</p>
    <ul style="padding-left:20px;margin-bottom:12px;line-height:2;opacity:.9">
      <li>你的眼镜，帮助客户看清世界——这份工作有意义</li>
      <li>你的专业，帮助客户做出正确选择——这份价值真实</li>
      <li>你的服务，让客户感到被关怀——这份影响持久</li>
    </ul>
    <p style="opacity:.85;font-size:.95rem">带着这八周积累的知识和技能，在每一次接待中继续成长。</p>
  </div>

"""

results = {}

# Day_44
fp44 = os.path.join(BASE7, "Day_44_学习内容.html")
results["Day_44"] = insert_before_nav(fp44, EXTRA_44)

# 第8周三个文件
files8 = {
    "Day_52_学习内容.html": EXTRA_52,
    "Day_53_学习内容.html": EXTRA_53,
    "Day_54_学习内容.html": EXTRA_54,
}
for fn, extra in files8.items():
    fp = os.path.join(BASE8, fn)
    results[fn.replace("_学习内容.html","")] = insert_before_nav(fp, extra)

for k, v in results.items():
    status = "✅" if v >= 200 else "⚠️ "
    print(f"{status} {k}: {v} 行")
