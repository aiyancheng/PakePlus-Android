# -*- coding: utf-8 -*-
"""优化 index.html 首页排版：全宽英雄区 + 吸顶工具条 + 标题字号减小"""
import shutil, os

P = 'index.html'
BAK = 'index.html.bak_index_layout'
if not os.path.exists(BAK):
    shutil.copy2(P, BAK)

s = open(P, encoding='utf-8').read()

NEW_CSS = """
        /* ===== 首页专属样式 ===== */
        .index-container { --idx-pad: 20px; padding-bottom: 48px; }

        /* 顶部英雄区（全宽通栏） */
        .index-hero {
            background: linear-gradient(135deg, #1677FF 0%, #4096FF 55%, #69B1FF 100%);
            color: #fff;
            text-align: center;
            padding: 34px 20px 28px;
            border-radius: 0 0 22px 22px;
            box-shadow: 0 2px 10px rgba(22, 119, 255, 0.18);
        }
        .index-hero h1 {
            font-size: 22px;
            font-weight: 700;
            line-height: 1.4;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }
        .index-hero p {
            font-size: 14px;
            opacity: 0.9;
            line-height: 1.6;
        }
        .index-hero .subtitle {
            font-size: 12.5px;
            opacity: 0.75;
            margin-top: 4px;
        }
        .index-hero .hero-tag {
            display: inline-block;
            margin-top: 12px;
            padding: 4px 14px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.28);
            font-size: 12px;
            letter-spacing: 0.5px;
        }

        /* 吸顶工具条（搜索 + 筛选） */
        .index-toolbar {
            position: sticky;
            top: 0;
            z-index: 100;
            margin: 0 calc(var(--idx-pad) * -1);
            padding: 14px var(--idx-pad) 10px;
            background: var(--bg-page);
        }
        .search-area { margin: 0 0 10px; }
        .search-box {
            width: 100%;
            padding: 11px 16px 11px 40px;
            border: 2px solid #E8E8E8;
            border-radius: 12px;
            font-size: 15px;
            font-family: var(--font-family);
            transition: border-color 0.2s;
            background: white url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="%23999" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>') no-repeat 12px center;
            box-sizing: border-box;
        }
        .search-box:focus { outline: none; border-color: var(--primary); }

        /* 模块筛选标签 */
        .filter-tabs {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }
        .filter-tab {
            padding: 7px 14px;
            border-radius: 20px;
            border: 1px solid #E8E8E8;
            background: white;
            color: #666;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
            white-space: nowrap;
            font-family: var(--font-family);
        }
        .filter-tab:hover { border-color: var(--primary-lighter); color: var(--primary); }
        .filter-tab.active { background: var(--primary); color: white; border-color: var(--primary); }

        /* 统计区：四等分网格 */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 4px 0 18px;
        }
        .stat-card {
            background: white;
            border-radius: 12px;
            padding: 12px 8px;
            text-align: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid #F0F0F0;
        }
        .stat-card .stat-num { font-size: 20px; font-weight: 700; color: var(--primary); line-height: 1.3; }
        .stat-card .stat-label { font-size: 12px; color: var(--text-light); margin-top: 2px; }

        /* 模块手风琴 */
        .module-accordion { margin-bottom: 14px; }
        .module-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 14px 18px;
            background: linear-gradient(135deg, #1677FF 0%, #4096FF 100%);
            color: white;
            border-radius: 12px;
            cursor: pointer;
            margin-bottom: 8px;
            transition: all 0.2s;
            user-select: none;
        }
        .module-header:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(22, 119, 255, 0.3); }
        .module-header.collapsed .module-arrow { transform: rotate(-90deg); }
        .module-title { font-size: 17px; font-weight: 700; }
        .module-meta { font-size: 12.5px; opacity: 0.9; margin-top: 2px; }
        .module-arrow { font-size: 18px; transition: transform 0.3s; }

        /* 周手风琴 */
        .week-accordion { padding-left: 18px; margin-bottom: 10px; display: none; }
        .module-header:not(.collapsed) + .week-accordion { display: block; }
        .week-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 11px 14px;
            background: #F0F5FF;
            border-radius: 10px;
            cursor: pointer;
            margin-bottom: 6px;
            transition: all 0.2s;
            user-select: none;
            border: 1px solid #D6E4FF;
        }
        .week-header:hover { background: #E6F0FF; }
        .week-header.collapsed .week-arrow { transform: rotate(-90deg); }
        .week-title { font-size: 14.5px; font-weight: 600; color: #1677FF; }
        .week-meta { font-size: 12px; color: #666; }
        .week-arrow { font-size: 14px; color: #1677FF; transition: transform 0.3s; }

        /* 天数网格 */
        .days-grid {
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
            padding: 10px 14px 14px;
            display: none;
        }
        .week-header:not(.collapsed) + .days-grid { display: grid; }
        .day-card {
            background: white;
            border-radius: 10px;
            padding: 10px 12px;
            box-shadow: var(--shadow-sm);
            border: 1px solid #F0F0F0;
            text-decoration: none;
            color: var(--text-body);
            transition: all 0.2s;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .day-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); border-color: var(--primary-lighter); }
        .day-card .day-num { font-size: 12px; color: var(--primary); font-weight: 600; }
        .day-card .day-topic {
            font-size: 12.5px;
            color: var(--text-secondary);
            line-height: 1.45;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .day-card .day-week {
            font-size: 10px;
            color: var(--text-light);
            padding: 1px 6px;
            border-radius: 8px;
            background: #F5F5F5;
            align-self: flex-start;
        }
        .day-card.disabled { opacity: 0.4; pointer-events: none; }

        /* 无结果提示 */
        .no-result { text-align: center; padding: 40px 20px; color: var(--text-light); font-size: 14px; }

        /* 底部 */
        .index-footer {
            text-align: center;
            padding: 18px 16px 24px;
            color: var(--text-light);
            font-size: 12.5px;
            border-top: 1px solid #E8E8E8;
            margin-top: 8px;
        }

        /* 平板 / 大屏：首页更宽、多列展示 */
        @media (min-width: 1024px) {
            .index-container { max-width: 1040px; --idx-pad: 40px; }
            .index-hero { padding: 38px 40px 32px; border-radius: 0 0 26px 26px; }
            .index-hero h1 { font-size: 23px; }
            .days-grid { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 12px; }
        }

        /* 手机 */
        @media (max-width: 768px) {
            .index-container { --idx-pad: 10px; padding-bottom: 32px; }
            .index-hero { padding: 26px 16px 22px; border-radius: 0 0 18px 18px; }
            .index-hero h1 { font-size: 20px; }
            .index-hero p { font-size: 13px; }
            .index-hero .subtitle { font-size: 12px; }
            .days-grid { grid-template-columns: repeat(auto-fill, minmax(128px, 1fr)); gap: 8px; }
            .stats-row { gap: 8px; }
            .stat-card .stat-num { font-size: 18px; }
            .module-title { font-size: 16px; }
            .week-title { font-size: 14px; }
        }
        @media (max-width: 480px) {
            .index-container { --idx-pad: 8px; }
            .index-hero h1 { font-size: 18px; }
            .days-grid { grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); gap: 8px; }
            .stat-card .stat-num { font-size: 17px; }
            .stat-card .stat-label { font-size: 11px; }
        }
"""

NEW_BODY = """<body>
    <!-- 顶部英雄区（全宽通栏） -->
    <header class="index-hero">
        <h1>📚 365天眼镜门店员工晋级培训</h1>
        <p>每天进步一点点，打造专业门店团队</p>
        <p class="subtitle">产品知识 · 销售技巧 · 验光与视力健康 · 客户服务与沟通</p>
        <span class="hero-tag">4 大模块 · 52 周 · 365 节课程</span>
    </header>

    <div class="container index-container">
        <!-- 搜索 + 筛选（吸顶工具条） -->
        <div class="index-toolbar">
            <div class="search-area">
                <input type="text" class="search-box" id="searchInput" placeholder="搜索培训主题关键词..." oninput="filterDays()">
            </div>
            <div class="filter-tabs" id="filterTabs">
                <button class="filter-tab active" data-module="all" onclick="switchModule('all', this)">📋 全部</button>
                <button class="filter-tab" data-module="产品知识" onclick="switchModule('产品知识', this)">🔬 产品知识</button>
                <button class="filter-tab" data-module="销售技巧" onclick="switchModule('销售技巧', this)">💼 销售技巧</button>
                <button class="filter-tab" data-module="验光与视力健康" onclick="switchModule('验光与视力健康', this)">👁 验光与视力健康</button>
                <button class="filter-tab" data-module="客户服务与沟通" onclick="switchModule('客户服务与沟通', this)">🤝 客户服务与沟通</button>
            </div>
        </div>

"""

a = s.index('    <style>')
b = s.index('    </style>') + len('    </style>')
c = s.index('<body>')
d = s.index('        <!-- 统计区 -->')

s2 = s[:a] + '    <style>' + NEW_CSS + '    </style>' + s[b:c] + NEW_BODY + s[d:]
open(P, 'w', encoding='utf-8', newline='\n').write(s2)

print('OK  backup ->', BAK)
print('old size', len(s), '-> new size', len(s2))
