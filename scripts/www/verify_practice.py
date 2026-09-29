# -*- coding: utf-8 -*-
"""校验修复后的练习题：选项数量、答案索引、正确答案文本、showReference 签名"""
import re

files = ['day099.html', 'day101.html', 'day102.html', 'day103.html', 'day104.html']
for f in files:
    s = open(f, encoding='utf-8').read()
    print('=' * 60)
    print(f)
    sig = re.search(r'function showReference\(([^)]*)\)', s)
    print('  showReference 签名:', sig.group(1) if sig else 'N/A')
    qs = re.findall(r'<div class="question-text">(.*?)</div>', s, re.S)
    blocks = re.findall(r"type: '(single|multi)',\s*options: \[(.*?)\],\s*answer: \[(.*?)\],\s*score: (\d+),", s, re.S)
    for i, (typ, opts, ans, score) in enumerate(blocks):
        texts = re.findall(r"text: '(.*?)'", opts)
        idxs = [int(x) for x in re.findall(r'\d+', ans)]
        ok = len(texts) == 4 and all(0 <= j < len(texts) for j in idxs)
        letters = '、'.join(chr(65 + j) for j in idxs)
        print(f'  Q{i+1} [{typ}] 选项数={len(texts)} 答案={letters} {"OK" if ok else "!!ERROR"}')
        print(f'     题干: {qs[i].strip()[:45]}')
        for j in idxs:
            print(f'     正确答案: {texts[j]}')
    essay = re.search(r'<div class="question-text">(4\..*?)</div>', s, re.S)
    print('  问答题:', (essay.group(1).strip()[:45] if essay else '缺失'))
