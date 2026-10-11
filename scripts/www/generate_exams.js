/* eslint-disable */
/**
 * 生成 14 套综合测试卷（exam01.html ~ exam14.html）
 * 题库来源：各 day*.html 中的 const choiceQuestions 数组
 * 每套随机抽取 20 题（单选/多选），每题 5 分，满分 100 分
 */
const fs = require('fs');
const path = require('path');

const DIR = 'd:/365培训';
const EXAM_COUNT = 14;
const PER_PAPER = 20;
const POINTS = 5; // 每题分值
const LETTERS = 'ABCDEFGH';

/* ---------- 1. 从 day*.html 提取题库 ---------- */
function stripQNum(t) {
  return String(t).replace(/^\s*\d+\s*[\.、．\)）]\s*/, '').replace(/[（(]\s*多选\s*[)）]\s*$/, '').trim();
}
function stripOptPrefix(t) {
  return String(t).replace(/^\s*[A-DＡ-Ｄ]\s*[\.、．\)）]\s*/, '').trim();
}

function extractPool() {
  const files = fs.readdirSync(DIR).filter(f => /^day\d{3}\.html$/.test(f)).sort();
  const pool = [];
  let failed = [];
  for (const f of files) {
    const html = fs.readFileSync(path.join(DIR, f), 'utf8');
    const dayNum = parseInt(f.match(/(\d{3})/)[1], 10);

    // 题面（仅选择题区的 question-text）
    const texts = [];
    const reText = /<div class="choice-question">[\s\S]*?<div class="question-text">([\s\S]*?)<\/div>/g;
    let mt;
    while ((mt = reText.exec(html)) !== null) texts.push(mt[1].replace(/<[^>]+>/g, '').trim());

    // 选项/答案数据
    const mArr = html.match(/const choiceQuestions\s*=\s*\[([\s\S]*?)\n\s*\];/);
    if (!mArr) { failed.push(f); continue; }
    let arr;
    try { arr = eval('[' + mArr[1] + ']'); } catch (e) { failed.push(f + '(eval)'); continue; }
    if (!Array.isArray(arr) || arr.length === 0) { failed.push(f + '(empty)'); continue; }

    arr.forEach((q, i) => {
      if (!q || !Array.isArray(q.options) || !Array.isArray(q.answer)) return;
      if (q.options.length < 2 || q.answer.length === 0) return;
      const text = texts[i] ? stripQNum(texts[i]) : '';
      if (!text) return; // 无题面则跳过
      pool.push({
        src: dayNum,
        type: q.type === 'multi' ? 'multi' : 'single',
        text,
        options: q.options.map(o => stripOptPrefix(o.text)),
        answer: q.answer.slice().sort((a, b) => a - b),
        score: POINTS,
        explanation: (q.explanation || '').trim()
      });
    });
  }
  return { pool, failed };
}

/* ---------- 2. 洗牌 + 分发（各套题目互不重复） ---------- */
function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ---------- 3. 试卷 HTML 模板 ---------- */
function buildExamHTML(no, questions) {
  const dataJSON = JSON.stringify(questions).replace(/<\//g, '<\\/');
  const max = questions.reduce((s, q) => s + q.score, 0);
  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>第${no}套 | 365天培训综合测试卷</title>
    <link rel="stylesheet" href="training-styles.css">
    <style>
        .exam-info { margin-bottom: 4px; }
        .exam-info p { margin-bottom: 10px; }
        .exam-badge {
            display: inline-block; margin: 8px 6px 0 0; padding: 4px 12px;
            background: #E6F0FF; color: #1677FF; border: 1px solid #D6E4FF;
            border-radius: 20px; font-size: 13px;
        }
        .score-display .score-text { white-space: pre-line; line-height: 1.7; }
        .reset-btn {
            display: inline-block; margin-left: 10px; padding: 10px 22px;
            background: #F5F5F5; color: #666; border: 1px solid #E0E0E0;
            border-radius: 10px; font-size: 15px; cursor: pointer;
            font-family: var(--font-family);
        }
        .reset-btn:hover { background: #EEE; }
    </style>
</head>
<body>
    <div class="container">
        <div class="page-header">
            <div class="day-number">模拟测试 · 第 ${no} 套</div>
            <h1 class="page-title">365天培训综合测试卷（第${no}套）</h1>
            <div class="page-subtitle">共 ${questions.length} 题 · 每题 ${POINTS} 分 · 满分 ${max} 分</div>
        </div>

        <div class="learning-card">
            <div class="card-header">
                <div class="card-icon">📝</div>
                <div class="card-title">考试说明</div>
            </div>
            <div class="learning-section exam-info">
                <p>1. 本试卷共 <strong>${questions.length}</strong> 道选择题（含单选、多选），每题 <strong>${POINTS}</strong> 分，满分 <strong>${max}</strong> 分。</p>
                <p>2. <strong>多选题</strong>须全部选对才得分，多选、少选、错选均不得分。</p>
                <p>3. 题目从 365 天课程题库中随机抽取，各套试卷题目互不重复。</p>
                <p>4. 作答完成后点击下方「📝 提交答案并评分」，系统自动评分并给出答题解析。</p>
                <div>
                    <span class="exam-badge">📚 题库总量 1000+ 题</span>
                    <span class="exam-badge">🎯 满分 ${max} 分</span>
                    <span class="exam-badge">⏱ 建议用时 20 分钟</span>
                </div>
            </div>
        </div>

        <div class="practice-section">
            <div class="section-title">试 题</div>
            <div id="questionArea"></div>

            <div class="submit-area">
                <button class="submit-btn" onclick="submitExam()">📝 提交答案并评分</button>
                <button class="reset-btn" onclick="location.reload()">🔄 重新作答</button>
            </div>

            <div class="score-display" id="scoreDisplay">
                <div class="score-number" id="scoreNumber">0/${max}分</div>
                <div class="score-text" id="scoreText">本次测试成绩</div>
            </div>
        </div>

        <div class="nav-bottom">
            <a href="index.html" class="nav-home">🏠 返回首页</a>
        </div>
    </div>

    <div class="footer-support">
        技术支持：闫胜君视光工作室
    </div>

    <script>
        // ========== 本套试卷题目数据（随机抽取） ==========
        const examData = ${dataJSON};
        const LETTERS = '${LETTERS}';

        // ========== 渲染试题 ==========
        function renderExam() {
            const area = document.getElementById('questionArea');
            examData.forEach((q, qi) => {
                const box = document.createElement('div');
                box.className = 'choice-question';

                const qt = document.createElement('div');
                qt.className = 'question-text';
                qt.textContent = (qi + 1) + '. ' + q.text + (q.type === 'multi' ? '（多选）' : '');
                box.appendChild(qt);

                const meta = document.createElement('div');
                meta.className = 'question-meta';
                meta.textContent = (q.type === 'multi' ? '多选题' : '单选题') + ' · ' + q.score + '分';
                box.appendChild(meta);

                const ul = document.createElement('ul');
                ul.className = 'options-list';
                q.options.forEach((opt, oi) => {
                    const li = document.createElement('li');
                    li.className = 'option-item';
                    const mk = document.createElement('div');
                    mk.className = 'option-marker';
                    mk.textContent = LETTERS[oi];
                    const tx = document.createElement('span');
                    tx.className = 'option-text';
                    tx.textContent = opt;
                    li.appendChild(mk);
                    li.appendChild(tx);
                    li.addEventListener('click', () => toggleOption(qi, oi, q.type === 'multi'));
                    ul.appendChild(li);
                });
                box.appendChild(ul);

                const fb = document.createElement('div');
                fb.className = 'feedback';
                box.appendChild(fb);

                area.appendChild(box);
            });
        }

        function toggleOption(qi, oi, isMulti) {
            const box = document.querySelectorAll('.choice-question')[qi];
            const items = box.querySelectorAll('.option-item');
            const item = items[oi];
            if (isMulti) {
                item.classList.toggle('selected');
            } else {
                items.forEach(li => li.classList.remove('selected'));
                item.classList.add('selected');
            }
        }

        function getSelected(qi) {
            const box = document.querySelectorAll('.choice-question')[qi];
            const items = box.querySelectorAll('.option-item');
            const sel = [];
            items.forEach((li, i) => { if (li.classList.contains('selected')) sel.push(i); });
            return sel.sort((a, b) => a - b);
        }

        // ========== 自动评分 ==========
        function submitExam() {
            let total = 0, correctCount = 0, answered = 0;
            examData.forEach((q, qi) => {
                const box = document.querySelectorAll('.choice-question')[qi];
                const items = box.querySelectorAll('.option-item');
                const sel = getSelected(qi);
                if (sel.length) answered++;
                const corr = q.answer.slice().sort((a, b) => a - b);
                const ok = JSON.stringify(sel) === JSON.stringify(corr);

                items.forEach(li => li.classList.remove('correct', 'wrong'));
                const fb = box.querySelector('.feedback');
                fb.classList.remove('show', 'correct-feedback', 'wrong-feedback');
                items.forEach((li, oi) => {
                    if (corr.includes(oi)) li.classList.add('correct');
                    if (sel.includes(oi) && !corr.includes(oi)) li.classList.add('wrong');
                });

                if (ok) {
                    total += q.score;
                    correctCount++;
                    fb.classList.add('correct-feedback', 'show');
                    fb.innerHTML = '✅ 回答正确！' + (q.explanation || '') + '  <em>（出自第' + q.src + '天）</em>';
                } else {
                    const letters = corr.map(i => LETTERS[i]).join('、');
                    fb.classList.add('wrong-feedback', 'show');
                    fb.innerHTML = '❌ 回答错误。正确答案：<strong>' + letters + '</strong>。' + (q.explanation || '') + '  <em>（出自第' + q.src + '天）</em>';
                }
            });

            const max = examData.reduce((s, q) => s + q.score, 0);
            const pct = Math.round(total / max * 100);
            let result, tip;
            if (pct >= 90) { result = '🏆 优秀！知识掌握非常扎实'; }
            else if (pct >= 80) { result = '👍 良好，继续巩固即可'; }
            else if (pct >= 60) { result = '✅ 合格，请重点复习错题'; }
            else { result = '⚠️ 不合格，建议回看相关课程后重新测试'; }
            tip = (answered < examData.length ? '（有 ' + (examData.length - answered) + ' 题未作答）' : '（已全部作答）');

            document.getElementById('scoreNumber').textContent = total + '/' + max + '分';
            document.getElementById('scoreText').innerHTML =
                result + '\\n答对 ' + correctCount + '/' + examData.length + ' 题 · 正确率 ' + pct + '% ' + tip;

            const disp = document.getElementById('scoreDisplay');
            disp.classList.add('show');
            disp.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        window.addEventListener('DOMContentLoaded', renderExam);
    </script>
</body>
</html>
`;
}

/* ---------- 4. 主流程 ---------- */
function main() {
  const { pool, failed } = extractPool();
  console.log('[INFO] pool size =', pool.length, '| skipped files =', failed.length, '(', failed.join(', '), ')');

  const need = EXAM_COUNT * PER_PAPER;
  if (pool.length < need) throw new Error('题库不足：需要 ' + need + '，实际 ' + pool.length);

  const shuffled = shuffle(pool.slice());
  const papers = [];
  for (let i = 0; i < EXAM_COUNT; i++) {
    papers.push(shuffled.slice(i * PER_PAPER, (i + 1) * PER_PAPER));
  }

  papers.forEach((qs, i) => {
    const no = i + 1;
    const name = 'exam' + String(no).padStart(2, '0') + '.html';
    fs.writeFileSync(path.join(DIR, name), buildExamHTML(no, qs), 'utf8');
    console.log('[OK]', name, '->', qs.length, 'questions');
  });

  console.log('[DONE] generated', EXAM_COUNT, 'papers,', need, 'questions total.');
}
main();
