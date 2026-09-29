# -*- coding: utf-8 -*-
import re, glob
files = sorted(glob.glob('day*.html'))
use_correct = []
for f in files:
    s = open(f, encoding='utf-8').read()
    code = re.sub(r"\{\s*text:.*?correct:\s*(?:true|false)\s*\}", "", s, flags=re.S)
    if re.search(r'\.correct|opt\.correct|q\.correct', code):
        use_correct.append(f)
print('代码中读取 correct 字段的文件:', len(use_correct), use_correct[:20])

for f in ['day212.html', 'day332.html', 'day339.html', 'day010.html']:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'const choiceQuestions = (\[.*?\n        \]);', s, re.S) or re.search(r'const choiceQuestions = (\[.*?\]);', s, re.S)
    print('=' * 50)
    print(f)
    print(m.group(1)[:1500] if m else 'no data')
