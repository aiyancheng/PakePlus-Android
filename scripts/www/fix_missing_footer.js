// 修复17个缺少footer-support的文件（添加标准footer-support）
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
const filesToFix = [
    'day071.html', 'day072.html', 'day073.html', 'day074.html', 'day075.html',
    'day085.html', 'day086.html', 'day087.html', 'day154.html', 'day155.html',
    'day156.html', 'day157.html', 'day158.html', 'day159.html', 'day160.html',
    'day161.html', 'day176.html'
];

let fixedCount = 0;
let errorCount = 0;

filesToFix.forEach(fileName => {
    const filePath = path.join(baseDir, fileName);
    if (!fs.existsSync(filePath)) {
        console.log(`  ⚠️ ${fileName}: 文件不存在`);
        return;
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;
    
    // 步骤1：删除任何现有的footer（可能在各种格式）
    // 匹配可能的footer格式
    const footerPatterns = [
        /<div style="text-align:\s*center[^"]*"[^>]*>[\s\S]*?闫胜君视光工作室[\s\S]*?<\/div>/gi,
        /<div class="footer-support">[\s\S]*?<\/div>/gi,
        /技术支持：闫胜君视光工作室[\s\S]*?<\/div>/gi
    ];
    
    footerPatterns.forEach(pattern => {
        if (pattern.test(content)) {
            content = content.replace(pattern, '');
            modified = true;
        }
    });
    
    // 步骤2：在</html>之后添加标准footer-support
    const htmlEndIndex = content.indexOf('</html>');
    if (htmlEndIndex === -1) {
        console.log(`  ❌ ${fileName}: 找不到</html>`);
        errorCount++;
        return;
    }
    
    const standardFooter = '\n<!-- 底部技术支持署名 -->\n<div class="footer-support">\n    技术支持：闫胜君视光工作室\n</div>';
    
    content = content.substring(0, htmlEndIndex + 7) + standardFooter + '\n' + content.substring(htmlEndIndex + 7);
    modified = true;
    
    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        fixedCount++;
        console.log(`  ✅ ${fileName}: 已添加footer-support`);
    }
});

console.log(`\n修复完成:`);
console.log(`  - 成功修复: ${fixedCount} 个文件`);
console.log(`  - 失败: ${errorCount} 个文件`);
