# -*- coding: utf-8 -*-
"""导出待修复文件的练习题题干/答案/解析"""
import re, sys

files = ['day099.html', 'day101.html', 'day102.html', 'day103.html', 'day104.html']
for f in files:
    s = open(f, encoding='utf-8').read()
    title = re.search(r'<h1 class="page-title">(.*?)</h1>', s, re.S)
    print('=' * 70)
    print(f, '|', title.group(1).strip() if title else '')
    qs = re.findall(r'<div class="question-text">(.*?)</div>', s, re.S)
    metas = re.findall(r'<div class="question-meta">(.*?)</div>', s, re.S)
    for i, q in enumerate(qs):
        print(f'  Q{i+1}: {q.strip()}   [{metas[i].strip() if i < len(metas) else ""}]')
    blocks = re.findall(r'\{\s*type:\s*[\'"](single|multi)[\'"],\s*options:\s*\[(.*?)\],\s*answer:\s*\[(.*?)\],\s*score:\s*(\d+),\s*explanation:\s*[\'"](.*?)[\'"]\s*\}', s, re.S)
    if not blocks:
        blocks = re.findall(r"type: '(single|multi)',\s*options: \[(.*?)\],\s*answer: \[(.*?)\],\s*score: (\d+),\s*explanation: '(.*?)'", s, re.S)
    for i, b in enumerate(blocks):
        print(f'  ANS{i+1}: type={b[0]} answer=[{b[2]}] score={b[3]}')
        print(f'     expl: {b[4].strip()}')
    print('  blocks found:', len(blocks))
