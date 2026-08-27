# -*- coding: utf-8 -*-
"""三年级数学练习题渲染器：读取 data_up.py / data_down.py 生成10份HTML练习卷"""
import os, sys

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>三年级数学 __TITLE__</title>
<style>
:root{--primary:#1677ff;--primary-light:#e6f0ff;--primary-dark:#0958d9;--ok:#52c41a;--warn:#fa8c16;--text:#1f2329;--text2:#4e5969;--line:#e5e6eb;--bg:#f7f8fa;--card:#fff}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB","Heiti SC","WenQuanYi Micro Hei",-apple-system,system-ui,SimHei,serif,sans-serif;background:var(--bg);color:var(--text);line-height:1.9;font-size:15px}
.wrap{max-width:860px;margin:0 auto;padding:20px 16px 60px}
header.paper{background:var(--card);border:1px solid var(--line);border-top:5px solid var(--primary);border-radius:12px;padding:24px 26px;margin-bottom:18px}
header.paper .sub{font-size:12.5px;color:var(--text2);letter-spacing:2px;margin-bottom:4px}
header.paper h1{font-size:22px;color:var(--primary-dark)}
header.paper .meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;font-size:13px}
header.paper .meta span{background:var(--primary-light);color:var(--primary-dark);padding:2px 12px;border-radius:99px}
header.paper .scope{margin-top:12px;font-size:13.5px;color:var(--text2);background:var(--bg);padding:10px 14px;border-left:3px solid var(--primary);border-radius:0 8px 8px 0}
section.block{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 22px;margin-bottom:18px}
h2.qsec{font-size:16px;color:var(--primary-dark);border-bottom:2px solid var(--primary-light);padding-bottom:8px;margin-bottom:6px}
h2.qsec small{font-weight:normal;color:var(--text2);font-size:12.5px;margin-left:8px}
ol.qlist{list-style:none;counter-reset:q}
ol.qlist>li{counter-increment:q;padding:8px 0 8px 34px;position:relative;border-bottom:1px dashed var(--line)}
ol.qlist>li:last-child{border-bottom:none}
ol.qlist>li::before{content:counter(q) ".";position:absolute;left:4px;color:var(--primary);font-weight:bold}
.blank{display:inline-block;min-width:56px;border-bottom:1.5px solid var(--text2);text-align:center;color:transparent}
input.fillin{display:inline-block;min-width:60px;border:none;border-bottom:1.5px solid #b9c0cc;text-align:center;font-size:15px;background:#fbfcfe;color:var(--primary-dark);outline:none;font-family:inherit}
input.fillin:focus{border-bottom-color:var(--primary);background:var(--primary-light)}
.opts{display:block;margin-top:2px}
.answer{margin-top:22px}
details.ans{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
details.ans summary{cursor:pointer;padding:13px 22px;font-size:15px;font-weight:bold;color:var(--ok);background:#f6ffed;border:1px solid #d9f7be;border-radius:12px;user-select:none;list-style:none;display:flex;align-items:center;gap:8px}
details.ans summary::before{content:"▸";transition:.2s}
details.ans[open] summary::before{transform:rotate(90deg)}
details.ans .ans-body{padding:14px 22px 20px}
table.mini{width:100%;border-collapse:collapse;font-size:13.5px;margin:8px 0}
table.mini th{background:var(--primary-light);color:var(--primary-dark);padding:6px 10px;border:1px solid #d4e3ff}
table.mini td{padding:6px 10px;border:1px solid var(--line);vertical-align:top}
table.mini td:first-child{white-space:nowrap;color:var(--primary-dark);font-weight:bold}
footer{margin-top:26px;text-align:center;color:var(--text2);font-size:12.5px}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:0 30px}
@media(max-width:640px){.twocol{grid-template-columns:1fr}}
.hint{font-size:12.5px;color:var(--warn);margin-top:4px}
</style>
</head>
<body>
<div class="wrap">
<header class="paper">
  <div class="sub">人教版小学数学三年级 · 专项练习</div>
  <h1>__TITLE__</h1>
  <div class="meta"><span>建议用时 __TIME__</span><span>满分 __FULL__</span><span>共 __COUNT__ 题</span></div>
  <div class="scope"><b>考点范围：</b>__SCOPE__</div>
</header>
<section class="block notice">
  <h2 class="qsec">答题须知<small>先读一遍再动笔</small></h2>
  <ol class="qlist">
    <li>先写姓名和日期，按题目顺序作答；遇到暂时不会的题先跳过，做完再回头思考。</li>
    <li>口算题不写过程，直接写得数；竖式题要列竖式，带※的题必须写出验算过程。</li>
    <li>填空题按空作答，注意单位名称是否要求填写；判断题打√或×，选择题填字母序号。</li>
    <li>解决问题要写出算式、得数和单位（或答句），只写得数要扣过程分。</li>
    <li>做完后预留5分钟检查：数字有没有抄错、单位有没有漏写、验算了没有。</li>
  </ol>
  <p class="hint">评分参考：填空每空1分；判断、选择每题2分；口算每题1分；竖式每题4分（验算占1分）；解决问题每题6分（列式3分＋计算2分＋单位答句1分）。错题请回到《三年级数学知识点与考点总览》对应单元查漏补缺。</p>
</section>
__BODY__
<div class="answer">
<details class="ans">
  <summary>参考答案与部分解析（点击展开 / 收起）</summary>
  <div class="ans-body">__ANSWERS__
  <p class="hint">答案核对规则：全对说明该考点已掌握；错1～3题标记\"待巩固\"，重做错题；错4题以上回到总览文档对应单元，先复习知识点再做本卷。</p>
  </div>
</details>
</div>
<footer>人教版三年级数学专项练习 · 闫胜君整理 · 建议先限时完成再核对答案，错题对照《知识点与考点总览》标注薄弱单元</footer>
</div>
</body>
</html>"""

SEC_TITLES = {
    "fill": ("一、填空题", "每空1分"),
    "judge": ("二、判断题", "对的打√，错的打×"),
    "choice": ("三、选择题", "把正确答案的序号填在括号里"),
    "oral": ("四、口算题", "直接写得数"),
    "vertical": ("五、__VCALC__", "要求 __VNOTE__"),
    "solve": ("六、解决问题", "写出必要的过程"),
}

def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def render_fill(items):
    rows = "\n".join(f'<li>{esc(t)}</li>' for t, _ in items)
    ans_rows = "\n".join(
        f'<tr><td>{i+1}</td><td>{esc(a)}</td></tr>' for i, (_, a) in enumerate(items)
    )
    return (
        f'<section class="block"><h2 class="qsec">{SEC_TITLES["fill"][0]}<small>{SEC_TITLES["fill"][1]}</small></h2><ol class="qlist">\n{rows}\n</ol></section>',
        f'<table class="mini">\n<tr><th style="width:52px">题号</th><th>答案</th></tr>\n{ans_rows}\n</table>',
    )

def render_judge(items):
    rows = "\n".join(f'<li>{esc(t)}（&nbsp;&nbsp;&nbsp;&nbsp;）</li>' for t, _, _ in items)
    ans_rows = "\n".join(
        f'<tr><td>{i+1}</td><td><b>{("√" if a else "×")}</b>　{esc(w)}</td></tr>'
        for i, (_, a, w) in enumerate(items)
    )
    return (
        f'<section class="block"><h2 class="qsec">{SEC_TITLES["judge"][0]}<small>{SEC_TITLES["judge"][1]}</small></h2><ol class="qlist">\n{rows}\n</ol></section>',
        f'<table class="mini">\n<tr><th style="width:52px">题号</th><th>答案与理由</th></tr>\n{ans_rows}\n</table>',
    )

def render_choice(items):
    rows = []
    for t, opts, _, _ in items:
        opt_html = "\n".join(
            f'<span class="opts">{chr(65+j)}．{esc(o)}</span>' for j, o in enumerate(opts)
        )
        rows.append(f"<li>{esc(t)}（&nbsp;&nbsp;&nbsp;&nbsp;）\n{opt_html}</li>")
    ans_rows = "\n".join(
        f'<tr><td>{i+1}</td><td><b>{chr(65+ans)}</b>　{esc(w)}</td></tr>'
        for i, (_, _, ans, w) in enumerate(items)
    )
    return (
        f'<section class="block"><h2 class="qsec">{SEC_TITLES["choice"][0]}<small>{SEC_TITLES["choice"][1]}</small></h2><ol class="qlist">\n{"".join(rows)}\n</ol></section>',
        f'<table class="mini">\n<tr><th style="width:52px">题号</th><th>答案与理由</th></tr>\n{ans_rows}\n</table>',
    )

def render_oral(items):
    cells = "\n".join(
        f'<li>{esc(t)}＝<span class="blank">　</span></li>' for t, _ in items
    )
    ans_cells = "\n".join(
        f'<tr><td>{esc(t)}</td><td><b>{esc(a)}</b></td></tr>' for t, a in items
    )
    return (
        f'<section class="block"><h2 class="qsec">{SEC_TITLES["oral"][0]}<small>{SEC_TITLES["oral"][1]}</small></h2><ol class="qlist twocol">\n{cells}\n</ol></section>',
        f'<table class="mini">\n<tr><th>算式</th><th>答案</th></tr>\n{ans_cells}\n</table>',
    )

def render_vertical(items, label, note):
    rows = "\n".join(f'<li>{esc(t)}</li>' for t, _, _ in items)
    ans_rows = "\n".join(
        f'<tr><td>{esc(t)}</td><td><b>{esc(a)}</b>{("　" + esc(w)) if w else ""}</td></tr>'
        for t, a, w in items
    )
    title = SEC_TITLES["vertical"][0].replace("__VCALC__", label)
    return (
        f'<section class="block"><h2 class="qsec">{title}<small>要求：{note}</small></h2><ol class="qlist twocol">\n{rows}\n</ol></section>',
        f'<table class="mini">\n<tr><th>题目</th><th>答案</th></tr>\n{ans_rows}\n</table>',
    )

def render_solve(items):
    rows = "\n".join(f'<li>{esc(t)}</li>' for t, _, _ in items)
    ans_rows = "\n".join(
        f'<tr><td>{i+1}</td><td>{esc(a)}</td></tr>' for i, (_, a, _) in enumerate(items)
    )
    return (
        f'<section class="block"><h2 class="qsec">{SEC_TITLES["solve"][0]}<small>{SEC_TITLES["solve"][1]}</small></h2><ol class="qlist">\n{rows}\n</ol></section>',
        f'<table class="mini">\n<tr><th style="width:52px">题号</th><th>答案与过程</th></tr>\n{ans_rows}\n</table>',
    )

def build(ex, outdir):
    body_parts, ans_parts = [], []
    b, a = render_fill(ex["fill"]); body_parts.append(b); ans_parts.append(("<b>一、填空题</b>", a))
    b, a = render_judge(ex["judge"]); body_parts.append(b); ans_parts.append(("<b>二、判断题</b>", a))
    b, a = render_choice(ex["choice"]); body_parts.append(b); ans_parts.append(("<b>三、选择题</b>", a))
    b, a = render_oral(ex["oral"]); body_parts.append(b); ans_parts.append(("<b>四、口算题</b>", a))
    b, a = render_vertical(ex["vertical"], ex.get("vlabel", "竖式计算"), ex.get("vnote", "列竖式计算，带※的要验算")); body_parts.append(b); ans_parts.append(("<b>五、" + ex.get("vlabel", "竖式计算") + "</b>", a))
    b, a = render_solve(ex["solve"]); body_parts.append(b); ans_parts.append(("<b>六、解决问题</b>", a))
    count = len(ex["fill"]) + len(ex["judge"]) + len(ex["choice"]) + len(ex["oral"]) + len(ex["vertical"]) + len(ex["solve"])
    answers = "\n".join(f'<div class="ans-sec">{h}\n{t}\n</div>' for h, t in ans_parts)
    html = (TPL.replace("__TITLE__", ex["title"])
               .replace("__TIME__", ex.get("time", "35分钟"))
               .replace("__FULL__", ex.get("full", "100分"))
               .replace("__COUNT__", str(count))
               .replace("__SCOPE__", ex["scope"])
               .replace("__BODY__", "\n".join(body_parts))
               .replace("__ANSWERS__", answers))
    path = os.path.join(outdir, ex["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    lines = html.count("\n") + 1
    print(f'[OK] {ex["file"]}  题目 {count} 题 / {lines} 行 / {os.path.getsize(path)//1024} KB')
    return count

def main():
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, outdir)
    from data_up import EXERCISES_UP
    from data_down import EXERCISES_DOWN
    total = 0
    for ex in EXERCISES_UP + EXERCISES_DOWN:
        total += build(ex, outdir)
    print(f"\n共生成 {len(EXERCISES_UP) + len(EXERCISES_DOWN)} 份练习，合计 {total} 题")

if __name__ == "__main__":
    main()
