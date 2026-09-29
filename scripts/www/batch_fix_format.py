#!/usr/bin/env python3
"""
批量修复HTML文件格式，使其符合day001.html标准
主要修复内容：
1. class="show-answer-btn" → class="answer-btn"
2. class="answer-area" → class="reference-answer"
3. class="essay-input" → 删除class属性
4. onclick="showReference(this, 'refId')" → onclick="showReference('btnId', 'refId')"
5. window.onload = function() {...} → document.addEventListener('DOMContentLoaded', () => {...})
"""

import os
import re
import glob

def fix_html_file(file_path):
    """修复单个HTML文件的格式"""
    print(f"正在修复: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 修复1: class="show-answer-btn" → class="answer-btn"
    content = re.sub(r'class="show-answer-btn"', 'class="answer-btn"', content)
    
    # 修复2: class="answer-area" → class="reference-answer"
    content = re.sub(r'class="answer-area"', 'class="reference-answer"', content)
    
    # 修复3: class="essay-input" → 删除class属性（标准格式中textarea无class）
    content = re.sub(r'<textarea class="essay-input"', '<textarea', content)
    
    # 修复4: onclick="showReference(this, 'refId')" → onclick="showReference('btnId', 'refId')"
    # 这个比较复杂，需要先找到所有的showReference调用，然后替换
    # 模式：onclick="showReference(this, 'xxx')"
    pattern = r'onclick="showReference\(this,\s*\'([^\']+)\'\)"'
    
    def replace_show_reference(match):
        ref_id = match.group(1)
        # 生成对应的btnId（通常是refId的变体）
        # 例如：ref86-1 → essayBtn1, ref86-2 → essayBtn2
        btn_id = re.sub(r'ref\d+-(\d+)', r'essayBtn\1', ref_id)
        if btn_id == ref_id:  # 如果没有匹配到模式，使用默认格式
            btn_id = f"essayBtn{ref_id}"
        return f'onclick="showReference(\'{btn_id}\', \'{ref_id}\')"'
    
    content = re.sub(pattern, replace_show_reference, content)
    
    # 修复5: window.onload = function() {...} → document.addEventListener('DOMContentLoaded', () => {...})
    # 模式1: window.onload = function() {\n            initChoiceQuestions();\n        };
    pattern1 = r'window\.onload\s*=\s*function\(\)\s*\{\s*initChoiceQuestions\(\);\s*\};'
    replacement1 = "document.addEventListener('DOMContentLoaded', () => { initChoiceQuestions(); });"
    content = re.sub(pattern1, replacement1, content)
    
    # 模式2: window.onload = function() {\n            initChoiceQuestions();\n        }\n    </script>
    pattern2 = r'window\.onload\s*=\s*function\(\)\s*\{\s*initChoiceQuestions\(\);\s*\}\s*\n\s*</script>'
    replacement2 = "    </script>"
    content = re.sub(pattern2, replacement2, content)
    
    # 修复6: 修复JavaScript中的showReference函数定义
    # 旧格式: function showReference(btn, refId) {
    # 新格式: function showReference(btnId, answerId) {
    old_func_pattern = r'function showReference\(btn,\s*refId\)\s*\{'
    new_func_pattern = 'function showReference(btnId, answerId) {'
    content = re.sub(old_func_pattern, new_func_pattern, content)
    
    # 修复7: 修复JavaScript函数体内的代码
    # 旧: const answerDiv = document.getElementById(refId);
    # 新: const answerDiv = document.getElementById(answerId);
    content = re.sub(r'const answerDiv = document\.getElementById\(refId\);', 
                    r'const answerDiv = document.getElementById(answerId);', content)
    
    # 旧: const btn = document.getElementById(btnId); (可能已经有了，如果没有就添加)
    # 这个函数比较复杂，需要更多逻辑
    
    # 检查是否有修改
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] 已修复")
        return True
    else:
        print(f"  [-] 无需修复")
        return False

def main():
    """主函数"""
    # 获取所有day*.html文件
    html_files = glob.glob("day*.html")
    html_files.sort()
    
    print(f"找到 {len(html_files)} 个HTML文件")
    print("=" * 50)
    
    fixed_count = 0
    for html_file in html_files:
        try:
            if fix_html_file(html_file):
                fixed_count += 1
        except Exception as e:
            print(f"  ✗ 修复失败: {e}")
    
    print("=" * 50)
    print(f"修复完成！共修复 {fixed_count} 个文件")

if __name__ == "__main__":
    main()
