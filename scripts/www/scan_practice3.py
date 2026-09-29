# -*- coding: utf-8 -*-
"""更准确地检测参考答案是否为空 / 题号重复情况"""
import re, glob

files = sorted(glob.glob('day*.html'))
bad_ref = []
dup_detail = []
for f in files:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<div class="reference-answer"[^>]*>', s):
        seg = s[m.end():m.end() + 900]
        idx = seg.find('</div>')
        body = seg[:idx if idx > 0 else len(seg)]
        text = re.sub(r'<[^>]+>', '', body).strip()
        if len(text) < 40:
            bad_ref.append((f, len(text), text[:40]))
    for m in re.finditer(r'<div class="question-text">(.*?)</div>', s, re.S):
        t = m.group(1).strip()
        mm = re.match(r'^(\d+)\.\s*(\d+)\.', t)
        if mm:
            dup_detail.append((f, t[:40]))

print('参考答案过短:', len(bad_ref))
for x in bad_ref: print('  ', x)
print('题号重复:', len(dup_detail))
for x in dup_detail: print('  ', x)
