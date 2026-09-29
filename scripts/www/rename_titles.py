# -*- coding: utf-8 -*-
"""统一 367 个页面的 <title> 名称。
用法：
    python rename_titles.py           # 旧名 -> 新名
    python rename_titles.py --revert  # 新名 -> 旧名（撤销）
"""
import glob
import os
import sys

OLD = '365天眼镜门店员工晋级培训'
NEW = '眼镜企业在职员工365天天学练'


def main(revert=False):
    src, dst = (NEW, OLD) if revert else (OLD, NEW)
    files = sorted(glob.glob('day*.html'))
    changed = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        if src not in s:
            continue
        s = s.replace(src, dst)
        open(f, 'w', encoding='utf-8', newline='\n').write(s)
        changed += 1
    print('%s -> %s，已修改 %d / %d 个文件' % (src, dst, changed, len(files)))


if __name__ == '__main__':
    main(revert='--revert' in sys.argv)
