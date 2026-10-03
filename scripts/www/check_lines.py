import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才"
weeks = [
    "第1周_文化与制度启蒙",
    "第2周_光学与产品知识",
    "第3周_专业技能训练",
    "第4周_销售话术与中期考核",
    "第5周_实战跟岗训练",
    "第6周_独立接单训练",
    "第7周_综合提升训练",
    "第8周_结业冲刺与毕业考核",
]

short_files = []
for week in weeks:
    week_dir = os.path.join(base, week)
    for fn in sorted(os.listdir(week_dir)):
        if fn.endswith("_学习内容.html"):
            fp = os.path.join(week_dir, fn)
            with open(fp, encoding='utf-8') as f:
                lines = f.readlines()
            count = len(lines)
            if count < 200:
                short_files.append((count, fn, week, fp))

short_files.sort(key=lambda x: x[0])
print(f"共有 {len(short_files)} 个学习内容文件不足200行：\n")
for count, fn, week, fp in short_files:
    print(f"  [{count:3d}行] {week}/{fn}")
