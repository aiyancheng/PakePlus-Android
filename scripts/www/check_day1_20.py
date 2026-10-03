import sys, os, glob
sys.stdout.reconfigure(encoding='utf-8')

base = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'
missing = []
ok_files = []

for d in range(1, 21):
    pattern = os.path.join(base, '**', 'Day_{:02d}_练习题.html'.format(d))
    files = glob.glob(pattern, recursive=True)
    if not files:
        missing.append('Day_{:02d} - 文件不存在'.format(d))
        continue
    for f in files:
        content = open(f, encoding='utf-8').read()
        has_interactive = 'interactive-options-type' in content
        rel = os.path.relpath(f, base)
        if has_interactive:
            ok_files.append(rel)
        else:
            missing.append(rel + ' - 未改造')

print('=== 已改造 ({}) ==='.format(len(ok_files)))
for x in ok_files:
    print('  OK:', x)

print('\n=== 未改造/缺失 ({}) ==='.format(len(missing)))
for x in missing:
    print('  !!', x)
