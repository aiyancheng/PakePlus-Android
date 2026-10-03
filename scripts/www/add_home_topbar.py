# -*- coding: utf-8 -*-
"""
为每一页（除首页）在 <body> 之后插入顶部「🏠 返回首页」入口，并注入配套样式。
幂等：以 HOME-BAR 标记判断，重复执行不会重复插入。
"""
import io
import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(ROOT, '_bak_tablet')
SKIP_DIRS = ('.workbuddy', '_bak', '_enrich', '_ima', '_scripts', '__pycache__')

MARK = 'HOME-BAR'

CSS = """
/* ══ HOME-BAR：顶部返回首页入口 ══ */
.home-topbar{background:#fff;padding:10px 0}
.home-topbar .ht-inner{max-width:900px;margin:0 auto;padding:0 30px}
.home-topbar a{display:inline-flex;align-items:center;gap:6px;font-size:.86em;font-weight:700;color:#4a5270;text-decoration:none;background:#f1f3f9;border-radius:20px;padding:7px 18px;transition:background .2s,color .2s,transform .2s}
.home-topbar a:hover{background:#e6eaf6;color:#283593;transform:translateX(-2px)}
@media (min-width:901px) and (max-width:1400px){.home-topbar .ht-inner{max-width:1080px}}
@media (max-width:900px){.home-topbar{padding:8px 0}.home-topbar .ht-inner{max-width:100%;padding:0 14px}.home-topbar a{font-size:.82em;padding:6px 14px}}
"""

BAR = ('<div class="home-topbar"><div class="ht-inner">'
       '<a href="../index.html">\U0001F3E0 返回首页</a></div></div>\n')


def brace_ok(css):
    d = 0
    for ch in css:
        if ch == '{':
            d += 1
        elif ch == '}':
            d -= 1
    return d == 0


def process(path):
    h = io.open(path, encoding='utf-8').read()
    if MARK in h:
        return 'skip'
    if '<body' not in h or '</style>' not in h:
        return 'invalid'

    style_css = CSS.replace('HOME-BAR', MARK)
    if not brace_ok(style_css):
        return 'css_error'

    # 1) 注入样式：放在第一个 </style> 之前
    i = h.index('</style>')
    h2 = h[:i] + style_css + h[i:]

    # 2) 插入顶部条：紧跟 <body ...> 之后
    m = re.search(r'<body[^>]*>', h2)
    if not m:
        return 'invalid'
    h2 = h2[:m.end()] + '\n' + BAR + h2[m.end():]

    # 备份
    os.makedirs(BAK, exist_ok=True)
    rel = os.path.relpath(path, ROOT).replace(os.sep, '__')
    bak = os.path.join(BAK, rel + '.bak_homebar')
    if not os.path.exists(bak):
        shutil.copy2(path, bak)

    io.open(path, 'w', encoding='utf-8').write(h2)
    return 'ok'


def main():
    stats = {'ok': 0, 'skip': 0, 'invalid': 0, 'css_error': 0}
    detail = []
    for root, dirs, fs in os.walk(ROOT):
        if any(s in root for s in SKIP_DIRS):
            continue
        for f in sorted(fs):
            if not f.endswith('.html') or f.startswith('index'):
                continue
            p = os.path.join(root, f)
            r = process(p)
            stats[r] = stats.get(r, 0) + 1
            if r not in ('ok', 'skip'):
                detail.append((r, os.path.relpath(p, ROOT)))
    print('结果:', stats)
    for d in detail:
        print('  !!', d)


if __name__ == '__main__':
    main()
