# -*- coding: utf-8 -*-
"""扫描所有 day*.html 的练习题完整性问题"""
import re, glob, json

files = sorted(glob.glob('day*.html'))
print('total files:', len(files))

empty_opts = []      # options 数组为空
no_essay = []        # 缺少问答题
dup_num = []         # 题号重复 "1. 1."
no_submit = []       # 无提交按钮 / scoreDisplay
footer_out = []      # footer-support 在 </html> 之外
good = []

for f in files:
    s = open(f, encoding='utf-8').read()
    # 1. options 数组是否为空
    opt_blocks = re.findall(r'options:\s*\[(.*?)\]', s, re.S)
    if not opt_blocks:
        continue
    empty = sum(1 for b in opt_blocks if b.strip() == '')
    has = len(opt_blocks) - empty
    if empty > 0:
        empty_opts.append((f, has, empty))
    if has == len(opt_blocks) and len(opt_blocks) > 0:
        good.append(f)
    # 2. 问答题
    if 'essay-question' not in s and '问答题' not in s:
        no_essay.append(f)
    elif '<!-- 问答题部分需要手动调整 -->' in s:
        no_essay.append(f + ' (占位)')
    # 3. 题号重复
    if re.search(r'question-text">\d+\.\s*\d+\.', s):
        dup_num.append(f)
    # 4. 提交按钮
    if 'submitAll' in s and 'scoreDisplay' not in s:
        no_submit.append(f)
    # 5. footer 位置
    i_html = s.rfind('</html>')
    i_footer = s.rfind('footer-support')
    if i_footer > i_html and i_html != -1:
        footer_out.append(f)

print('\n=== 1. 选择题 options 为空 ===', len(empty_opts))
print(empty_opts[:40])
print('\n=== 2. 问答题缺失/占位 ===', len(no_essay))
print(no_essay[:40])
print('\n=== 3. 题号重复 ===', len(dup_num))
print(dup_num[:20])
print('\n=== 4. 无 scoreDisplay（提交判分会报错） ===', len(no_submit))
print(no_submit[:20])
print('\n=== 5. footer-support 在 </html> 之后 ===', len(footer_out))
print(footer_out[:20])
print('\n=== 结构完整参考文件 ===', len(good))
print(good[:20])
