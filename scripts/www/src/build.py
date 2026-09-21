# -*- coding: utf-8 -*-
"""生成「二次函数26讲」站点：index.html + 26 个分讲 HTML"""
import json
import os
import re
import html

from diagrams import draw
from template import page
from lessons_01_09 import LESSONS_A
from lessons_10_18 import LESSONS_B
from lessons_19_26 import LESSONS_C

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = LESSONS_A + LESSONS_B + LESSONS_C


# ---------------- 行内标记 ----------------
def md(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"==(.+?)==", r'<span class="hl">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r'<span class="mono">\1</span>', s)
    return s


def blocks(items):
    out = []
    for it in items:
        if isinstance(it, dict):
            if "h" in it:
                out.append('<h3 class="sub">' + md(it["h"]) + "</h3>")
                for p in it.get("p", []):
                    out.append("<p>" + md(p) + "</p>")
            elif "rows" in it:
                rows = "".join(
                    '<div class="row"><div class="k">' + md(k) + '</div><div class="v">' + md(v) + "</div></div>"
                    for k, v in it["rows"])
                out.append('<div class="formula">' + rows + "</div>")
            elif "note" in it:
                out.append('<div class="formula"><div class="v">' + md(it["note"]) + "</div></div>")
            elif "grid" in it:
                cells = "".join('<div class="mini"><h4>' + md(c[0]) + "</h4><p>" + md(c[1]) + "</p></div>"
                                for c in it["grid"])
                cls = "grid3" if len(it["grid"]) % 3 == 0 else "grid2"
                out.append('<div class="' + cls + '">' + cells + "</div>")
        else:
            if re.match(r'^[一二三四五六七八九十]{1,3}[、．.]', it) and len(it) <= 40:
                out.append('<h3 class="sub">' + md(it) + "</h3>")
            else:
                out.append("<p>" + md(it) + "</p>")
    return "\n".join(out)


def fname(i, name):
    return "%02d_%s.html" % (i, name.replace("·", "").replace(" ", ""))


# ---------------- 分讲页面 ----------------
def render_lesson(idx, l):
    i = l["no"]
    prev_l = LESSONS[idx - 1] if idx > 0 else None
    next_l = LESSONS[idx + 1] if idx < len(LESSONS) - 1 else None

    hero = [
        '<div class="hero"><div class="hero-in">',
        '<div class="crumb"><a href="index.html">二次函数26讲</a> / ' + md(l["group"]) + " / 第" + str(i) + "讲</div>",
        '<div class="badge-line"><span class="badge">第 ' + str(i) + " 讲 / 共 26 讲</span>"
        '<span class="badge">' + md(l["group"]) + '</span>'
        '<span class="badge gold">' + md(l.get("tag", "核心专题")) + "</span></div>",
        '<h1 class="title">' + md(l["name"]) + "</h1>",
        '<div class="motto">' + md(l["motto"]) + "</div>",
        '<div class="hero-meta">概念讲透型 · 原理推导 + 图像逻辑 + 生活场景 + 自测反馈</div>',
        "</div></div>",
    ]

    b = ['<div class="wrap">']
    b.append('<div class="card">')
    b.append('<div class="hook"><div class="t">🌱 生活引子：为什么要学这一讲</div>')
    for p in l["hook"]:
        b.append("<p>" + md(p) + "</p>")
    b.append("</div>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">壹</span>从原理上讲透</h2>')
    b.append(blocks(l["derive"]))
    b.append("</div>")

    if l.get("diagram"):
        b.append('<div class="card">')
        b.append('<h2 class="sec"><span class="n">贰</span>图像里的逻辑</h2>')
        for d in l["diagram"]:
            b.append("<figure>" + draw(d) + "<figcaption>" + md(d.get("note", "")) + "</figcaption></figure>")
        b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">叁</span>核心结论（要背的）</h2>')
    b.append(blocks(l["points"]))
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">肆</span>解题步骤：拿到题怎么下手</h2>')
    b.append('<ol class="num">' + "".join("<li>" + md(s) + "</li>" for s in l["steps"]) + "</ol>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">伍</span>例题精讲</h2>')
    for k, e in enumerate(l["examples"]):
        tag = "例" + str(k + 1) if not e.get("tag") else e["tag"]
        cls = "tag g" if e.get("hard") else "tag"
        b.append('<div class="ex">')
        b.append('<div class="ex-q"><span class="' + cls + '">' + md(tag) + "</span>" + md(e["q"]) + "</div>")
        b.append('<details class="sol"><summary>展开完整解析</summary><div class="sol-body">')
        if e.get("think"):
            b.append('<p style="color:#6b7280;font-size:14.5px"><b>思路：</b>' + md(e["think"]) + "</p>")
        b.append("<ol>" + "".join("<li>" + md(s) + "</li>" for s in e["sol"]) + "</ol>")
        b.append('<div class="ansbox">' + md(e["ans"]) + "</div>")
        b.append("</div></details></div>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">陆</span>易错陷阱</h2>')
    b.append('<div class="pit"><h4>⚠️ 这一讲最容易丢分的地方</h4>')
    b.append('<ul class="dot">' + "".join("<li>" + md(s) + "</li>" for s in l["pitfalls"]) + "</ul>")
    b.append("</div></div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">柒</span>它在生活里长什么样</h2>')
    b.append('<div class="life"><h4>🏀 从课本走到现实</h4>')
    b.append('<ul class="dot">' + "".join("<li>" + md(s) + "</li>" for s in l["life"]) + "</ul>")
    b.append("</div></div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">捌</span>本节小结</h2>')
    b.append('<div class="sum"><h4>✍️ 记住这几条就够了</h4>')
    b.append('<ul class="dot">' + "".join("<li>" + md(s) + "</li>" for s in l["summary"]) + "</ul>")
    b.append("</div>")
    if l.get("verse"):
        b.append('<div class="verse" style="margin-top:14px">' + md(l["verse"]) + "</div>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">玖</span>自测反馈</h2>')
    b.append('<div id="quiz"></div>')
    b.append("</div>")

    b.append('<div class="nav">')
    if prev_l:
        b.append('<a href="' + fname(prev_l["no"], prev_l["name"]) + '"><span>← 上一讲</span>'
                 + html.escape(prev_l["name"]) + "</a>")
    else:
        b.append('<a href="index.html"><span>← 返回</span>课程目录</a>')
    b.append('<a class="home" href="index.html"><span>课程总目录</span>二次函数26讲</a>')
    if next_l:
        b.append('<a href="' + fname(next_l["no"], next_l["name"]) + '"><span>下一讲 →</span>'
                 + html.escape(next_l["name"]) + "</a>")
    else:
        b.append('<a href="index.html"><span>返回 →</span>课程目录</a>')
    b.append("</div>")

    b.append("<footer>二次函数26讲 · 第 " + str(i) + " 讲《" + html.escape(l["name"]) + "》"
             "｜概念讲透型 · 建议先遮住解析自己做一遍</footer>")
    b.append("</div>")

    qs = json.dumps(l["quiz"], ensure_ascii=False, indent=2)
    return page("第%02d讲 %s | 二次函数26讲" % (i, l["name"]), "\n".join(hero), "\n".join(b), qs)


# ---------------- 目录页 ----------------
METHODS = [
    ["方法一 · 判别定根", "Δ=b²−4ac", "Δ>0 两根不同、Δ=0 一根（重根）、Δ<0 无实根。含参题第一道门。"],
    ["方法二 · 韦达和积", "x₁+x₂=−b/a，x₁x₂=c/a", "和定正负方向、积定同号异号，不求出根也能判性质。"],
    ["方法三 · 穿针引线", "化正→标根→穿线→定解", "奇穿偶不穿，从右上角起笔，高次不等式通杀。"],
    ["方法四 · 图像卡点", "Δ + 对称轴 + f(k) 三条件", "区间根、同侧根的唯一解法，缺一不可。"],
    ["方法五 · 对称轴位", "x=−b/2a", "决定两根整体靠左还是靠右，卡点法的核心位置变量。"],
    ["方法六 · 开口方向", "a>0 向上，a<0 向下", "决定外部位置、f(k) 变号方向、比大小结果。"],
    ["方法七 · 看高看低", "图像在上，函数值大", "函数不等式与函数值比较的不二法门。"],
    ["方法八 · 端点取舍", "有等号端点可取", "Δ=0 可取、分母的根必须舍去，端点逐项核对。"],
]

VERSES = [
    ["第一句", "判别式兜底万变", "Δ=b²−4ac 永远先算，没根后面都不用列。"],
    ["第二句", "韦达和积定正反", "ac 定同异、ab 定正负，判根正负别硬解。"],
    ["第三句", "奇穿偶不穿一点", "化正→标根→穿线→定解，所有整式不等式通杀。"],
    ["第四句", "异号乘积必穿轴", "f(m)·f(n)<0 区间恰一根，闭区间另验端点。"],
    ["第五句", "开口方向莫看反", "看图第一步先看开口，一切方法建立在开口明确之上。"],
]

LIFE = [
    ["拱桥承重", "桥拱是一条抛物线", "顶点处承重最大 → 求最值就是求顶点坐标"],
    ["喷泉水柱", "水柱轨迹是抛物线", "最高点高度 → 顶点纵坐标 = 最大高度"],
    ["篮球抛投", "球的飞行轨迹", "何时到最高点 → 对称轴 t = −b/2a"],
    ["灯光设计", "抛物面反射聚光", "照射距离 → 抛物线与地面的落点距离"],
    ["利润最大化", "收入是二次的", "定价多少利润最高 → 顶点横坐标"],
]


def render_index():
    hero = (
        '<div class="hero"><div class="hero-in">'
        '<div class="badge-line"><span class="badge">初中数学 · 二次函数</span>'
        '<span class="badge gold">26 讲全部完结</span></div>'
        '<h1 class="title">二次函数 26 讲通关 · 课程总目录</h1>'
        '<div class="motto">从第 1 讲「平移·左加右减」出发，到第 26 讲「区间内恰有一根」收官'
        "——每一讲攻克一类题型、一套方法。前 13 讲围着「图像」转，后 13 讲围着「根」转。</div>"
        '<div class="hero-meta">概念讲透型：原理推导 → 图像逻辑 → 核心结论 → 例题精讲 → 易错陷阱 → '
        "生活场景 → 小结口诀 → 自测反馈</div>"
        "</div></div>"
    )

    b = ['<div class="wrap">']
    b.append('<div class="card">')
    b.append('<div class="stat">'
             '<div><b>26</b><span>讲课程</span></div>'
             '<div><b>8</b><span>套方法</span></div>'
             '<div><b>5</b><span>句口诀</span></div>'
             '<div><b>78</b><span>道自测题</span></div>'
             "</div>")
    b.append('<p class="lead" style="margin-top:14px">'
             "学完 26 讲还做错题，往往不是不会，而是知识散成一把豆子、考场上一紧张抓错那一颗。"
             "这套课程按<b>「先懂为什么，再用套路」</b>的方式编排：每一讲都从原理推导讲起，配一张示意图建立图像感，"
             "再落到可执行的步骤与例子。建议按顺序学，学完一讲立刻做自测。</p>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">目</span>课程地图</h2>')
    cur = None
    for l in LESSONS:
        if l["group"] != cur:
            cur = l["group"]
            desc = ("练的是画图、看图的基本功：平移、对称、最值、符号"
                    if cur.endswith("图像篇") else
                    "练的是数形结合的硬功夫：判别式、韦达定理、根的分布")
            b.append('<div class="group">' + md(cur) + "</div>")
            b.append('<div class="g-desc">' + desc + "</div>")
            b.append('<div class="lessons">')
        b.append('<a class="lesson" href="' + fname(l["no"], l["name"]) + '">'
                 '<div class="no">第 ' + str(l["no"]) + " 讲</div>"
                 '<div class="nm">' + html.escape(l["name"]) + "</div>"
                 '<div class="mo">' + md(l["motto"]) + "</div></a>")
        nxt = LESSONS[LESSONS.index(l) + 1]["group"] if LESSONS.index(l) + 1 < len(LESSONS) else None
        if nxt != cur:
            b.append("</div>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">法</span>26 讲其实只有八套方法</h2>')
    b.append("<p>遇到题先看它属于哪一类，再打开对应的那一枚锦囊。</p>")
    b.append('<table class="tb"><tr><th style="width:22%">锦囊</th><th style="width:28%">核心式子</th><th>什么时候用</th></tr>')
    for m in METHODS:
        b.append("<tr><td><b>" + md(m[0]) + "</b></td><td>" + md(m[1]) + "</td><td>" + md(m[2]) + "</td></tr>")
    b.append("</table></div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">诀</span>五句口诀 · 考前十分钟</h2>')
    for v in VERSES:
        b.append('<div class="verse" style="margin-bottom:12px;text-align:left;font-size:16px">' +
                 md(v[0]) + "｜" + md(v[1]) + "　——　" + md(v[2]) + "</div>")
    b.append("</div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">用</span>二次函数在生活里长什么样</h2>')
    b.append('<table class="tb"><tr><th style="width:20%">场景</th><th style="width:26%">数学本质</th><th>对应的讲次</th></tr>')
    for x in LIFE:
        b.append("<tr><td><b>" + md(x[0]) + "</b></td><td>" + md(x[1]) + "</td><td>" + md(x[2]) + "</td></tr>")
    b.append("</table></div>")

    b.append('<div class="card">')
    b.append('<h2 class="sec"><span class="n">序</span>建议的学习顺序</h2>')
    b.append('<ol class="num">'
             "<li><b>初次学：</b>按第 1→26 讲顺序来，每讲先自己推一遍原理，再看解析。</li>"
             "<li><b>考前复习：</b>优先重看第 3、8、9、10、18、20、24、25、26 讲——这几讲是中考高频。</li>"
             "<li><b>做题手感：</b>遮住解析，先看题干判断「该用哪套方法」，三秒内调不出来就回看该讲的核心结论。</li>"
             "<li><b>错题处理：</b>错题回到对应讲次，只看「易错陷阱」和「核心结论」两块。</li>"
             "</ol></div>")

    b.append("<footer>二次函数26讲 · 概念讲透型课程包｜共 26 讲，每讲含：原理推导 · 图像逻辑 · 核心结论 · "
             "解题步骤 · 例题精讲 · 易错陷阱 · 生活场景 · 小结口诀 · 自测反馈</footer>")
    b.append("</div>")
    return page("二次函数26讲 · 课程总目录", hero, "\n".join(b))


def main():
    if not os.path.exists(OUT):
        os.makedirs(OUT)
    n = 0
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    n += 1
    for idx, l in enumerate(LESSONS):
        p = os.path.join(OUT, fname(l["no"], l["name"]))
        with open(p, "w", encoding="utf-8") as f:
            f.write(render_lesson(idx, l))
        n += 1
        lines = len(open(p, encoding="utf-8").read().splitlines())
        flag = "OK " if lines >= 200 else "!! "
        print("%s%02d %-16s %4d 行" % (flag, l["no"], l["name"], lines))
    print("\n共生成 %d 个文件 -> %s" % (n, OUT))


if __name__ == "__main__":
    main()
