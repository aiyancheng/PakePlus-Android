# -*- coding: utf-8 -*-
"""把原本设计为 4 列的卡片网格固定为「一行 4 列」：
1) 移除平板适配层 / 旧媒体查询里对它们的降级（3 列 / 2 列 / 1 列）
2) 在样式表最末追加固定 4 列规则（窄屏靠缩小字号与间距适配）
幂等，可重复执行。
"""
import io, os, re, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = '.'
MARK = '四列卡片固定一行4列'
BAK = '_bak_tablet'


def main_css(css):
    return css.split('@media')[0]


def find4(css):
    """主 CSS 中 grid-template-columns: repeat(4, ...) 的类选择器"""
    out = set()
    for m in re.finditer(r'([^{}]+)\{([^{}]*grid-template-columns[^}]*)\}', main_css(css)):
        body = m.group(2)
        if not re.search(r'repeat\(\s*4\s*,', body):
            continue
        for s in m.group(1).split(','):
            s = s.strip()
            if s.startswith('.'):
                out.add(s)
    return sorted(out)


def strip_from_selector_list(css, cls):
    """把 cls 从 `.a, .b, .cls, .c { ... }` 这类选择器列表里删掉；若列表空则整条规则删除"""
    def repl(m):
        sel, body = m.group(1), m.group(2)
        parts = [p.strip() for p in sel.split(',') if p.strip()]
        parts = [p for p in parts if p != cls]
        if not parts:
            return ''
        return ', '.join(parts) + '{' + body + '}'
    css = re.sub(r'([^{}]*\b' + re.escape(cls) + r'\b[^{}]*)\{([^{}]*)\}', repl, css)
    return css


def depth(css):
    d = 0
    for ch in css:
        if ch == '{':
            d += 1
        elif ch == '}':
            d -= 1
    return d


def process(path):
    h = io.open(path, encoding='utf-8').read()
    m = re.search(r'(<style>)(.*?)(</style>)', h, re.S)
    if not m:
        return None
    css = m.group(2)
    cls4 = find4(css)
    if not cls4:
        return None

    orig = h
    if not os.path.exists(path + '.bak_grid4'):
        shutil.copy2(path, path + '.bak_grid4')

    # 0) 去掉上一次追加的块（幂等）
    css = re.sub(r'\n/\* ═+ ' + re.escape(MARK) + r'.*?(?=\n</style>|\Z)', '\n', css, flags=re.S)

    d0 = depth(css)
    for c in cls4:
        # 1) 删除针对该类的 grid-template-columns 覆盖规则（适配层里的 3/2/1 列）
        css = re.sub(r'[ \t]*' + re.escape(c) + r'\s*\{\s*grid-template-columns:[^}]*\}\n?', '', css)
        # 2) 从选择器列表中剔除
        css2 = strip_from_selector_list(css, c)
        # 列表改写可能破坏括号结构，只在括号深度不变时才采用
        if depth(css2) == depth(css):
            css = css2
    if depth(css) != d0:
        print('!! 括号结构异常，跳过:', path)
        return None

    # 3) 追加固定 4 列块（放最末，优先级最高）
    sel = ','.join(cls4)
    block = '\n/* ═══════ ' + MARK + ' ═══════ */\n'
    block += sel + '{grid-template-columns:repeat(4,1fr)!important}\n'
    for c in cls4:
        block += c + '>*{min-width:0;overflow-wrap:break-word}\n'
    block += '@media(max-width:1150px){\n'
    block += '  ' + sel + '{grid-template-columns:repeat(4,1fr)!important;gap:10px!important}\n'
    block += '  ' + sel + '>*{padding:12px 8px!important}\n'
    block += '}\n'
    block += '@media(max-width:900px){\n'
    block += '  ' + sel + '{grid-template-columns:repeat(4,1fr)!important;gap:8px!important}\n'
    block += '  ' + sel + '>*{padding:10px 6px!important;font-size:12px!important}\n'
    block += '  ' + sel + ' .icon,' + sel + ' .letter{font-size:20px!important}\n'
    block += '  ' + sel + ' .title,' + sel + ' .name{font-size:13px!important}\n'
    block += '  ' + sel + ' .desc{font-size:11px!important;line-height:1.45!important}\n'
    block += '}\n'
    block += '@media(max-width:640px){\n'
    block += '  ' + sel + '{grid-template-columns:repeat(4,1fr)!important;gap:5px!important}\n'
    block += '  ' + sel + '>*{padding:8px 4px!important;font-size:11px!important}\n'
    block += '  ' + sel + ' .icon,' + sel + ' .letter{font-size:17px!important}\n'
    block += '  ' + sel + ' .title,' + sel + ' .name{font-size:11px!important}\n'
    block += '  ' + sel + ' .desc{font-size:10px!important;line-height:1.4!important}\n'
    block += '}\n'

    # 插到 </style> 之前
    newcss = css.rstrip() + '\n' + block
    h = h[:m.start(2)] + newcss + h[m.end(2):]
    if h != orig:
        io.open(path, 'w', encoding='utf-8').write(h)
    return cls4


def main():
    os.makedirs(BAK, exist_ok=True)
    done = []
    for root, dirs, fs in os.walk(ROOT):
        if '.workbuddy' in root or '_bak' in root:
            continue
        for f in fs:
            if not f.endswith('.html'):
                continue
            r = process(os.path.join(root, f))
            if r:
                done.append((os.path.join(root, f), r))
    for p, r in done:
        print('已固定4列:', p, r)
    print('共处理 %d 个文件' % len(done))
    # 归档备份
    n = 0
    for root, dirs, fs in os.walk(ROOT):
        if '.workbuddy' in root or '_bak' in root:
            continue
        for f in fs:
            if f.endswith('.bak_grid4'):
                src = os.path.join(root, f)
                dst = os.path.join(BAK, os.path.relpath(src, '.').replace(os.sep, '__'))
                shutil.move(src, dst)
                n += 1
    print('备份归档 %d 个' % n)


if __name__ == '__main__':
    main()
