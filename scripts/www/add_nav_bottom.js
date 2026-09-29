// 为缺少nav-bottom的文件添加导航按钮
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';

// 从报告得知缺少nav-bottom的文件
const filesToFix = [
    'day072.html', 'day073.html', 'day074.html', 'day075.html',
    'day082.html', 'day083.html', 'day084.html',
    'day088.html', 'day089.html', 'day090.html', 'day091.html', 'day092.html', 'day093.html'
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
    
    // 检查是否已经有nav-bottom
    if (content.includes('nav-bottom')) {
        console.log(`  ⚠️ ${fileName}: 已有nav-bottom`);
        return;
    }
    
    // 提取天数
    const dayMatch = fileName.match(/day(\d+)/);
    if (!dayMatch) {
        console.log(`  ❌ ${fileName}: 无法解析天数`);
        errorCount++;
        return;
    }
    
    const dayNum = parseInt(dayMatch[1]);
    const prevDay = dayNum === 1 ? 365 : dayNum - 1;
    const nextDay = dayNum === 365 ? 1 : dayNum + 1;
    
    // 创建nav-bottom HTML
    const navBottom = `    <!-- 底部导航按钮区 -->\n    <div class="nav-bottom">\n        <a href="day${String(prevDay).padStart(3,'0')}.html" class="nav-arrow">← 第${prevDay}天</a>\n        <a href="index.html" class="nav-home">🏠 返回首页</a>\n        <a href="day${String(nextDay).padStart(3,'0')}.html" class="nav-arrow">第${nextDay}天 →</a>\n    </div>`;
    
    // 在</body>之前插入nav-bottom
    const bodyEndIndex = content.indexOf('</body>');
    if (bodyEndIndex === -1) {
        console.log(`  ❌ ${fileName}: 找不到</body>`);
        errorCount++;
        return;
    }
    
    content = content.substring(0, bodyEndIndex) + '\n' + navBottom + '\n' + content.substring(bodyEndIndex);
    
    // 写回文件
    fs.writeFileSync(filePath, content, 'utf8');
    fixedCount++;
    console.log(`  ✅ ${fileName}: 已添加nav-bottom`);
});

console.log(`\n修复完成:`);
console.log(`  - 成功修复: ${fixedCount} 个文件`);
console.log(`  - 失败: ${errorCount} 个文件`);
