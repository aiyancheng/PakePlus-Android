"""修复training-styles.css中的CSS属性名语法错误"""
import re, os

css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "training-styles.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 修复CSS属性名中连字符被替换的问题
# 正确的属性名模式
fixes = [
    (r'align-items', 'align-items'),
    (r'justify-content', 'justify-content'),
    (r'inline-block', 'inline-block'),
    (r'max-width', 'max-width'),
    (r'box-shadow', 'box-shadow'),
    (r'white-space', 'white-space'),
    (r'text-align', 'text-align'),
    (r'border-radius', 'border-radius'),
    (r'font-size', 'font-size'),
    (r'line-height', 'line-height'),
    (r'grid-template-columns', 'grid-template-columns'),
    (r'flex-shrink', 'flex-shrink'),
    (r'letter-spacing', 'letter-spacing'),
    (r'background-color', 'background-color'),
    (r'border-color', 'border-color'),
    (r'transform', 'transform'),
]

fixed_count = 0
for wrong, right in fixes:
    count = css.count(wrong)
    if count > 0:
        css = css.replace(wrong, right)
        fixed_count += count
        print(f"  修复: '{wrong}' -> '{right}' ({count}处)")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print(f"\n共修复 {fixed_count} 处错误")
print("CSS文件已修复并保存")
