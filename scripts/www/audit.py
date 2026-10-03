# -*- coding: utf-8 -*-
"""全项目体检：结构 / 链接 / 重复 id / 交互 / 模块完整性。只读，不改文件。"""
import io, os, re, sys, json
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

ROOT = '.'
SKIP_DIR = ('.workbuddy', '_bak', '_enrich', '_ima', '_bak_tablet')

files = []
for root, dirs, fs in sorted(os.walk(ROOT)):
    if any(s in root for s in SKIP_DIR):
        continue
    for f in sorted(fs):
        if f.endswith('.html'):
            files.append(os.path.join(root, f).replace('\\', '/'))

print('HTML 文件数:', len(files))
print()

problems = {}

def add(p, kind, detail):
    problems.setdefault(kind, []).append((p, detail))

PAIR_TAGS = ['div', 'ul', 'ol', 'table', 'tr', 'td', 'th', 'li', 'p', 'span', 'section', 'details', 'h2', 'h3']

for p in files:
    h = io.open(p, encoding='utf-8').read()
    body = h[h.find('<body'):] if '<body' in h else h

    # 1) style / script 配对
    if h.count('<style>') != h.count('</style>'):
        add(p, 'style标签不配对', '%d/%d' % (h.count('<style>'), h.count('</style>')))
    if h.count('<script>') != h.count('</script>'):
        add(p, 'script标签不配对', '%d/%d' % (h.count('<script>'), h.count('</script>')))

    # 2) 常见标签配对（忽略自闭合）
    for t in PAIR_TAGS:
        o = len(re.findall(r'<%s\b[^>]*?(?<!/)>' % t, body, re.I))
        c = len(re.findall(r'</%s\s*>' % t, body, re.I))
        if o != c:
            add(p, '标签不配对:%s' % t, '%d/%d' % (o, c))

    # 3) 重复 id
    ids = re.findall(r'\bid="([^"]+)"', h)
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        add(p, '重复id', ','.join(dup[:6]))

    # 4) 链接有效性
    links = re.findall(r'(?:href|src)="([^"#:]+\.html)(?:#[^"]*)?"', h)
    for lk in set(links):
        tgt = os.path.normpath(os.path.join(os.path.dirname(p), lk)).replace('\\', '/')
        if not os.path.exists(tgt):
            add(p, '死链', lk)

    # 5) 学习内容：LM 模块
    if p.endswith('学习内容.html'):
        need = ['lm-goal', 'lm-quiz']
        for k in need:
            if k not in h:
                add(p, '缺学习模块', k)

    # 6) 练习题：可点击选项
    if p.endswith('练习题.html'):
        if 'options' not in h and 'choiceQuestions' not in h and 'opt' not in h:
            add(p, '练习题无可点击选项', '')

    # 7) 表格结构
    for tb in re.findall(r'<table\b.*?</table>', body, re.S):
        if '<th' in tb and '</th>' not in tb:
            add(p, '表头标签异常', tb[:60])
        if tb.count('<thead') != tb.count('</thead>') or tb.count('<tbody') != tb.count('</tbody>'):
            add(p, '表格结构异常', tb[:60])

print('=== 问题汇总 ===')
if not problems:
    print('无问题')
for k, v in sorted(problems.items(), key=lambda x: -len(x[1])):
    print()
    print('【%s】%d 处' % (k, len(v)))
    seen = set()
    shown = 0
    for p, d in v:
        key = (p, d)
        if key in seen:
            continue
        seen.add(key)
        print('   ', p, '|', d)
        shown += 1
        if shown >= 25:
            print('    ...(其余省略)')
            break
json.dump({k: [list(x) for x in v] for k, v in problems.items()},
          io.open('_audit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
