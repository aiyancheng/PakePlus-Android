// 修复footer-support位置：从</body>内部移到</body></html>之后
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
let fixedCount = 0;
let errorCount = 0;

for (let i = 2; i <= 365; i++) {
    const fileName = `day${String(i).padStart(3, '0')}.html`;
    const filePath = path.join(baseDir, fileName);
    
    if (!fs.existsSync(filePath)) continue;
    
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;
    
    // 查找footer-support的位置
    const footerIndex = content.indexOf('footer-support');
    if (footerIndex === -1) continue;
    
    // 检查footer-support是否在</body>之前（错误位置）
    const bodyEndIndex = content.indexOf('</body>');
    if (footerIndex < bodyEndIndex) {
        // footer-support在错误位置，需要修复
        
        // 找到footer-support的开始和结束
        const footerStart = content.lastIndexOf('<div', footerIndex);
        const footerEnd = content.indexOf('</div>', footerIndex) + 6;
        
        if (footerStart === -1 || footerEnd === -1) {
            console.error(`  ❌ ${fileName}: 无法解析footer-support`);
            errorCount++;
            continue;
        }
        
        const footerContent = content.substring(footerStart, footerEnd);
        
        // 从原位置删除footer-support
        content = content.substring(0, footerStart) + content.substring(footerEnd);
        
        // 找到</html>的位置，在它之后插入footer-support
        const htmlEndIndex = content.indexOf('</html>');
        if (htmlEndIndex === -1) {
            console.error(`  ❌ ${fileName}: 找不到</html>`);
            errorCount++;
            continue;
        }
        
        content = content.substring(0, htmlEndIndex + 7) + '\n' + footerContent + '\n' + content.substring(htmlEndIndex + 7);
        
        modified = true;
    }
    
    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        fixedCount++;
        if (fixedCount <= 5 || fixedCount % 50 === 0) {
            console.log(`  ✅ ${fileName}: 已修复footer位置`);
        }
    }
}

console.log(`\n修复完成:`);
console.log(`  - 成功修复: ${fixedCount} 个文件`);
console.log(`  - 失败: ${errorCount} 个文件`);
