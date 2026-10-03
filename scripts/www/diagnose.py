import sys, os, glob, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'c:\Users\81784\WorkBuddy\20260326092633\眼镜门店新员工8周成才'
all_files = sorted(glob.glob(os.path.join(base, '**', '*练习题.html'), recursive=True))

for f in all_files:
    content = open(f, encoding='utf-8').read()
    rel = os.path.relpath(f, base)

    # 检测类型标记
    type_tag = 'none'
    for t in ['type-a', 'type-b', 'type-c', 'type-d', 'type-e']:
        if 'interactive-options-' + t in content:
            type_tag = t
            break

    # 检查是否有双重JS
    js_count = content.count('interactive-options-type')
    
    # 针对type-a：检查正则能否匹配到答案
    issues = []
    if type_tag == 'type-a':
        # 找所有 answer-hint 内容
        hints = re.findall(r'class="answer-hint"[^>]*>(.*?)</div>', content, re.DOTALL)
        for h in hints:
            # 检查是否有 <strong> 包裹答案字母
            if re.search(r'正确答案[：:]\s*<strong>[A-Da-d]', h):
                pass  # OK
            elif re.search(r'正确答案[：:][^<\n]*[A-Da-d]', h):
                issues.append('answer-hint无<strong>标签')
                break

    if type_tag == 'type-b':
        # 找所有 answer-box 内容
        boxes = re.findall(r'class="answer-box"[^>]*>(.*?)</div>', content, re.DOTALL)
        for b in boxes:
            if re.search(r'正确答案[：:]\s*([A-Da-d])', b):
                pass  # OK
            
    if js_count > 2:
        issues.append('多套JS({})'.format(js_count))
    elif js_count == 2:
        # 检查是否有原始手写JS + 注入JS
        if content.count('<script>') > 2:
            issues.append('疑似双重JS脚本')

    status = 'OK' if not issues else '!! ' + '; '.join(issues)
    print('{} [{}] {}'.format(rel.split('\\')[-1], type_tag, status))
