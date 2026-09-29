# -*- coding: utf-8 -*-
"""修复后统一校验：选项数、答案索引、正确答案文本、score"""
import re, glob

targets = ['day075.html','day076.html','day077.html','day078.html','day079.html','day080.html',
           'day081.html','day082.html','day083.html','day084.html',
           'day099.html','day101.html','day102.html','day103.html','day104.html',
           'day332.html','day333.html','day334.html','day335.html','day339.html','day340.html']
bad = []
for f in targets:
    s = open(f, encoding='utf-8').read()
    blocks = re.findall(r"type:\s*['\"](single|multi)['\"],\s*options: \[(.*?)\],\s*answer: \[(.*?)\],\s*score: (\d+),", s, re.S)
    print('=' * 55)
    print(f, '| 题目数:', len(blocks))
    for i, (typ, opts, ans, score) in enumerate(blocks):
        texts = re.findall(r"text:\s*['\"](.*?)['\"]", opts)
        idxs = [int(x) for x in re.findall(r'\d+', ans)]
        ok = len(texts) == 4 and idxs and max(idxs) < len(texts)
        if not ok:
            bad.append((f, i + 1, len(texts), idxs))
        letters = '、'.join(chr(65 + j) for j in idxs)
        print(f'  Q{i+1} [{typ}] 选项={len(texts)} 答案={letters} score={score} {"OK" if ok else "!!"}')
print('\n异常:', bad if bad else '无')
