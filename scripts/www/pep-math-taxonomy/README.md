# 人教版初中数学知识图谱

基于 [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) 的数据结构，覆盖**义务教育教科书·数学（人民教育出版社2022版）七至九年级全6册**的完整知识图谱。

> **169 个微知识点 · 237 条前置依赖边 · 36 个领域聚类 · 覆盖初中数学全部章节**

---

## 数据概览

| 册次 | 教材 | 知识点 | 依赖边 | 聚类 |
|------|------|-------:|-------:|-----:|
| 7-up | 七年级上册（有理数、整式、一元一次方程、几何初步） | 64 | 87 | 12 |
| 7-down | 七年级下册（整式乘除、相交平行线、三角形、数据收集） | 29 | 42 | 8 |
| 8-up | 八年级上册（三角形全等、轴对称、整式乘法、因式分解、分式） | 28 | 41 | 9 |
| 8-down | 八年级下册（二次根式、勾股定理、四边形、函数、一次函数、数据分析） | 19 | 27 | 6 |
| 9-up | 九年级上册（一元二次方程、二次函数、旋转、圆、概率初步） | 18 | 25 | 5 |
| 9-down | 九年级下册（反比例函数、相似、锐角三角函数、投影与视图） | 11 | 15 | 4 |
| **合计** | | **169** | **237** | **44** |

### 知识点类型分布

| 类型 | 说明 | 适用题型 |
|------|------|---------|
| `CONCEPTUAL` | 概念理解 | 判断辨析、举例说明 |
| `PROCEDURAL` | 程序性计算 | 计算步骤、纠错题 |
| `REPRESENTATIONAL` | 表征图示 | 画图、数形结合 |

---

## 文件结构

```
pep-math-taxonomy/
├── data/
│   ├── topics.json              ← 七年级上册（原始数据，根目录）
│   ├── dependencies.json
│   ├── clusters.json
│   ├── curriculum-standards.json
│   ├── manifest.json
│   ├── 7-down/
│   │   ├── topics.json          ← 微知识点（图的节点）
│   │   ├── dependencies.json    ← 前置依赖边（有向无环图）
│   │   ├── clusters.json        ← 领域聚类摘要
│   │   ├── curriculum-standards.json  ← 课标对齐
│   │   └── manifest.json        ← 统计元数据
│   ├── 8-up/  8-down/  9-up/  9-down/   ← 同上
├── skills/
│   └── math-tutor/
│       └── SKILL.md             ← Claude Code 辅导 Skill（见下方）
├── schema/                      ← JSON Schema（来自 os-taxonomy）
└── visualization.html           ← 交互式知识图谱可视化
```

### 每册 5 个文件说明

| 文件 | 内容 |
|------|------|
| `topics.json` | 所有微知识点，含 id、name、type、domain、description、evidence、assessmentPrompt |
| `dependencies.json` | 前置依赖边，含 topicId、prerequisiteId、strength（hard/soft）、reason |
| `clusters.json` | 按领域分组的摘要，面向家长/学生说明每个领域的学习意义 |
| `curriculum-standards.json` | 对齐 2022 年版义务教育数学课程标准 |
| `manifest.json` | 各文件统计数据（知识点数、依赖数、章节分布、类型分布） |

---

## 数据结构示例

### topic（知识点节点）

```json
{
  "id": "mt_ch8_003",
  "type": "CONCEPTUAL",
  "subject": "Mathematics",
  "domain": "实数",
  "name": "无理数与实数的概念",
  "description": "无限不循环小数叫做无理数。有理数和无理数统称为实数。实数与数轴上的点一一对应。",
  "ageRangeStart": 12,
  "ageRangeEnd": 13,
  "centrality": 0.9,
  "evidence": [
    "能判断一个数是有理数还是无理数",
    "能在数轴上表示实数",
    "能对实数进行分类"
  ],
  "assessmentPrompt": "{{name}}能说出 √2、π、0.1010010001... 为什么是无理数吗？",
  "standards": ["pep-math-2022:7下.8.3"]
}
```

### dependency（依赖边）

```json
{
  "topicId": "mt_ch8_003",
  "prerequisiteId": "mt_ch1_003",
  "strength": "hard",
  "reason": "实数是有理数的扩展，需先掌握有理数分类"
}
```

---

## 使用方式

```js
import topics from './data/7-down/topics.json' with { type: 'json' };
import deps   from './data/7-down/dependencies.json' with { type: 'json' };

const byId = new Map(topics.topics.map(t => [t.id, t]));

// 查找某知识点的所有前置
const prereqs = deps.dependencies
  .filter(d => d.topicId === 'mt_ch8_003')
  .map(d => byId.get(d.prerequisiteId)?.name);
// => ["算术平方根与平方根", "有理数的概念"]

// 查找某知识点解锁的所有后续
const unlocks = deps.dependencies
  .filter(d => d.prerequisiteId === 'mt_ch8_003')
  .map(d => byId.get(d.topicId)?.name);
// => ["实数的运算"]
```

```python
import json

topics = json.load(open('data/7-down/topics.json'))['topics']
deps   = json.load(open('data/7-down/dependencies.json'))['dependencies']

by_id = {t['id']: t for t in topics}

# DAG 拓扑排序（学习路径）
from collections import defaultdict, deque
graph = defaultdict(list)
in_degree = defaultdict(int)
for d in deps:
    if d['prerequisiteId'] in by_id and d['topicId'] in by_id:
        graph[d['prerequisiteId']].append(d['topicId'])
        in_degree[d['topicId']] += 1

queue = deque(t['id'] for t in topics if in_degree[t['id']] == 0)
order = []
while queue:
    node = queue.popleft()
    order.append(by_id[node]['name'])
    for nxt in graph[node]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)

print('\n'.join(f'{i+1}. {n}' for i, n in enumerate(order)))
```

---

## Claude Code Skill：math-tutor

本仓库附带一个 [Claude Code](https://claude.ai/code) Skill，直接基于知识图谱实现**初中数学自适应辅导**，无需额外配置。

### 安装

将 `skills/math-tutor/SKILL.md` 放入你的 Claude Code 项目的 `.claude/skills/math-tutor/` 目录。

### 4 个辅导模式

#### `/math-tutor diagnose` — 错题诊断

输入错题描述，自动：
1. 映射到对应知识点（topics.json 语义匹配）
2. 沿 dependencies DAG 向前追溯，找到最底层未掌握的根因
3. 输出薄弱链报告 + 建议补强顺序

```
示例输入：「无限不循环小数是有理数」（判断题，答错）

输出：
🔴 根因：有理数的概念（mt_ch1_003，七上）
  ↓
🟡 无理数与实数的概念（mt_ch8_003，七下）← 直接出错点
建议：先回看有理数定义，再理解无理数引入过程
```

#### `/math-tutor generate` — 自适应出题

根据诊断结果或指定知识点，按类型出对应题型：

| 知识点类型 | 出题类型 |
|-----------|---------|
| CONCEPTUAL | 判断题、概念辨析、举例题 |
| PROCEDURAL | 计算步骤题、纠错题、填空 |
| REPRESENTATIONAL | 画图题、数形结合题 |

4 档难度：**夯基**（前置知识）→ **目标**（本知识点）→ **综合**（跨知识点）→ **挑战**（下游知识点）

#### `/math-tutor learn` — 自学引导

生成拓扑排序的学习路径，支持 5 种内容形式：

- **思维导图**（Mermaid 格式，展示前置/核心/后续/易错点）
- **视频脚本**（3-5分钟，含生活引入 + 例题演示 + 口诀总结）
- **故事化讲解**（将抽象概念包装进情境，适合低年级或数学焦虑学生）
- **费曼笔记**（不用术语的一句话定义 + 生活类比 + 类比边界）
- **刷题清单**（答对升级、答错回退的自适应练习序列）

#### `/math-tutor build` — 图谱扩展

从教材 PDF 目录生成新的知识图谱数据，输出符合本仓库 schema 的 JSON 文件，可直接 push。

### 典型使用闭环

```
输入错题
  → diagnose（定位根因）
  → learn（选一种形式补强）
  → generate（夯基题验证）
  → diagnose（确认掌握）
```

---

## 覆盖知识点（按册）

<details>
<summary>七年级上册（64 个知识点）</summary>

**第1章 有理数**（24）：正负数、有理数概念与分类、数轴、相反数、绝对值、有理数大小比较、加减法、乘除法、乘方、混合运算、科学记数法

**第2章 整式的加减**（10）：用字母表示数、单项式、多项式、同类项、合并同类项、去括号、整式加减

**第3章 一元一次方程**（13）：方程概念、等式性质、移项合并、去括号去分母解方程、一元一次方程应用

**第4章 几何图形初步**（17）：立体图形与平面图形、三视图、展开图、点线面体、直线射线线段、角的概念与度量、余角补角、角平分线

</details>

<details>
<summary>七年级下册（29 个知识点）</summary>

**第5章 相交线与平行线**：对顶角、垂线、同位角、内错角、平行线判定与性质、平移

**第6章 平面直角坐标系**：坐标系概念、点的坐标读写、象限与坐标轴

**第7章 三角形**：三角形概念、三边关系、角平分线中线高、外角定理、多边形内角和、全等三角形

**第8章 二次根式预备**：平方根、立方根、无理数与实数、实数运算

**统计（第12章）**：数据收集、频率直方图、抽样调查

</details>

<details>
<summary>八年级上册（28 个知识点）</summary>

**第13章 三角形**：全等三角形判定（SSS/SAS/ASA/AAS/HL）

**第14章 轴对称**：轴对称图形、线段垂直平分线、角平分线性质、等腰三角形

**第15章 整式乘法**：同底数幂乘法、幂的乘方、积的乘方、多项式乘法、平方差公式、完全平方公式

**第16章 因式分解**：提公因式法、公式法（平方差、完全平方）

**第17章 分式**：分式概念与基本性质、四则运算、分式方程

</details>

<details>
<summary>八年级下册（19 个知识点）</summary>

**第19章 二次根式**：概念与性质、乘除运算与化简、加减运算

**第20章 勾股定理**：正定理、逆定理

**第21章 四边形**：多边形内角和、平行四边形、矩形、菱形、正方形

**第22-23章 函数**：函数概念与三种表示、一次函数图象与性质、函数与方程不等式的关系

**第24章 数据分析**：平均数中位数众数、方差与标准差、四分位数

</details>

<details>
<summary>九年级上册（18 个知识点）</summary>

**第21章 一元二次方程**：概念、配方法、公式法（判别式Δ）、因式分解法、应用

**第22章 二次函数**：y=ax²、平移变换与顶点式、一般式配方、与一元二次方程的关系

**第23章 旋转**：旋转变换性质、中心对称与中心对称图形

**第24章 圆**：垂径定理、弧弦圆心角关系、圆周角定理、切线判定与性质、弧长扇形面积

**第25章 概率初步**：随机事件与概率、列表法与树状图、频率估计概率

</details>

<details>
<summary>九年级下册（11 个知识点）</summary>

**第26章 反比例函数**：概念、图象与性质（双曲线）、应用

**第27章 相似**：相似图形概念、相似三角形判定（AA/SAS/SSS）、性质（面积比=相似比²）、位似变换

**第28章 锐角三角函数**：sin/cos/tan定义、特殊角值、解直角三角形、仰俯角应用

**第29章 投影与视图**：平行投影与中心投影、三视图画法与识读

</details>

---

## License

数据结构遵循 [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) 的 ODbL 1.0 协议（数据库结构）和 CC BY-SA 4.0（内容）。

知识点内容基于人教版教材整理，仅供学习研究使用。
