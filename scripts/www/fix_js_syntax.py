# -*- coding: utf-8 -*-
"""批量修复练习题脚本中的 JS 语法错误与缺失字段"""
import re, shutil, os, glob

def smart_quote(text, left, right):
    """把内部的直引号交替替换为成对弯引号"""
    out = []
    toggle = True
    for ch in text:
        if ch in ('\'', '"'):
            out.append(left if toggle else right)
            toggle = not toggle
        else:
            out.append(ch)
    return ''.join(out)

changed = {}

def edit(fname, fn):
    bak = fname + '.bak_practice2'
    if not os.path.exists(bak):
        shutil.copy2(fname, bak)
    s = open(fname, encoding='utf-8').read()
    s2 = fn(s)
    if s2 != s:
        open(fname, 'w', encoding='utf-8', newline='\n').write(s2)
        changed[fname] = True
        print('FIXED', fname)
    else:
        print('  no change', fname)

# ---- (1) day075-084：删除残缺的选项行 ----
def fix_stray(s):
    return re.sub(r'(?m)^[ \t]*, correct: (?:true|false) \},[ \t]*\n', '', s)

for i in range(75, 85):
    edit('day%03d.html' % i, fix_stray)

# ---- (2) 单引号内含直单引号（explanation / text）----
def fix_single(s):
    def repl(m):
        head, body, tail = m.group(1), m.group(2), m.group(3)
        return head + smart_quote(body, '\u2018', '\u2019') + tail
    s = re.sub(r"(?m)^(\s*explanation: ')(.*?)('(?=,?\s*$))", repl, s)
    s = re.sub(r"(?m)^(\s*\{ text: ')(.*?)('(?= \},?\s*$))", repl, s)
    return s

for f in ['day099.html', 'day101.html', 'day102.html', 'day103.html', 'day104.html']:
    edit(f, fix_single)

# ---- (3) 双引号内含直双引号（text 字段）----
def fix_double(s):
    def repl(m):
        return m.group(1) + smart_quote(m.group(2), '\u201c', '\u201d') + m.group(3)
    return re.sub(r'(text:\s*")(.*?)(",\s*correct:)', repl, s)

for f in ['day333.html']:
    edit(f, fix_double)

# ---- (4) 缺 answer / score：由 correct:true 推导 ----
def fix_missing_answer(s):
    def repl(m):
        opts = m.group(0)
        idxs = [i for i, o in enumerate(re.findall(r'\{\s*text:.*?correct:\s*(true|false)\s*\}', opts, re.S)) if o == 'true']
        return opts + '\n                answer: [%s],\n                score: 10,' % ', '.join(str(i) for i in idxs)
    # 仅处理其后没有 answer 的 options 块
    out = []
    pos = 0
    for m in re.finditer(r'options: \[.*?\n\s*\],(?![^\n]*answer)', s, re.S):
        seg = s[pos:m.start()]
        tail = s[m.end():m.end() + 200]
        if 'answer:' in tail:
            out.append(seg + m.group(0))
        else:
            out.append(seg + repl(m))
        pos = m.end()
    out.append(s[pos:])
    return ''.join(out)

for f in ['day332.html', 'day333.html', 'day334.html', 'day335.html', 'day339.html', 'day340.html']:
    edit(f, fix_missing_answer)

print('done, changed:', len(changed))
