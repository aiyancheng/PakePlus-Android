# 人教版小学数学知识图谱

基于 [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) 的数据结构，覆盖**义务教育教科书·数学（人民教育出版社2024版）一至六年级全12册**的完整知识图谱。

> **378 个微知识点 · 502 条前置依赖边 · 覆盖小学数学全部章节**
>
> v2：基于全册 PDF 完整阅读提取（每册100-131页），知识点精确到例题级别

姊妹项目：[pep-math-taxonomy](https://github.com/Xww-coder/pep-math-taxonomy)（初中数学知识图谱）

---

## 数据概览

| 册次 | 教材 | 知识点 | 依赖边 |
|------|------|-------:|-------:|
| 1-up | 一年级上册（5以内数、6~10、立体图形、11~20、进位加法） | 30 | 28 |
| 1-down | 一年级下册（平面图形、退位减法、100以内数、加减法、人民币） | 31 | 32 |
| 2-up | 二年级上册（分类整理、表内乘除法1~9、厘米和米、位置方向） | 30 | 48 |
| 2-down | 二年级下册（时间、有余数除法、万以内数、万以内加减法） | 28 | 47 |
| 3-up | 三年级上册（观察物体、混合运算、长度质量单位、多位数乘一位数、线和角、分数初步） | 30 | 32 |
| 3-down | 三年级下册（对称平移旋转、一位数除法、长方形正方形、面积、数据整理、年月日、小数初步） | 32 | 40 |
| 4-up | 四年级上册（大数认识、面积单位、角度量、三位数乘两位数、平行四边形梯形、两位数除法、统计图） | 36 | 42 |
| 4-down | 四年级下册（四则运算、运算律、小数意义性质、三角形、小数加减、图形运动、平均数） | 35 | 45 |
| 5-up | 五年级上册（小数乘除法、位置、可能性、简易方程、多边形面积、植树问题） | 23 | 35 |
| 5-down | 五年级下册（三视图、因数倍数、长方体正方体体积、分数意义性质、旋转、分数加减、折线统计图） | 28 | 42 |
| 6-up | 六年级上册（分数乘除法、位置方向、比、圆周率圆面积、百分数、扇形统计图） | 38 | 55 |
| 6-down | 六年级下册（负数、百分数应用、圆柱圆锥体积、比例正反比例、鸽巢问题、整理复习） | 37 | 56 |
| **合计** | | **378** | **502** |

### 知识点类型分布

| 类型 | 说明 | 适用题型 |
|------|------|---------|
| `CONCEPTUAL` | 概念理解 | 判断辨析、举例说明 |
| `PROCEDURAL` | 程序性计算 | 计算步骤、纠错题 |
| `REPRESENTATIONAL` | 表征图示 | 画图、数形结合 |

### 知识领域

- **数的认识**：整数、小数、分数、负数的认识与理解
- **数的运算**：四则运算、混合运算、运算律
- **图形与几何**：平面图形、立体图形、图形运动
- **量与计量**：长度、面积、体积、质量、时间单位
- **统计与概率**：数据收集整理、统计图、可能性
- **综合实践**：数学广角、解决问题策略

---

## 文件结构

```
pep-primary-math-taxonomy/
├── data/
│   ├── 1-up/                    ← 一年级上册
│   │   ├── topics.json          ← 微知识点（图的节点）
│   │   ├── dependencies.json    ← 前置依赖边（有向无环图）
│   │   ├── clusters.json        ← 领域聚类摘要
│   │   ├── curriculum-standards.json  ← 课标对齐
│   │   └── manifest.json        ← 统计元数据
│   ├── 1-down/  2-up/  2-down/  ← 同上结构
│   ├── 3-up/  3-down/  4-up/  4-down/
│   └── 5-up/  5-down/  6-up/  6-down/
├── schema/                      ← JSON Schema
├── visualization.html           ← 交互式知识图谱可视化
└── README.md
```

### 每册 5 个文件说明

| 文件 | 内容 |
|------|------|
| `topics.json` | 所有微知识点，含 id、name、type、domain、description、evidence、assessmentPrompt |
| `dependencies.json` | 前置依赖边，含 topicId、prerequisiteId、strength（hard/soft）、reason |
| `clusters.json` | 按领域分组的摘要，面向家长/学生说明每个领域的学习意义 |
| `curriculum-standards.json` | 对齐 2022 年版义务教育数学课程标准 |
| `manifest.json` | 各文件统计数据 |

---

## 数据结构示例

### topic（知识点节点）

```json
{
  "id": "mt_g3u_005",
  "type": "PROCEDURAL",
  "subject": "Mathematics",
  "domain": "数的运算",
  "name": "多位数乘一位数的笔算",
  "description": "掌握多位数乘一位数的笔算方法，理解竖式计算中进位的处理。",
  "ageRangeStart": 8,
  "ageRangeEnd": 9,
  "centrality": 0.85,
  "evidence": [
    "能正确笔算三位数乘一位数",
    "能处理连续进位的情况",
    "能用估算验证结果的合理性"
  ],
  "assessmentPrompt": "{{name}}能正确计算 246×7 并说出每一步的含义吗？",
  "standards": ["pep-math-2022:3上.5.2"]
}
```

### dependency（依赖边）

```json
{
  "topicId": "mt_g3u_005",
  "prerequisiteId": "mt_g2u_008",
  "strength": "hard",
  "reason": "多位数乘一位数需要先掌握表内乘法"
}
```

---

## 使用方式

### JavaScript

```js
import topics from './data/3-up/topics.json' with { type: 'json' };
import deps from './data/3-up/dependencies.json' with { type: 'json' };

const byId = new Map(topics.topics.map(t => [t.id, t]));

// 查找某知识点的所有前置
const prereqs = deps.dependencies
  .filter(d => d.topicId === 'mt_g3u_005')
  .map(d => byId.get(d.prerequisiteId)?.name);

// 查找某知识点解锁的所有后续
const unlocks = deps.dependencies
  .filter(d => d.prerequisiteId === 'mt_g3u_005')
  .map(d => byId.get(d.topicId)?.name);
```

### Python

```python
import json
from collections import defaultdict, deque

# 加载所有册次数据
all_topics, all_deps = [], []
for vol in ['1-up','1-down','2-up','2-down','3-up','3-down',
            '4-up','4-down','5-up','5-down','6-up','6-down']:
    t = json.load(open(f'data/{vol}/topics.json'))
    d = json.load(open(f'data/{vol}/dependencies.json'))
    all_topics.extend(t['topics'])
    all_deps.extend(d['dependencies'])

by_id = {t['id']: t for t in all_topics}

# DAG 拓扑排序（完整学习路径）
graph = defaultdict(list)
in_degree = defaultdict(int)
for d in all_deps:
    if d['prerequisiteId'] in by_id and d['topicId'] in by_id:
        graph[d['prerequisiteId']].append(d['topicId'])
        in_degree[d['topicId']] += 1

queue = deque(t['id'] for t in all_topics if in_degree[t['id']] == 0)
order = []
while queue:
    node = queue.popleft()
    order.append(by_id[node]['name'])
    for nxt in graph[node]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)

print(f'学习路径共 {len(order)} 步')
```

---

## 可视化

打开 `visualization.html` 即可查看交互式知识图谱，支持：

- 按年级/册次筛选
- 按知识领域筛选
- 关键词搜索
- 点击节点查看详情（前置/后续知识点）

---

## License

数据结构遵循 [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) 的 ODbL 1.0 协议（数据库结构）和 CC BY-SA 4.0（内容）。

知识点内容基于人教版教材整理，仅供学习研究使用。
