# -*- coding: utf-8 -*-
"""用 node 语法检查指定 HTML 中的 <script> 代码"""
import re, subprocess, sys, glob, tempfile, os

if len(sys.argv) > 1 and sys.argv[1] == '--all':
    files = sorted(glob.glob('day*.html'))
else:
    files = sys.argv[1:] if len(sys.argv) > 1 else ['day099.html', 'day101.html', 'day102.html', 'day103.html', 'day104.html']
bad = []
for f in files:
    s = open(f, encoding='utf-8').read()
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', s, re.S)
    for i, code in enumerate(scripts):
        tmp = os.path.join(tempfile.gettempdir(), 'chk_%s_%d.js' % (f.replace('.', '_'), i))
        open(tmp, 'w', encoding='utf-8').write(code)
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        if r.returncode != 0:
            bad.append((f, i, r.stderr[:300]))
        os.remove(tmp)
print('检查文件数:', len(files))
if bad:
    for b in bad: print('  SYNTAX ERROR:', b)
else:
    print('  全部通过 JS 语法检查')
