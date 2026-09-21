# -*- coding: utf-8 -*-
"""页面模板：CSS / 结构 / 自测交互 JS"""

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --primary:#1d4ed8;--primary-d:#1e3a8a;--soft:#eff6ff;--soft2:#dbeafe;
  --accent:#ea580c;--accent-soft:#fff7ed;
  --ink:#1f2937;--muted:#6b7280;--line:#e5e7eb;--bg:#f5f7fb;--card:#ffffff;
  --ok:#15803d;--bad:#dc2626;--okbg:#f0fdf4;--badbg:#fef2f2;
  --radius:14px;
}
html{scroll-behavior:smooth}
body{
  font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif;
  background:var(--bg);color:var(--ink);line-height:1.85;font-size:16px;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1000px;margin:0 auto;padding:0 20px 60px}

/* ---------- 顶部 ---------- */
.hero{
  background:linear-gradient(125deg,#1e3a8a 0%,#1d4ed8 55%,#2563eb 100%);
  color:#fff;padding:34px 0 30px;position:relative;overflow:hidden;
}
.hero::after{
  content:"";position:absolute;right:-70px;top:-70px;width:260px;height:260px;
  border-radius:50%;background:rgba(255,255,255,.07);
}
.hero-in{max-width:1000px;margin:0 auto;padding:0 20px;position:relative;z-index:2}
.crumb{font-size:13px;opacity:.82;margin-bottom:10px}
.crumb a{color:#fff;text-decoration:none;opacity:.9}
.crumb a:hover{text-decoration:underline}
.badge-line{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
.badge{
  display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.3);
  color:#fff;font-size:13px;padding:4px 13px;border-radius:999px;letter-spacing:.5px;
}
.badge.gold{background:#f59e0b;border-color:#fbbf24;color:#7c2d12;font-weight:700}
h1.title{font-size:29px;line-height:1.35;font-weight:800;letter-spacing:.5px}
.motto{margin-top:12px;font-size:16.5px;background:rgba(255,255,255,.14);
  border-left:4px solid #fbbf24;padding:10px 16px;border-radius:0 10px 10px 0;line-height:1.7}
.hero-meta{margin-top:14px;font-size:13.5px;opacity:.85}

/* ---------- 卡片 ---------- */
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);
  padding:24px 26px;margin-bottom:22px;box-shadow:0 1px 2px rgba(15,23,42,.04)}
h2.sec{font-size:20px;font-weight:800;color:var(--primary-d);display:flex;align-items:center;
  gap:10px;padding-bottom:12px;margin-bottom:16px;border-bottom:2px solid var(--soft2)}
h2.sec .n{background:var(--primary);color:#fff;width:30px;height:30px;border-radius:9px;
  display:inline-flex;align-items:center;justify-content:center;font-size:15px;flex:none}
h3.sub{font-size:16.5px;font-weight:700;color:var(--primary-d);margin:18px 0 8px;
  padding-left:11px;border-left:4px solid var(--primary)}
p{margin-bottom:11px}
p.tight{margin-bottom:7px}
ul.dot,ol.num{margin:6px 0 12px 0;padding-left:22px}
ul.dot li,ol.num li{margin-bottom:7px}
b,strong{color:var(--primary-d)}
.hl{background:linear-gradient(transparent 62%,#fde68a 62%);font-weight:700;padding:0 1px}
.mono{font-family:Consolas,"Courier New",monospace;background:var(--soft);color:var(--primary-d);
  padding:1px 6px;border-radius:5px;font-size:15px}

/* ---------- 引子 ---------- */
.hook{background:var(--accent-soft);border:1px dashed #fdba74;border-radius:12px;padding:16px 20px;margin-bottom:20px}
.hook .t{font-weight:800;color:var(--accent);margin-bottom:6px;font-size:15.5px}

/* ---------- 公式 / 结论 ---------- */
.formula{background:var(--soft);border:1px solid var(--soft2);border-left:5px solid var(--primary);
  border-radius:10px;padding:16px 20px;margin:12px 0}
.formula .row{display:flex;gap:12px;padding:7px 0;border-bottom:1px dashed #c7d7fb;align-items:baseline}
.formula .row:last-child{border-bottom:none}
.formula .k{flex:none;width:132px;font-weight:800;color:var(--primary-d);font-size:15px}
.formula .v{flex:1;font-size:15.5px}
.grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.mini{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:14px 16px}
.mini h4{font-size:15px;color:var(--primary-d);margin-bottom:6px;font-weight:800}
.mini p{font-size:14.5px;color:#374151;margin-bottom:0}

/* ---------- 图 ---------- */
figure{margin:16px 0 6px;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center}
figure svg{max-width:100%}
figcaption{font-size:13.5px;color:var(--muted);margin-top:9px;line-height:1.6}

/* ---------- 例题 ---------- */
.ex{border:1px solid var(--line);border-radius:12px;margin-bottom:14px;overflow:hidden;background:#fff}
.ex-q{background:#f8fafc;padding:14px 18px;font-size:15.5px;border-bottom:1px solid var(--line)}
.ex-q .tag{display:inline-block;background:var(--primary);color:#fff;font-size:12.5px;
  padding:2px 9px;border-radius:6px;margin-right:9px;font-weight:700;vertical-align:2px}
.ex-q .tag.g{background:var(--accent)}
details.sol{border-top:1px dashed var(--line)}
details.sol summary{cursor:pointer;padding:11px 18px;font-size:14.5px;color:var(--primary);
  font-weight:700;user-select:none;background:#fcfdff;list-style:none}
details.sol summary::-webkit-details-marker{display:none}
details.sol summary::before{content:"▸ ";display:inline-block;transition:.2s}
details.sol[open] summary::before{transform:rotate(90deg)}
details.sol[open] summary{border-bottom:1px dashed var(--line)}
.sol-body{padding:14px 20px 16px;font-size:15.2px;background:#fff}
.sol-body ol{padding-left:20px}
.sol-body li{margin-bottom:8px}
.ansbox{margin-top:12px;background:var(--okbg);border:1px solid #bbf7d0;color:#166534;
  padding:10px 15px;border-radius:9px;font-weight:700;font-size:15px}

/* ---------- 陷阱 ---------- */
.pit{background:var(--badbg);border:1px solid #fecaca;border-radius:12px;padding:16px 20px}
.pit h4{color:var(--bad);font-size:15.5px;margin-bottom:8px;font-weight:800}
.pit li{color:#7f1d1d;font-size:15px}

/* ---------- 生活 / 小结 ---------- */
.life{background:#f0fdfa;border:1px solid #99f6e4;border-radius:12px;padding:16px 20px}
.life h4{color:#0f766e;font-size:15.5px;margin-bottom:8px;font-weight:800}
.sum{background:linear-gradient(120deg,#eff6ff,#f5f3ff);border:1px solid var(--soft2);border-radius:12px;padding:16px 20px}
.sum h4{color:var(--primary-d);font-size:15.5px;margin-bottom:8px;font-weight:800}
.sum li{margin-bottom:6px}
.verse{background:#111827;color:#fef3c7;border-radius:12px;padding:18px 22px;text-align:center;
  font-size:17px;font-weight:700;letter-spacing:1px;line-height:1.9}

/* ---------- 自测 ---------- */
#quiz .q-item{border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:14px;background:#fff}
.q-title{font-size:15.5px;font-weight:600;margin-bottom:11px;line-height:1.75}
.q-no{display:inline-block;background:var(--soft2);color:var(--primary-d);font-size:12.5px;
  padding:2px 9px;border-radius:6px;margin-right:8px;font-weight:800}
.q-options{list-style:none}
.q-opt{display:flex;gap:10px;align-items:flex-start;padding:9px 12px;margin-bottom:7px;
  border:1px solid var(--line);border-radius:9px;cursor:pointer;transition:.15s;font-size:15px;background:#fff}
.q-opt:hover{border-color:var(--primary);background:var(--soft)}
.q-key{flex:none;width:23px;height:23px;line-height:21px;text-align:center;border:1px solid var(--line);
  border-radius:6px;font-size:13px;font-weight:700;color:var(--muted)}
.q-opt.right{border-color:#16a34a;background:var(--okbg)}
.q-opt.right .q-key{background:#16a34a;color:#fff;border-color:#16a34a}
.q-opt.wrong{border-color:#dc2626;background:var(--badbg)}
.q-opt.wrong .q-key{background:#dc2626;color:#fff;border-color:#dc2626}
.q-opt.locked{cursor:default}
.q-opt.locked:hover{border-color:var(--line);background:#fff}
.q-opt.locked.right:hover{border-color:#16a34a;background:var(--okbg)}
.q-opt.locked.wrong:hover{border-color:#dc2626;background:var(--badbg)}
.q-explain{display:none;margin-top:10px;padding:12px 15px;border-radius:9px;font-size:14.5px;line-height:1.8}
.q-explain.show{display:block}
.q-explain.ok{background:var(--okbg);border:1px solid #bbf7d0;color:#166534}
.q-explain.bad{background:var(--badbg);border:1px solid #fecaca;color:#7f1d1d}

/* ---------- 导航 ---------- */
.nav{display:flex;gap:12px;justify-content:space-between;margin:26px 0 8px;flex-wrap:wrap}
.nav a{flex:1;min-width:150px;text-align:center;background:#fff;border:1px solid var(--line);
  border-radius:11px;padding:13px 16px;text-decoration:none;color:var(--ink);font-size:14.5px;
  box-shadow:0 1px 2px rgba(15,23,42,.04);transition:.15s}
.nav a:hover{border-color:var(--primary);color:var(--primary);transform:translateY(-1px)}
.nav a.home{flex:none;min-width:120px;font-weight:700;color:var(--primary);border-color:var(--soft2);background:var(--soft)}
.nav a span{display:block;font-size:12.5px;color:var(--muted);margin-top:2px}
footer{text-align:center;color:var(--muted);font-size:13px;padding:26px 0 0;border-top:1px solid var(--line);margin-top:26px}

/* ---------- 目录页 ---------- */
.lead{font-size:15.5px;color:#374151;margin-bottom:6px}
.group{margin:26px 0 10px;font-size:18px;font-weight:800;color:var(--primary-d);
  display:flex;align-items:center;gap:10px}
.group::after{content:"";flex:1;height:2px;background:var(--soft2)}
.g-desc{font-size:14px;color:var(--muted);margin:2px 0 14px}
.lessons{display:grid;grid-template-columns:repeat(2,1fr);gap:13px}
.lesson{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;
  padding:15px 17px;text-decoration:none;color:var(--ink);transition:.15s;position:relative;overflow:hidden}
.lesson::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--primary)}
.lesson:hover{border-color:var(--primary);transform:translateY(-2px);box-shadow:0 6px 16px rgba(29,78,216,.1)}
.lesson .no{font-size:12.5px;color:var(--primary);font-weight:800;letter-spacing:.5px}
.lesson .nm{font-size:16.5px;font-weight:800;color:var(--primary-d);margin:3px 0 5px}
.lesson .mo{font-size:13.8px;color:var(--muted);line-height:1.65}
table.tb{width:100%;border-collapse:collapse;font-size:14.8px;margin:10px 0}
table.tb th,table.tb td{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}
table.tb th{background:var(--soft);color:var(--primary-d);font-weight:800;text-align:center}
table.tb td.c{text-align:center}
table.tb tr:nth-child(even) td{background:#fbfcfe}
.stat{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:8px 0 4px}
.stat div{background:var(--soft);border:1px solid var(--soft2);border-radius:11px;padding:13px;text-align:center}
.stat b{display:block;font-size:22px;color:var(--primary-d);line-height:1.3}
.stat span{font-size:13px;color:var(--muted)}

@media(max-width:900px){
  .lessons{grid-template-columns:1fr}
  .grid2,.grid3{grid-template-columns:1fr}
  .stat{grid-template-columns:repeat(2,1fr)}
  h1.title{font-size:24px}
  .formula .k{width:100px}
}
@media print{
  body{background:#fff}
  .hero{background:#1e3a8a!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  details.sol{display:block}
  details.sol summary{display:none}
  .card{break-inside:avoid;box-shadow:none}
}
"""

JS = """
const choiceQuestions = __QUESTIONS__;

function initChoiceQuestions(){
  const box = document.getElementById('quiz');
  if(!box) return;
  let html = '';
  for(let i=0;i<choiceQuestions.length;i++){
    const q = choiceQuestions[i];
    html += '<div class="q-item" id="q'+i+'">';
    html += '<div class="q-title"><span class="q-no">自测 '+(i+1)+'</span>'+q.q+'</div>';
    html += '<ul class="q-options">';
    for(let j=0;j<q.options.length;j++){
      html += '<li class="q-opt" onclick="toggleOption('+i+','+j+')">'
           +  '<span class="q-key">'+'ABCD'[j]+'</span><span>'+q.options[j]+'</span></li>';
    }
    html += '</ul><div class="q-explain" id="e'+i+'"></div></div>';
  }
  box.innerHTML = html;
}

function toggleOption(qi, oi){
  const q = choiceQuestions[qi];
  const opts = document.querySelectorAll('#q'+qi+' .q-opt');
  const right = (oi === q.answer);
  for(let j=0;j<opts.length;j++){
    opts[j].classList.add('locked');
    if(j === q.answer) opts[j].classList.add('right');
    if(j === oi && !right) opts[j].classList.add('wrong');
  }
  const box = document.getElementById('e'+qi);
  box.className = 'q-explain show ' + (right ? 'ok' : 'bad');
  box.innerHTML = (right ? '✅ 回答正确！' : '❌ 正确答案：' + 'ABCD'[q.answer])
                + '<br>' + q.explain;
}

document.addEventListener('DOMContentLoaded', initChoiceQuestions);
"""


def page(title, hero, body, questions=None, extra_head=""):
    """组装整页"""
    if questions:
        js = JS.replace("__QUESTIONS__", questions)
        script = '<script>\n' + js + '\n</script>'
    else:
        script = ''
    return (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>' + title + '</title>\n'
        '<style>' + CSS + '</style>\n' + extra_head +
        '</head>\n<body>\n' + hero + '\n' + body + '\n' + script +
        '\n</body>\n</html>\n'
    )
