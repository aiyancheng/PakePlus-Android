# -*- coding: utf-8 -*-
"""修复 explanation 双引号字符串内的直双引号"""
import re

f = 'day333.html'
s = open(f, encoding='utf-8').read()


def repl(m):
    body = m.group(2)
    if '"' not in body:
        return m.group(0)
    out, t = [], True
    for ch in body:
        if ch == '"':
            out.append('\u201c' if t else '\u201d')
            t = not t
        else:
            out.append(ch)
    return m.group(1) + ''.join(out) + m.group(3)


pat = re.compile(r'(?m)^(\s*explanation:\s*")(.*?)("(?=,?\s*$))')
s2 = pat.sub(repl, s)
open(f, 'w', encoding='utf-8', newline='\n').write(s2)
print('changed:', s != s2)
