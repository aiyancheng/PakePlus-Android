# -*- coding: utf-8 -*-
"""
为每一天的学习内容注入统一学习模块：
  1. 当日学习目标（3-5 条）
  2. 动手实践任务（1-2 个）
  3. 常见问题与注意事项
  4. 参考资料
  5. 自测题（3-5 道，折叠答案）
  6. 每周最后一天：本周回顾小结 + 阶段性检查点

用法：python enrich.py [--dry]
幂等：以 <!-- LM-START --> / <!-- LM-END --> 标记，重复执行不叠加。
"""
import io
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(BASE, '_bak_tablet')
MARK_S = '<!-- LM-START -->'
MARK_E = '<!-- LM-END -->'
DRY = '--dry' in sys.argv

# ─────────── 样式（无描边，色块 + 圆角，与其他页面风格一致） ───────────
CSS = """
  /* ═══════ 每日学习标准模块（目标 / 实践 / FAQ / 参考 / 自测 / 阶段复盘） ═══════ */
  .lm-block{border-radius:14px;padding:20px 24px;margin:24px 0;line-height:1.85}
  .lm-block h3{margin:0 0 14px;font-size:1.1em;font-weight:700;letter-spacing:.3px}
  .lm-list{margin:0;padding-left:22px}
  .lm-list li{margin-bottom:9px}
  .lm-goal{background:#e8f5e9;color:#1b5e20}
  .lm-goal h3{color:#2e7d32}
  .lm-practice{background:#fff8e1;color:#4e342e}
  .lm-practice h3{color:#e65100}
  .lm-faq{background:#f3e5f5;color:#4a148c}
  .lm-faq h3{color:#7b1fa2}
  .lm-ref{background:#e3f2fd;color:#0d3c61}
  .lm-ref h3{color:#1565c0}
  .lm-quiz{background:#fce4ec;color:#880e4f}
  .lm-quiz h3{color:#c2185b}
  .lm-review{background:#ede7f6;color:#311b92}
  .lm-review h3{color:#4527a0}
  .lm-meta{margin:12px 0 0;font-size:.9em;opacity:.92}
  .lm-pr{margin:0 0 14px;padding:14px 16px;background:rgba(255,255,255,.75);border-radius:10px}
  .lm-pr:last-child{margin-bottom:0}
  .lm-pr-t{font-weight:700;margin-bottom:6px}
  .lm-pr-d{margin-bottom:6px}
  .lm-pr-o{font-size:.92em;font-weight:600}
  .lm-q{margin:0 0 10px;padding:10px 14px;background:rgba(255,255,255,.75);border-radius:10px}
  .lm-q:last-child{margin-bottom:0}
  .lm-q summary{cursor:pointer;font-weight:600;line-height:1.7}
  .lm-q[open] summary{margin-bottom:8px}
  .lm-a{font-size:.95em;color:#212121;line-height:1.8}
  .lm-a b{color:#c2185b}
  .lm-faq .lm-a b{color:#7b1fa2}
  .lm-sub{font-weight:700;margin:14px 0 8px;font-size:1em}
  @media(max-width:900px){
    .lm-block{padding:16px 14px;margin:18px 0;line-height:1.75}
    .lm-block h3{font-size:1.02em}
    .lm-list{padding-left:18px}
  }
"""


def esc(s):
    return s


def goal_html(d):
    lis = '\n'.join('      <li>%s</li>' % esc(x) for x in d['goal'])
    return ("""
<div class="lm-block lm-goal">
  <h3>🎯 今日学习目标（学完你应该能做到）</h3>
  <ul class="lm-list">
%s
  </ul>
  <p class="lm-meta">⏱ 学习量控制：约 <strong>2 小时</strong> —— 精读讲解 60 分钟 ｜ 动手实践 45 分钟 ｜ 自测与订正 15 分钟</p>
</div>""" % lis)


def practice_html(d):
    if not d.get('practice'):
        return ''
    items = []
    for i, p in enumerate(d['practice'], 1):
        t, desc, out = p[0], p[1], p[2]
        items.append("""    <div class="lm-pr">
      <div class="lm-pr-t">任务 %d：%s</div>
      <div class="lm-pr-d">%s</div>
      <div class="lm-pr-o">✅ 完成标准：%s</div>
    </div>""" % (i, esc(t), esc(desc), esc(out)))
    return """
<div class="lm-block lm-practice">
  <h3>🔧 动手实践任务（今日必做）</h3>
%s
</div>""" % '\n'.join(items)


def faq_html(d):
    if not d.get('faq'):
        return ''
    items = []
    for q, a in d['faq']:
        items.append("""    <details class="lm-q">
      <summary>❓ %s</summary>
      <div class="lm-a">%s</div>
    </details>""" % (esc(q), esc(a)))
    return """
<div class="lm-block lm-faq">
  <h3>⚠️ 常见问题与注意事项</h3>
%s
</div>""" % '\n'.join(items)


def ref_html(d):
    if not d.get('ref'):
        return ''
    lis = '\n'.join('      <li>%s</li>' % esc(x) for x in d['ref'])
    return """
<div class="lm-block lm-ref">
  <h3>📚 参考资料（可边学边查）</h3>
  <ul class="lm-list">
%s
  </ul>
</div>""" % lis


def quiz_html(d):
    if not d.get('quiz'):
        return ''
    items = []
    for i, (q, a) in enumerate(d['quiz'], 1):
        items.append("""    <details class="lm-q">
      <summary>第 %d 题：%s</summary>
      <div class="lm-a"><b>参考答案：</b>%s</div>
    </details>""" % (i, esc(q), esc(a)))
    return """
<div class="lm-block lm-quiz">
  <h3>📝 今日自测（先做完再看答案）</h3>
%s
</div>""" % '\n'.join(items)


def review_html(d):
    r = d.get('review')
    if not r:
        return ''
    pts = '\n'.join('      <li>%s</li>' % esc(x) for x in r['sum'])
    rows = '\n'.join('        <tr><td>%s</td><td>%s</td></tr>' % (esc(a), esc(b))
                     for a, b in r['check'])
    return """
<div class="lm-block lm-review">
  <h3>🗓️ 本周回顾小结与阶段检查点</h3>
  <div class="lm-sub">① 本周知识串讲（前后衔接）</div>
  <ul class="lm-list">
%s
  </ul>
  <div class="lm-sub">② 阶段检查点（达到才算过关，未达标先补这天的内容）</div>
  <table class="rule-table">
    <thead><tr><th>检查点</th><th>达标标准</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
  <p class="lm-meta">💡 自检方式：逐项打勾 → 有 2 项以上未达标，先把对应天的自测题重做一遍，再请师傅复评。</p>
</div>""" % (pts, rows)


def build_tail(d):
    return MARK_S + practice_html(d) + faq_html(d) + ref_html(d) + \
        quiz_html(d) + review_html(d) + '\n' + MARK_E


# ─────────── 注入 ───────────
def inject_css(h):
    if '每日学习标准模块' in h:
        return h
    i = h.rfind('</style>')
    if i < 0:
        return h
    return h[:i] + CSS + '\n  ' + h[i:]


def find_tail_pos(h):
    """导航块之前"""
    for cls in ('nav-footer', 'nav-bar'):
        m = re.search(r'\n\s*<div class="%s"' % cls, h)
        if m:
            return m.start()
    m = re.search(r'\n\s*<div class="nav-btn', h)
    if m:
        return m.start()
    i = h.rfind('</div>')
    return i if i > 0 else len(h)


def find_head_pos(h):
    """正文首个 h2 / 主区块之前"""
    best = -1
    for pat in (r'\n\s*<h2', r'\n\s*<div class="section', r'\n\s*<div class="objective-box"',
                r'\n\s*<div class="highlight-box"', r'\n\s*<div class="story-box"'):
        m = re.search(pat, h)
        if m and (best < 0 or m.start() < best):
            best = m.start()
    if best > 0:
        return best
    m = re.search(r'<div class="container">', h)
    return m.end() if m else -1


def process(path, d):
    h = io.open(path, encoding='utf-8').read()
    orig = h
    h = inject_css(h)

    # 头部：学习目标
    if d.get('goal') and '今日学习目标（学完你应该能做到）' not in h:
        pos = find_head_pos(h)
        if pos > 0:
            h = h[:pos] + '\n' + goal_html(d) + '\n' + h[pos:]

    # 尾部：实践 / FAQ / 参考 / 自测 / 复盘
    if MARK_S in h:
        s = h.index(MARK_S)
        e = h.index(MARK_E) + len(MARK_E)
        h = h[:s] + build_tail(d) + h[e:]
    else:
        pos = find_tail_pos(h)
        h = h[:pos] + '\n' + build_tail(d) + '\n' + h[pos:]

    if h == orig:
        return 0
    if not DRY:
        io.open(path, 'w', encoding='utf-8').write(h)
    return 1


def load_data():
    data = {}
    sys.path.insert(0, os.path.join(BASE, '_enrich'))
    import importlib
    for w in range(1, 9):
        try:
            m = importlib.import_module('w%d' % w)
        except Exception as e:
            print('  跳过 w%d：%s' % (w, e))
            continue
        for k, v in getattr(m, 'DAYS', {}).items():
            data[k] = v
    return data


def main():
    data = load_data()
    print('数据天数：%d' % len(data))
    os.makedirs(BAK, exist_ok=True)
    done = skip = miss = 0
    missing = []
    for root, dirs, fs in sorted(os.walk(BASE)):
        if '.workbuddy' in root or '_bak' in root or '_enrich' in root or '_ima' in root:
            continue
        for f in sorted(fs):
            if not f.endswith('学习内容.html'):
                continue
            p = os.path.join(root, f)
            key = f[:6]
            d = data.get(key)
            if not d:
                miss += 1
                missing.append(key)
                continue
            if not DRY:
                bak = p + '.bak_enrich'
                shutil.copy2(p, bak)
                name = os.path.relpath(bak, BASE).replace(os.sep, '__')
                dst = os.path.join(BAK, name)
                if os.path.exists(dst):
                    os.remove(dst)
                shutil.move(bak, dst)
            n = process(p, d)
            if n:
                done += 1
            else:
                skip += 1
    print('已写入 %d 个，无变化 %d 个，缺数据 %d 个' % (done, skip, miss))
    if missing:
        print('缺数据：', sorted(missing))


if __name__ == '__main__':
    main()
