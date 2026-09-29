# -*- coding: utf-8 -*-
"""扫描练习题数据字段完整性：answer / score 是否缺失，以及 correct 标记与 answer 是否冲突"""
import re, glob

files = sorted(glob.glob('day*.html'))
missing_answer, missing_score, conflict = [], [], []
for f in files:
    s = open(f, encoding='utf-8').read()
    # 取出 choiceQuestions 数组整体
    m = re.search(r'const choiceQuestions = (\[.*?\n        \]);', s, re.S)
    if not m:
        m = re.search(r'const choiceQuestions = (\[.*?\]);', s, re.S)
    if not m:
        continue
    block = m.group(1)
    n_q = len(re.findall(r"type:\s*['\"](single|multi)['\"]", block))
    n_ans = len(re.findall(r'answer:\s*\[', block))
    n_score = len(re.findall(r'score:\s*\d+', block))
    if n_q and n_ans < n_q:
        missing_answer.append((f, n_q, n_ans))
    if n_q and n_score < n_q:
        missing_score.append((f, n_q, n_score))
    # correct 标记与 answer 冲突检测
    if 'correct: true' in block and n_ans == n_q:
        qs = re.split(r"type:\s*['\"](?:single|multi)['\"]", block)[1:]
        for i, q in enumerate(qs):
            am = re.search(r'answer:\s*\[([^\]]*)\]', q)
            if not am:
                continue
            idxs = [int(x) for x in re.findall(r'\d+', am.group(1))]
            texts = re.findall(r"text:\s*['\"](.*?)['\"]\s*,\s*correct:", q)
            if not texts:
                texts = re.findall(r"text:\s*['\"](.*?)['\"]", q)
            t_idx = [j for j, t in enumerate(texts) if re.search(r'text:\s*[\'"].*?[\'"]\s*,\s*correct:\s*true', q) and j == j and re.match(r'\s*' + re.escape(t), '') is not None]
            # 精确匹配：逐条判断
            opt_matches = re.findall(r"\{\s*text:\s*['\"](.*?)['\"],\s*correct:\s*(true|false)\s*\}", q)
            if opt_matches:
                marked = [j for j, (_, c) in enumerate(opt_matches) if c == 'true']
                if marked != idxs:
                    conflict.append((f, i + 1, 'answer=' + str(idxs), 'marked=' + str(marked)))

print('=== 缺少 answer 字段（提交判分会报错） ===', len(missing_answer))
for x in missing_answer: print('  ', x)
print('=== 缺少 score 字段 ===', len(missing_score))
for x in missing_score: print('  ', x)
print('=== correct 标记与 answer 不一致 ===', len(conflict))
for x in conflict[:30]: print('  ', x)
