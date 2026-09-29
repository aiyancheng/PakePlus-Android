# -*- coding: utf-8 -*-
"""
适配红米 12.1 寸平板：横屏 1280x800 / 竖屏 800x1280
- training-styles.css: 新增 769-1023px 竖屏平板断点；重写 >=1024px 横屏断点；追加通用加固
- index.html: 新增 769-1023px 竖屏平板断点
"""
import re
import shutil
import os

CSS = 'training-styles.css'
IDX = 'index.html'


def block_range(src, start_idx):
    """给定起始下标，返回 (start, end) 完整大括号块"""
    d = 0
    k = src.find('{', start_idx)
    i = k
    while k < len(src):
        if src[k] == '{':
            d += 1
        elif src[k] == '}':
            d -= 1
            if d == 0:
                return i, k + 1
        k += 1
    return None


PORTRAIT_CSS = """/* ===== 平板竖屏：红米12.1寸竖屏 800x1280 等（769px - 1023px） ===== */
@media (min-width: 769px) and (max-width: 1023px) {
    .container {
        max-width: 100%;
        padding: 26px 28px 110px;
    }

    body {
        font-size: 17px;
        line-height: 1.95;
    }

    .top-bar {
        padding: 16px 24px 20px;
    }

    .top-bar .day-badge {
        font-size: 15px;
        padding: 4px 16px;
    }

    .page-header {
        margin-bottom: 28px;
        padding: 28px 0 22px;
    }

    .page-header .page-title {
        font-size: 25px;
        margin: 10px 0 6px;
    }

    .page-header .page-subtitle {
        font-size: 15px;
    }

    .learning-card, .practice-section {
        padding: 30px 32px;
        border-radius: 18px;
    }

    .learning-card .card-title {
        font-size: 20px;
    }

    .practice-section .section-title {
        font-size: 20px;
    }

    .learning-section h3 {
        font-size: 18px;
        margin: 28px 0 16px;
    }

    .learning-section p {
        font-size: 16.5px;
        line-height: 2.0;
        margin-bottom: 15px;
    }

    .learning-section li {
        font-size: 16.5px;
        line-height: 2.0;
        margin-bottom: 10px;
    }

    .learning-section .tip-box,
    .learning-section .warn-box {
        font-size: 15.5px;
        line-height: 1.9;
        padding: 18px 22px;
    }

    .choice-question, .essay-question {
        padding: 22px 26px;
        margin-bottom: 20px;
    }

    .choice-question .question-text,
    .essay-question .question-text {
        font-size: 17px;
        line-height: 1.9;
    }

    .choice-question .option-item {
        padding: 14px 18px;
        font-size: 16.5px;
        margin-bottom: 10px;
        min-height: 50px;
    }

    .choice-question .option-marker {
        width: 25px;
        height: 25px;
        font-size: 13px;
    }

    .essay-question textarea {
        font-size: 16.5px;
        min-height: 100px;
        line-height: 1.9;
    }

    .essay-question .answer-btn {
        font-size: 15px;
        padding: 11px 24px;
        min-height: 44px;
    }

    .essay-question .reference-answer {
        font-size: 15.5px;
        line-height: 1.9;
    }

    .submit-btn {
        padding: 16px 54px;
        font-size: 17px;
        min-height: 52px;
    }

    .nav-bottom {
        padding: 22px 0;
    }

    .nav-top .nav-arrow,
    .nav-top .nav-home,
    .nav-bottom .nav-arrow,
    .nav-bottom .nav-home {
        padding: 12px 26px;
        font-size: 15px;
        min-height: 46px;
        display: inline-flex;
        align-items: center;
    }

    .footer-support {
        padding: 24px 16px 40px;
        font-size: 14px;
    }

    .summary-card {
        padding: 24px 28px;
    }

    .summary-card li {
        font-size: 15.5px;
        margin-bottom: 10px;
    }

    /* 表格内联字号偏小，平板上统一放大并允许换行 */
    .comparison-table th,
    .comparison-table td {
        font-size: 15.5px !important;
        padding: 10px 14px !important;
        word-break: break-word;
    }
}

"""

LANDSCAPE_CSS = """/* ===== 平板横屏：红米12.1寸横屏 1280x800 等（>=1024px） ===== */
@media (min-width: 1024px) {
    .container {
        max-width: 1100px;
        padding: 30px 40px 120px;
    }

    body {
        font-size: 18px;
        line-height: 2.0;
    }

    .page-header {
        margin-bottom: 30px;
        padding: 30px 0 22px;
    }

    .page-header .page-title {
        font-size: 26px;
        margin: 10px 0 6px;
    }

    .page-header .page-subtitle {
        font-size: 16px;
    }

    .learning-card, .practice-section {
        padding: 36px 44px;
        border-radius: 20px;
    }

    .learning-card .card-title {
        font-size: 21px;
    }

    .practice-section .section-title {
        font-size: 21px;
    }

    .learning-section h3 {
        font-size: 19px;
        margin: 30px 0 18px;
    }

    .learning-section p {
        font-size: 17.5px;
        line-height: 2.05;
        margin-bottom: 16px;
    }

    .learning-section li {
        font-size: 17.5px;
        line-height: 2.0;
        margin-bottom: 10px;
    }

    .learning-section .tip-box,
    .learning-section .warn-box {
        font-size: 16px;
        line-height: 1.95;
        padding: 18px 24px;
    }

    .choice-question, .essay-question {
        padding: 24px 30px;
        margin-bottom: 22px;
    }

    .choice-question .question-text,
    .essay-question .question-text {
        font-size: 18px;
        line-height: 1.9;
    }

    .choice-question .option-item {
        padding: 15px 20px;
        font-size: 17px;
        margin-bottom: 12px;
        min-height: 52px;
    }

    .choice-question .option-marker {
        width: 26px;
        height: 26px;
        font-size: 14px;
    }

    .essay-question textarea {
        font-size: 17px;
        min-height: 110px;
        line-height: 1.9;
    }

    .essay-question .answer-btn {
        font-size: 15px;
        padding: 11px 26px;
        min-height: 44px;
    }

    .essay-question .reference-answer {
        font-size: 16px;
        line-height: 1.95;
    }

    .submit-btn {
        padding: 18px 64px;
        font-size: 18px;
        min-height: 56px;
    }

    .nav-bottom {
        padding: 24px 0;
    }

    .nav-top .nav-arrow,
    .nav-top .nav-home,
    .nav-bottom .nav-arrow,
    .nav-bottom .nav-home {
        padding: 12px 30px;
        font-size: 15px;
        min-height: 46px;
        display: inline-flex;
        align-items: center;
    }

    .footer-support {
        padding: 26px 16px 44px;
        font-size: 15px;
    }

    .summary-card {
        padding: 26px 32px;
    }

    .summary-card li {
        font-size: 16px;
        margin-bottom: 10px;
    }

    .comparison-table th,
    .comparison-table td {
        font-size: 16.5px !important;
        padding: 12px 16px !important;
        word-break: break-word;
    }
}
"""

COMMON_CSS = """

/* ============================================================
   平板通用加固：禁止横向滚动 / 触控目标尺寸 / 超宽屏收敛
   ============================================================ */
html {
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
}

body {
    overflow-x: hidden;
}

img, table, iframe, video {
    max-width: 100%;
}

p, li, td, th, .option-text, .question-text, .page-title {
    overflow-wrap: break-word;
    word-break: break-word;
}

/* 触摸设备：可点区域不小于 44px */
@media (pointer: coarse) {
    .nav-top .nav-arrow,
    .nav-top .nav-home,
    .nav-bottom .nav-arrow,
    .nav-bottom .nav-home,
    .option-item,
    .submit-btn,
    .filter-tab {
        min-height: 44px;
    }
}

/* 超大桌面：内容不过分拉长 */
@media (min-width: 1600px) {
    .container {
        max-width: 1200px;
    }
}
"""

PORTRAIT_IDX = """        /* 平板竖屏 769-1023px（红米12.1寸 800x1280） */
        @media (min-width: 769px) and (max-width: 1023px) {
            .index-container { --idx-pad: 24px; padding-bottom: 40px; }
            .index-hero { padding: 30px 24px 26px; border-radius: 0 0 22px 22px; }
            .index-hero h1 { font-size: 21px; }
            .index-hero p { font-size: 14.5px; }
            .index-hero .subtitle { font-size: 13px; }
            .search-box { padding: 13px 16px 13px 44px; font-size: 16px; }
            .filter-tab { padding: 10px 18px; font-size: 14px; min-height: 44px; display: inline-flex; align-items: center; }
            .stats-row { gap: 12px; margin: 4px 0 20px; }
            .stat-card { padding: 14px 10px; }
            .stat-card .stat-num { font-size: 21px; }
            .stat-card .stat-label { font-size: 12.5px; }
            .module-header { padding: 16px 22px; }
            .module-title { font-size: 17.5px; }
            .week-accordion { padding-left: 22px; }
            .week-header { padding: 13px 16px; }
            .week-title { font-size: 15.5px; }
            .days-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; padding: 12px 16px 16px; }
            .day-card { padding: 12px 14px; }
            .day-card .day-topic { font-size: 13.5px; }
            .index-footer { font-size: 13.5px; }
        }

"""


def patch_css():
    s = open(CSS, encoding='utf-8').read()
    if '.bak_tablet' in s:
        pass
    orig = s
    old_start = s.find('@media (min-width: 1024px)')
    if old_start < 0:
        print('[CSS] 未找到 @media (min-width: 1024px)')
        return False
    rng = block_range(s, old_start)
    if not rng:
        print('[CSS] 括号匹配失败')
        return False
    b_start, b_end = rng
    s = s[:old_start] + PORTRAIT_CSS + LANDSCAPE_CSS + s[b_end + 1:]
    s = s.rstrip('\n') + '\n' + COMMON_CSS
    open(CSS, 'w', encoding='utf-8', newline='\n').write(s)
    print('[CSS] 已写入，长度 %d -> %d' % (len(orig), len(s)))
    return True


def patch_index():
    s = open(IDX, encoding='utf-8').read()
    orig = s
    anchor = '@media (min-width: 1024px)'
    i = s.find(anchor)
    if i < 0:
        print('[IDX] 未找到 ' + anchor)
        return False
    # 回退到该行行首
    line_start = s.rfind('\n', 0, i) + 1
    s = s[:line_start] + PORTRAIT_IDX + s[line_start:]
    open(IDX, 'w', encoding='utf-8', newline='\n').write(s)
    print('[IDX] 已写入，长度 %d -> %d' % (len(orig), len(s)))
    return True


if __name__ == '__main__':
    for f in (CSS, IDX):
        bak = f + '.bak_tablet'
        if not os.path.exists(bak):
            shutil.copy2(f, bak)
            print('备份 ->', bak)
    patch_css()
    patch_index()
