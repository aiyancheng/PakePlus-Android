# -*- coding: utf-8 -*-
"""扫描所有 day*.html 练习题结构要素是否齐全"""
import re, glob

files = sorted(glob.glob('day*.html'))
prob = {'no_practice': [], 'choice_lt3': [], 'no_essay': [], 'no_submit': [],
        'no_score': [], 'empty_ref': [], 'dup_num': []}
for f in files:
    s = open(f, encoding='utf-8').read()
    if 'practice-section' not in s:
        prob['no_practice'].append(f); continue
    n_choice = len(re.findall(r'class="choice-question"', s))
    n_essay = len(re.findall(r'class="essay-question"', s))
    if n_choice < 3: prob['choice_lt3'].append((f, n_choice))
    if n_essay < 1: prob['no_essay'].append(f)
    if 'submit-btn' not in s: prob['no_submit'].append(f)
    if 'id="scoreDisplay"' not in s: prob['no_score'].append(f)
    refs = re.findall(r'<div class="reference-answer" id="essayAnswer\d+">(.*?)</div>', s, re.S)
    if n_essay and (not refs or any(len(r.strip()) < 30 for r in refs)):
        prob['empty_ref'].append(f)
    if re.search(r'question-text">\d+\.\s*\d+\.', s): prob['dup_num'].append(f)

for k, v in prob.items():
    print(f'{k}: {len(v)}')
    if v: print('   ', v[:20])
