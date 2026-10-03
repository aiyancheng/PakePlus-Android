import sys, os, glob
sys.stdout.reconfigure(encoding='utf-8')

base = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'
all_files = sorted(glob.glob(os.path.join(base, '**', '*练习题.html'), recursive=True))

ok = []
missing = []

for f in all_files:
    content = open(f, encoding='utf-8').read()
    rel = os.path.relpath(f, base)
    if 'interactive-options-type' in content:
        ok.append(rel)
    else:
        missing.append(rel)

print('=== 已改造 ({}) ==='.format(len(ok)))
for x in ok:
    print('  OK:', x)

print('\n=== 未改造 ({}) ==='.format(len(missing)))
for x in missing:
    print('  !!', x)
