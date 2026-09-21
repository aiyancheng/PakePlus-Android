# -*- coding: utf-8 -*-
"""二次函数示意图：由数据驱动的 SVG 绘图模块。

每个 lesson 的 diagram 字段是一个 dict：
    xr / yr   坐标范围
    curves    [{f: lambda, color, dash, width}]   曲线
    dots      [{x, y, label, color, pos}]         标记点
    vlines    [{x, label, color}]                 竖直虚线（对称轴等）
    hlines    [{y, label, color}]                 水平虚线
    spans     [{a, b, color, label}]              x 轴上的区间色带
    regions   [{a, b, kind}]                      数轴正负区间标记
    texts     [{x, y, s, color}]                  自由文字
    note      图下方说明
"""

FONT = "Microsoft YaHei, PingFang SC, sans-serif"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class Plot:
    def __init__(self, cfg):
        self.w = cfg.get("w", 660)
        self.h = cfg.get("h", 360)
        self.m = cfg.get("m", 48)
        self.x0, self.x1 = cfg.get("xr", (-5, 5))
        self.y0, self.y1 = cfg.get("yr", (-4, 6))
        self.parts = []
        self.show_y = cfg.get("yaxis", True)
        self.show_grid = cfg.get("grid", True)
        self.step = cfg.get("step", 1)

    # ---------- 坐标变换 ----------
    def px(self, x):
        return self.m + (x - self.x0) / (self.x1 - self.x0) * (self.w - 2 * self.m)

    def py(self, y):
        return self.h - self.m - (y - self.y0) / (self.y1 - self.y0) * (self.h - 2 * self.m)

    # ---------- 基础元素 ----------
    def grid(self):
        if not self.show_grid:
            return self
        x = self.x0
        while x <= self.x1 + 1e-9:
            self.parts.append(
                '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#edf1f7" stroke-width="1"/>'
                % (self.px(x), self.py(self.y1), self.px(x), self.py(self.y0)))
            x += self.step
        y = self.y0
        while y <= self.y1 + 1e-9:
            self.parts.append(
                '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#edf1f7" stroke-width="1"/>'
                % (self.px(self.x0), self.py(y), self.px(self.x1), self.py(y)))
            y += self.step
        return self

    def axes(self, xlabel="x", ylabel="y"):
        y0pix = min(max(self.py(0), 8), self.h - 8)
        x0pix = min(max(self.px(0), 8), self.w - 8)
        self.parts.append(
            '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#64748b" stroke-width="1.6"/>'
            % (self.m - 10, y0pix, self.w - self.m + 14, y0pix))
        self.parts.append('<path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f Z" fill="#64748b"/>'
                          % (self.w - self.m + 14, y0pix, self.w - self.m + 22, y0pix - 4.5,
                             self.w - self.m + 22, y0pix + 4.5))
        if self.show_y:
            self.parts.append(
                '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#64748b" stroke-width="1.6"/>'
                % (x0pix, self.h - self.m + 10, x0pix, self.m - 14))
            self.parts.append('<path d="M %.1f %d L %.1f %d L %.1f %d Z" fill="#64748b"/>'
                              % (x0pix, self.m - 14, x0pix - 4.5, self.m - 22, x0pix + 4.5, self.m - 22))
        if self.show_grid:
            x = self.x0
            while x <= self.x1 + 1e-9:
                if abs(x) > 1e-9:
                    self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#94a3b8" stroke-width="1"/>'
                                      % (self.px(x), y0pix - 4, self.px(x), y0pix + 4))
                    self.parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="#64748b" text-anchor="middle" '
                                      'font-family="%s">%s</text>'
                                      % (self.px(x), y0pix + 17, FONT, _fmt(x)))
                x += self.step
            if self.show_y:
                y = self.y0
                while y <= self.y1 + 1e-9:
                    if abs(y) > 1e-9:
                        self.parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="#64748b" text-anchor="end" '
                                          'font-family="%s">%s</text>'
                                          % (x0pix - 7, self.py(y) + 4, FONT, _fmt(y)))
                    y += self.step
        self.parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="#64748b" font-family="%s">%s</text>'
                          % (x0pix + 7, y0pix + 16, FONT, "O"))
        if xlabel:
            self.parts.append('<text x="%d" y="%.1f" font-size="12" fill="#475569" font-family="%s">%s</text>'
                              % (self.w - self.m + 8, y0pix - 8, FONT, xlabel))
        if ylabel and self.show_y:
            self.parts.append('<text x="%.1f" y="%d" font-size="12" fill="#475569" font-family="%s">%s</text>'
                              % (x0pix + 8, self.m - 20, FONT, ylabel))
        return self

    # ---------- 曲线 ----------
    def curve(self, f, color="#1d4ed8", width=2.4, dash=None):
        n = 480
        segs, cur = [], []
        for i in range(n + 1):
            x = self.x0 + (self.x1 - self.x0) * i / n
            try:
                y = f(x)
            except Exception:
                cur = []
                continue
            
            pad = (self.y1 - self.y0) * 0.08
            if y < self.y0 - pad or y > self.y1 + pad:
                if len(cur) > 1:
                    segs.append(cur)
                cur = []
                continue
            cur.append((self.px(x), self.py(y)))
        if len(cur) > 1:
            segs.append(cur)
        d = " ".join("M " + " L ".join("%.1f %.1f" % p for p in s) for s in segs)
        if not d:
            return self
        dash_attr = ' stroke-dasharray="%s"' % dash if dash else ""
        self.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f"%s stroke-linejoin="round"/>'
                          % (d, color, width, dash_attr))
        return self

    # ---------- 点 ----------
    def dot(self, x, y, label=None, color="#dc2626", pos="top", hollow=False):
        px, py = self.px(x), self.py(y)
        fill = "#ffffff" if hollow else color
        self.parts.append('<circle cx="%.1f" cy="%.1f" r="4.2" fill="%s" stroke="%s" stroke-width="2"/>'
                          % (px, py, fill, color))
        if label:
            off = {"top": -12, "bottom": 20, "right": 6, "left": -6}
            anchor = "middle" if pos in ("top", "bottom") else ("start" if pos == "right" else "end")
            dy = off.get(pos, -12)
            dx = 0 if pos in ("top", "bottom") else (8 if pos == "right" else -8)
            y_anchor = py + dy
            # 白色描边提升可读性
            self.parts.append('<text x="%.1f" y="%.1f" font-size="12.5" font-weight="600" fill="%s" '
                              'text-anchor="%s" font-family="%s" stroke="#ffffff" stroke-width="3.5" '
                              'paint-order="stroke">%s</text>'
                              % (px + dx, y_anchor, color, anchor, FONT, esc(label)))
            self.parts.append('<text x="%.1f" y="%.1f" font-size="12.5" font-weight="600" fill="%s" '
                              'text-anchor="%s" font-family="%s">%s</text>'
                              % (px + dx, y_anchor, color, anchor, FONT, esc(label)))
        return self

    # ---------- 辅助线 ----------
    def vline(self, x, label=None, color="#94a3b8", dash="5 4"):
        self.parts.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.3" '
                          'stroke-dasharray="%s"/>'
                          % (self.px(x), self.m - 12, self.px(x), self.h - self.m + 6, color, dash))
        if label:
            y0pix = min(max(self.py(0), 8), self.h - 8)
            self.parts.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="%s" text-anchor="middle" '
                              'font-family="%s" stroke="#ffffff" stroke-width="3" paint-order="stroke">%s</text>'
                              % (self.px(x), self.m - 16, color, FONT, esc(label)))
            self.parts.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="%s" text-anchor="middle" '
                              'font-family="%s">%s</text>'
                              % (self.px(x), self.m - 16, color, FONT, esc(label)))
        return self

    def hline(self, y, label=None, color="#94a3b8", dash="5 4"):
        self.parts.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.3" '
                          'stroke-dasharray="%s"/>'
                          % (self.m - 6, self.py(y), self.w - self.m + 6, self.py(y), color, dash))
        if label:
            self.parts.append('<text x="%d" y="%.1f" font-size="11.5" fill="%s" text-anchor="start" '
                              'font-family="%s" stroke="#ffffff" stroke-width="3" paint-order="stroke">%s</text>'
                              % (self.m - 2, self.py(y) - 6, color, FONT, esc(label)))
            self.parts.append('<text x="%d" y="%.1f" font-size="11.5" fill="%s" text-anchor="start" '
                              'font-family="%s">%s</text>'
                              % (self.m - 2, self.py(y) - 6, color, FONT, esc(label)))
        return self

    def segment(self, x1, y1, x2, y2, color="#0ea5e9", dash=None, width=1.6, arrow=False):
        dash_attr = ' stroke-dasharray="%s"' % dash if dash else ""
        marker = ' marker-end="url(#arw)"' if arrow else ""
        self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"%s%s/>'
                          % (self.px(x1), self.py(y1), self.px(x2), self.py(y2), color, width, dash_attr, marker))
        return self

    def brace_span(self, a, b, y, label, color="#0ea5e9"):
        """x 轴上 [a,b] 区间的双箭头标注"""
        self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
                          % (self.px(a), self.py(y), self.px(b), self.py(y), color))
        for xx in (a, b):
            self.parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
                              % (self.px(xx), self.py(y) - 5, self.px(xx), self.py(y) + 5, color))
        mx = self.px((a + b) / 2)
        my = self.py(y) - 10
        self.parts.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s" text-anchor="middle" '
                          'font-family="%s" stroke="#ffffff" stroke-width="3.5" paint-order="stroke">%s</text>'
                          % (mx, my, color, FONT, esc(label)))
        self.parts.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="600" fill="%s" text-anchor="middle" '
                          'font-family="%s">%s</text>' % (mx, my, color, FONT, esc(label)))
        return self

    def shade(self, a, b, y_bottom, y_top, color="#38bdf8", opacity=0.13):
        self.parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity="%.2f"/>'
                          % (self.px(a), self.py(y_top), abs(self.px(b) - self.px(a)),
                             abs(self.py(y_bottom) - self.py(y_top)), color, opacity))
        return self

    def text(self, x, y, s, color="#334155", size=13, anchor="middle", weight="400"):
        self.parts.append('<text x="%.1f" y="%.1f" font-size="%.1f" fill="%s" text-anchor="%s" font-weight="%s" '
                          'font-family="%s" stroke="#ffffff" stroke-width="3.5" paint-order="stroke">%s</text>'
                          % (self.px(x), self.py(y), size, color, anchor, weight, FONT, esc(s)))
        self.parts.append('<text x="%.1f" y="%.1f" font-size="%.1f" fill="%s" text-anchor="%s" font-weight="%s" '
                          'font-family="%s">%s</text>'
                          % (self.px(x), self.py(y), size, color, anchor, weight, FONT, esc(s)))
        return self

    def band(self, a, b, color="#dc2626", opacity=0.12, height=None):
        """数轴上的粗细线条段"""
        y0pix = min(max(self.py(0), 8), self.h - 8)
        hgt = height or 5
        self.parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity="%.2f" rx="2"/>'
                          % (self.px(a), y0pix - hgt / 2, abs(self.px(b) - self.px(a)), hgt, color, opacity))
        return self

    def plus_minus(self, pts, signs, y=0.0):
        for x, s in zip(pts, signs):
            self.parts.append('<text x="%.1f" y="%.1f" font-size="15" font-weight="700" fill="%s" text-anchor="middle" '
                              'font-family="%s">%s</text>'
                              % (self.px(x), self.py(y) + 26, "#dc2626" if s > 0 else "#2563eb", FONT,
                                 "+" if s > 0 else "−"))
        return self

    # ---------- 输出 ----------
    def render(self):
        head = ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
                'style="width:100%%;height:auto;display:block">'
                '<defs><marker id="arw" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">'
                '<path d="M0,0 L8,3 L0,6 Z" fill="#0ea5e9"/></marker></defs>'
                '<rect width="%d" height="%d" fill="#ffffff"/>' % (self.w, self.h, self.w, self.h))
        return head + "".join(self.parts) + "</svg>"


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return ("%.1f" % v).rstrip("0").rstrip(".")


def threading(p, th):
    """数轴标根法（穿针引线）示意图：从右上起笔，奇穿偶不穿"""
    roots = th["roots"]
    mults = th.get("mults", [1] * len(roots))
    lead = th.get("lead", 1)
    n = len(roots)
    signs = [0] * (n + 1)
    signs[n] = 1 if lead > 0 else -1
    for i in range(n - 1, -1, -1):
        signs[i] = signs[i + 1] * (-1 if mults[i] % 2 == 1 else 1)
    amp = th.get("amp", 1.7)
    col = th.get("color", "#7c3aed")
    # 内部区间
    for i in range(1, n):
        a, b = roots[i - 1], roots[i]
        s = signs[i]
        mx = (a + b) / 2
        d = ("M %.1f %.1f Q %.1f %.1f %.1f %.1f"
             % (p.px(a), p.py(0), p.px(mx), p.py(s * 2 * amp), p.px(b), p.py(0)))
        p.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % (d, col))
    # 最右外侧
    s = signs[n]
    x_end = p.x1 - 0.25
    d = ("M %.1f %.1f C %.1f %.1f %.1f %.1f %.1f %.1f"
         % (p.px(roots[-1]), p.py(0),
            p.px(roots[-1] + 0.5), p.py(s * amp * 0.7),
            p.px(x_end - 0.6), p.py(s * amp * 1.5),
            p.px(x_end), p.py(s * amp * 1.7)))
    p.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % (d, col))
    # 最左外侧
    s = signs[0]
    x_start = p.x0 + 0.25
    d = ("M %.1f %.1f C %.1f %.1f %.1f %.1f %.1f %.1f"
         % (p.px(x_start), p.py(s * amp * 1.7),
            p.px(x_start + 0.6), p.py(s * amp * 1.5),
            p.px(roots[0] - 0.5), p.py(s * amp * 0.7),
            p.px(roots[0]), p.py(0)))
    p.parts.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % (d, col))
    # 标注奇偶
    for i, (r, m) in enumerate(zip(roots, mults)):
        if m % 2 == 0:
            p.parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" text-anchor="middle" '
                           'font-family="%s" stroke="#ffffff" stroke-width="3" paint-order="stroke">偶·弹回</text>'
                           % (p.px(r), p.py(0) + 30, col, FONT))
            p.parts.append('<text x="%.1f" y="%.1f" font-size="11" fill="%s" text-anchor="middle" '
                           'font-family="%s">偶·弹回</text>' % (p.px(r), p.py(0) + 30, col, FONT))
    return p


def draw(cfg):
    """根据 diagram 配置生成完整 SVG"""
    p = Plot(cfg)
    p.grid()
    if not cfg.get("no_axes", False):
        p.axes(cfg.get("xlabel", "x"), cfg.get("ylabel", "y"))
    for s in cfg.get("spans", []):
        p.shade(s["a"], s["b"], cfg["yr"][0], cfg["yr"][1], s.get("color", "#38bdf8"), s.get("opacity", 0.13))
    band=None
    if cfg.get("thread"):
        threading(p, cfg["thread"])
    for c in cfg.get("curves", []):
        p.curve(c["f"], c.get("color", "#1d4ed8"), c.get("width", 2.4), c.get("dash"))
    for h in cfg.get("hlines", []):
        p.hline(h["y"], h.get("label"), h.get("color", "#94a3b8"))
    for v in cfg.get("vlines", []):
        p.vline(v["x"], v.get("label"), v.get("color", "#94a3b8"))
    for s in cfg.get("seg", []):
        p.segment(s["x1"], s["y1"], s["x2"], s["y2"], s.get("color", "#0ea5e9"), s.get("dash"), s.get("width", 1.6))
    for d in cfg.get("dots", []):
        p.dot(d["x"], d["y"], d.get("label"), d.get("color", "#dc2626"), d.get("pos", "top"), d.get("hollow", False))
    for b in cfg.get("braces", []):
        p.brace_span(b["a"], b["b"], b.get("y", 0), b.get("label", ""), b.get("color", "#0ea5e9"))
    for t in cfg.get("texts", []):
        p.text(t["x"], t["y"], t["s"], t.get("color", "#334155"), t.get("size", 13), t.get("anchor", "middle"),
               t.get("weight", "400"))
    return p.render()
