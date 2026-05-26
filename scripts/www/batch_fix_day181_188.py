#!/usr/bin/env python3
"""
批量修复 day181-day188 的 choiceQuestions 数据和问答题格式
"""
import re

# 预定义的 choiceQuestions 数据（基于培训内容推断）
QUESTIONS_DATA = {
    'day181': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 20/20', 'correct': True},
                {'text': 'B. 20/40', 'correct': False},
                {'text': 'C. 20/100', 'correct': False},
                {'text': 'D. 20/200', 'correct': False}
            ],
            'answer': [0],
            'score': 10,
            'explanation': 'LogMAR = 0.0 相当于 Snellen 20/20（即视力1.0），这是标准视力。20/200 = LogMAR 1.0 是法定盲的标准。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 每行字母数相等（5个）', 'correct': True},
                {'text': 'B. 难度递增均匀（每行LogMAR差0.1）', 'correct': True},
                {'text': 'C. 线性好，便于统计分析', 'correct': True},
                {'text': 'D. 国际通用标准', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': 'LogMAR视力表相比Snellen的优点包括：每行字母数相等（5个）、难度递增均匀（每行LogMAR差0.1）、线性好便于统计分析、国际通用标准。四个优点都是LogMAR的优势。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 1个', 'correct': False},
                {'text': 'B. 2个', 'correct': False},
                {'text': 'C. 3个', 'correct': True},
                {'text': 'D. 4个', 'correct': False}
            ],
            'answer': [2],
            'score': 10,
            'explanation': '使用LogMAR视力表检查时，如果顾客在某行认对少于3个字母，应停止检查。因为再往后的行更看不清，继续检查没有意义。'
        }
    ],
    'day182': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 电脑验光仪', 'correct': False},
                {'text': 'B. 综合验光仪', 'correct': True},
                {'text': 'C. 镜片箱', 'correct': False},
                {'text': 'D. 瞳距仪', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '综合验光仪是主观验光的核心设备，可以精确测量顾客的屈光状态（球镜、柱镜、轴位、ADD等），是验光师的"主战场"。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 视标系统（投影仪/液晶屏）', 'correct': True},
                {'text': 'B. 球镜轮和柱镜轮', 'correct': True},
                {'text': 'C. 交叉圆柱镜（JCC）', 'correct': True},
                {'text': 'D. 瞳距测量模块', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': '综合验光仪的主要部件包括：视标系统（投影仪或液晶屏，显示视力表）、球镜轮和柱镜轮（调节度数）、交叉圆柱镜JCC（精调轴位和度数）、瞳距测量模块（测量瞳距）。四个部件都是综合验光仪的标准配置。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 直接告诉顾客度数', 'correct': False},
                {'text': 'B. 让顾客比较"1和2哪个更清楚"', 'correct': True},
                {'text': 'C. 让顾客自己选择镜片', 'correct': False},
                {'text': 'D. 跳过主观验光，直接给处方', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '使用综合验光仪进行主观验光时，核心方法是让顾客比较"1和2哪个更清楚"（或"3和4哪个更清楚"）。这是标准化的问诊方式，避免诱导性提问，让顾客自主判断。'
        }
    ],
    'day183': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 用遮眼板遮住左眼', 'correct': False},
                {'text': 'B. 调整座椅高度，让顾客眼睛与仪器目镜中心平齐', 'correct': True},
                {'text': 'C. 直接开始验光', 'correct': False},
                {'text': 'D. 让顾客自己操作仪器', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '使用综合验光仪的第一步是调整座椅高度，让顾客眼睛与仪器目镜中心平齐。如果高度不合适，顾客需要仰头或低头，会导致姿势不舒适，影响验光结果。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 初检（电脑验光仪）', 'correct': True},
                {'text': 'B. 置入验光（综合验光仪）', 'correct': True},
                {'text': 'C. 处方确认（试戴）', 'correct': True},
                {'text': 'D. 记录处方', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': '综合验光仪标准验光流程包括：初检（用电脑验光仪获得客观验光结果）、置入验光（用综合验光仪精细调整度数）、处方确认（让顾客试戴，确认舒适度）、记录处方（写下最终处方）。四个步骤缺一不可。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 柱镜轴位', 'correct': False},
                {'text': 'B. 球镜度数', 'correct': True},
                {'text': 'C. 柱镜度数', 'correct': False},
                {'text': 'D. ADD（老花附加）', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '使用综合验光仪时，首先调整的是球镜度数（用粗调轮快速接近正确度数），然后才是柱镜轴位和柱镜度数的精细调整。球镜是基础，必须先确定。'
        }
    ],
    'day184': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 老花眼（Presbyopia）', 'correct': True},
                {'text': 'B. 近视（Myopia）', 'correct': False},
                {'text': 'C. 散光（Astigmatism）', 'correct': False},
                {'text': 'D. 远视（Hyperopia）', 'correct': False}
            ],
            'answer': [0],
            'score': 10,
            'explanation': 'ADD（Addition）是指老花附加度数，即看近处时需要额外增加的正度数。随着年龄增长，晶状体弹性下降，调节能力减弱，需要ADD来补偿。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 年龄（主要因素）', 'correct': True},
                {'text': 'B. 原先的屈光状态', 'correct': True},
                {'text': 'C. 用眼习惯', 'correct': True},
                {'text': 'D. 健康状况', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': 'ADD的大小受多种因素影响：年龄（主要因素，年龄越大ADD越大）、原先的屈光状态（近视者ADD较小，远视者ADD较大）、用眼习惯（近距离工作多者ADD需求大）、健康状况（糖尿病等全身疾病可能影响）。四个因素都需要考虑。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. +0.75D', 'correct': False},
                {'text': 'B. +1.00D', 'correct': False},
                {'text': 'C. +1.50D', 'correct': False},
                {'text': 'D. +2.00D', 'correct': True}
            ],
            'answer': [3],
            'score': 10,
            'explanation': '根据年龄与ADD对应表，55岁对应的ADD大约是+2.00D。年龄与ADD的对应关系：40岁≈+0.75D，45岁≈+1.00D，50岁≈+1.50D，55岁≈+2.00D，60岁≈+2.50D。'
        }
    ],
    'day185': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 用酒精棉球擦拭镜头', 'correct': False},
                {'text': 'B. 用镜头纸或专用布轻轻擦拭', 'correct': True},
                {'text': 'C. 用清水冲洗', 'correct': False},
                {'text': 'D. 用纸巾擦拭', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '清洁综合验光仪镜头时，应该用镜头纸或专用布轻轻擦拭。不能用酒精（可能损坏镀膜）、清水（可能留下水渍）、纸巾（可能划伤镜头）。正确方法是用镜头纸沿一个方向轻轻擦拭。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 每日清洁镜头和目镜', 'correct': True},
                {'text': 'B. 每周检查瞳距仪精度', 'correct': True},
                {'text': 'C. 每月校准球镜轮和柱镜轮', 'correct': True},
                {'text': 'D. 每年更换灯泡', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': '综合验光仪的保养包括：每日清洁镜头和目镜（保持清晰）、每周检查瞳距仪精度（确保测量准确）、每月校准球镜轮和柱镜轮（确保度数准确）、每年更换灯泡（投影仪灯泡寿命约1000小时）。四个保养项目都很重要。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 继续使用', 'correct': False},
                {'text': 'B. 立即停止使用，联系维修', 'correct': True},
                {'text': 'C. 自己拆开修理', 'correct': False},
                {'text': 'D. 忽略问题', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '如果发现综合验光仪有异常（如度数显示错误、按钮失灵、投影模糊等），应该立即停止使用，联系专业维修人员。不能继续使用（可能导致错误验光），不能自己拆修（可能损坏设备），不能忽略（问题会恶化）。'
        }
    ],
    'day186': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 角膜地形图仪', 'correct': False},
                {'text': 'B. 眼底镜', 'correct': True},
                {'text': 'C. 眼压计', 'correct': False},
                {'text': 'D. 视野计', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '眼底镜（检眼镜）用于检查视网膜、视神经乳头、黄斑区等眼底结构，是发现青光眼、糖尿病视网膜病变、黄斑变性等眼病的重要工具。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 直接检眼镜', 'correct': True},
                {'text': 'B. 间接检眼镜', 'correct': True},
                {'text': 'C. 裂隙灯+前置镜', 'correct': True},
                {'text': 'D. OCT（光学相干断层扫描）', 'correct': False}
            ],
            'answer': [0, 1, 2],
            'score': 10,
            'explanation': '常用的眼底检查方法包括：直接检眼镜（手持式，简便快捷，看到正立像）、间接检眼镜（头戴式，视野大，看到倒立像，适合周边眼底检查）、裂隙灯+前置镜（通过裂隙灯看眼底，放大倍数高）。OCT是断层扫描，不是直接的眼底镜检查。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 正常视神经乳头', 'correct': False},
                {'text': 'B. 青光眼性视神经病变', 'correct': True},
                {'text': 'C. 糖尿病视网膜病变', 'correct': False},
                {'text': 'D. 黄斑变性', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': '杯盘比（Cup-to-Disc Ratio, CDR）增大是青光眼性视神经病变的典型表现。正常CDR ≤ 0.3，青光眼患者CDR通常 > 0.6，且双眼差异 > 0.2。'
        }
    ],
    'day187': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 角膜', 'correct': False},
                {'text': 'B. 晶状体', 'correct': False},
                {'text': 'C. 玻璃体', 'correct': False},
                {'text': 'D. 视网膜', 'correct': True}
            ],
            'answer': [3],
            'score': 10,
            'explanation': 'OCT（光学相干断层扫描）主要检查视网膜的层间结构，可以精确测量视网膜厚度、发现黄斑水肿、视网膜前膜、玻璃体牵拉等病变。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 黄斑疾病（黄斑水肿、黄斑前膜、黄斑裂孔）', 'correct': True},
                {'text': 'B. 青光眼（视网膜神经纤维层厚度）', 'correct': True},
                {'text': 'C. 糖尿病视网膜病变', 'correct': True},
                {'text': 'D. 高度近视眼底病变', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': 'OCT的临床应用非常广泛，包括：黄斑疾病（黄斑水肿、黄斑前膜、黄斑裂孔等）、青光眼（测量视网膜神经纤维层厚度，评估视神经损害）、糖尿病视网膜病变（发现黄斑水肿、微动脉瘤等）、高度近视眼底病变（漆裂纹、Fuchs斑等）。四个都是OCT的重要应用。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 1-2分钟', 'correct': False},
                {'text': 'B. 3-5分钟', 'correct': True},
                {'text': 'C. 10-15分钟', 'correct': False},
                {'text': 'D. 20-30分钟', 'correct': False}
            ],
            'answer': [1],
            'score': 10,
            'explanation': 'OCT检查通常需要3-5分钟（每只眼约1-2分钟）。相比眼底照相或眼底镜检查，OCT稍慢，但远快于视野检查（20-30分钟）。'
        }
    ],
    'day188': [
        {
            'type': 'single',
            'options': [
                {'text': 'A. 眼压正常就可以排除青光眼', 'correct': False},
                {'text': 'B. 眼压升高就一定有青光眼', 'correct': False},
                {'text': 'C. 眼压正常也不能排除青光眼（正常眼压性青光眼）', 'correct': True},
                {'text': 'D. 眼压与青光眼无关', 'correct': False}
            ],
            'answer': [2],
            'score': 10,
            'explanation': '眼压正常也不能排除青光眼，因为存在"正常眼压性青光眼"（Normal-Tension Glaucoma, NTG），这类患者的眼压在正常范围内（<21mmHg），但视神经损伤仍在进展。所以不能仅凭眼压正常就排除青光眼。'
        },
        {
            'type': 'multi',
            'options': [
                {'text': 'A. 眼压测量', 'correct': True},
                {'text': 'B. 眼底镜检查（视神经乳头）', 'correct': True},
                {'text': 'C. 视野检查', 'correct': True},
                {'text': 'D. OCT（视网膜神经纤维层厚度）', 'correct': True}
            ],
            'answer': [0, 1, 2, 3],
            'score': 10,
            'explanation': '青光眼筛查的"金标准"组合包括：眼压测量（NCT或GAT，正常10-21mmHg）、眼底镜检查（观察视神经乳头杯盘比，正常≤0.3）、视野检查（检测视野缺损，如弓形暗点、鼻侧阶梯）、OCT（测量视网膜神经纤维层厚度，正常≥80μm）。四个检查缺一不可。'
        },
        {
            'type': 'single',
            'options': [
                {'text': 'A. 立即转诊眼科医院', 'correct': True},
                {'text': 'B. 继续验光，忽略青光眼迹象', 'correct': False},
                {'text': 'C. 让顾客自己决定是否就医', 'correct': False},
                {'text': 'D. 给顾客开眼药水', 'correct': False}
            ],
            'answer': [0],
            'score': 10,
            'explanation': '如果发现顾客有青光眼迹象（眼压>21mmHg、杯盘比>0.6、视野缺损、OCT异常），应该立即转诊眼科医院进行确诊和治疗。青光眼是不可逆性致盲眼病，早发现早治疗是关键。验光师不能诊断或治疗青光眼，只能筛查和转诊。'
        }
    ]
}

def generate_choiceQuestions_js(day_num):
    """生成choiceQuestions JavaScript代码"""
    day_key = f'day{day_num}'
    if day_key not in QUESTIONS_DATA:
        return None
    
    questions = QUESTIONS_DATA[day_key]
    js_lines = ['        // ========== 选择题数据 ==========', '        const choiceQuestions = [']
    
    for i, q in enumerate(questions):
        js_lines.append('            {')
        js_lines.append(f'                type: \'{q["type"]}\',')
        js_lines.append('                options: [')
        for j, opt in enumerate(q['options']):
            correct_str = 'true' if opt['correct'] else 'false'
            js_lines.append(f'                    {{ text: \'{opt["text"]}\', correct: {correct_str} }},')
        js_lines.append('                ],')
        answer_str = str(q['answer'])
        js_lines.append(f'                answer: {answer_str},')
        js_lines.append(f'                score: {q["score"]},')
        # 转义explanation中的单引号
        explanation_escaped = q['explanation'].replace('\\', '\\\\').replace("'", "\\'")
        js_lines.append(f'                explanation: \'{explanation_escaped}\'')
        if i < len(questions) - 1:
            js_lines.append('            },')
        else:
            js_lines.append('            }')
    
    js_lines.append('        ];')
    return '\n'.join(js_lines)

def fix_file(filepath):
    """修复单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取day编号
    import os
    filename = os.path.basename(filepath)
    day_num = filename.replace('day', '').replace('.html', '')
    
    # 1. 修复choiceQuestions数据
    choiceQuestions_js = generate_choiceQuestions_js(day_num)
    if choiceQuestions_js:
        # 找到旧的choiceQuestions并替换
        pattern = r'// ========== 选择题数据 ==========\s*const choiceQuestions = \[[^\]]*\];'
        replacement = choiceQuestions_js
        content_new = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if content_new == content:
            print(f'  [WARN] 无法替换choiceQuestions: {filename}')
            return False
        content = content_new
        print(f'  [OK] 已修复choiceQuestions: {filename}')
    
    # 2. 修复问答题按钮格式
    # 替换 button class="reference-btn" 为 class="answer-btn" id="essayBtn1"
    old_btn_pattern = r'<button class="reference-btn" onclick="toggleReference\([^"]+\)">'
    new_btn = '<button class="answer-btn" id="essayBtn1" onclick="showReference(\'essayBtn1\', \'essayAnswer1\')">'
    content = re.sub(old_btn_pattern, new_btn, content)
    
    # 替换 answer div: id="ref1" style="display:none;" 为 id="essayAnswer1"
    old_answer_pattern = r'<div class="reference-answer" id="ref1" style="display:none;">'
    new_answer = '<div class="reference-answer" id="essayAnswer1">'
    content = re.sub(old_answer_pattern, new_answer, content)
    
    # 检查是否修复了问答题
    if 'class="reference-btn"' in content:
        print(f'  ⚠️ 仍有reference-btn: {filename}')
    else:
        print(f'  ✓ 已修复问答题按钮: {filename}')
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    import os
    
    files_to_fix = [f'day{i:03d}.html' for i in range(181, 189)]  # day181-day188
    
    print('开始批量修复 day181-day188...')
    print('=' * 50)
    
    success_count = 0
    for filename in files_to_fix:
        filepath = os.path.join('d:\\365培训', filename)
        if not os.path.exists(filepath):
            print(f'⚠️ 文件不存在: {filename}')
            continue
        
        print(f'\n处理: {filename}')
        try:
            if fix_file(filepath):
                success_count += 1
        except Exception as e:
            print(f'  ❌ 错误: {e}')
    
    print('\n' + '=' * 50)
    print(f'修复完成: {success_count}/{len(files_to_fix)} 个文件成功')

if __name__ == '__main__':
    main()
