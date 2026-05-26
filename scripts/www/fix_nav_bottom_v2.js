// 修复nav-bottom格式：添加"返回首页"按钮
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
const problemFiles = [
    'day073.html', 'day074.html', 'day075.html', 'day085.html', 'day086.html',
    'day087.html', 'day098.html', 'day154.html', 'day155.html', 'day156.html',
    'day157.html', 'day158.html', 'day159.html', 'day160.html', 'day161.html',
    'day176.html', 'day219.html', 'day220.html', 'day221.html', 'day222.html',
    'day223.html'
];

let fixedCount = 0;
let errorCount = 0;

problemFiles.forEach(fileName => {
    const filePath = path.join(baseDir, fileName);
    if (!fs.existsSync(filePath)) {
        console.log(`  ⚠️ ${fileName}: 文件不存在`);
        return;
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    
    // 查找nav-bottom
    const navIndex = content.indexOf('nav-bottom');
    if (navIndex === -1) {
        console.log(`  ❌ ${fileName}: 找不到nav-bottom`);
        errorCount++;
        return;
    }
    
    // 找到nav-bottom的div开始和结束
    const navStart = content.lastIndexOf('<div', navIndex);
    const navEnd = content.indexOf('</div>', navIndex) + 6;
    
    if (navStart === -1 || navEnd === -1) {
        console.log(`  ❌ ${fileName}: 无法解析nav-bottom`);
        errorCount++;
        return;
    }
    
    const navContent = content.substring(navStart, navEnd);
    
    // 检查是否已经有"返回首页"
    if (navContent.includes('返回首页')) {
        console.log(`  ⚠️ ${fileName}: 已有返回首页按钮`);
        return;
    }
    
    // 修复nav-bottom：添加"返回首页"按钮
    // 格式应该是：← 第X天 / 🏠 返回首页 / 第Y天 →
    let newNavContent;
    
    if (navContent.includes('上一天') || navContent.includes('下一天')) {
        // 旧格式：上一天/下一天 → 需要完全重写
        const dayNum = parseInt(fileName.match(/day(\d+)/)[1]);
        const prevDay = dayNum === 1 ? 365 : dayNum - 1;
        const nextDay = dayNum === 365 ? 1 : dayNum + 1;
        
        newNavContent = `        <div class="nav-bottom">\n            <a href="day${String(prevDay).padStart(3,'0')}.html" class="nav-arrow">← 第${prevDay}天</a>\n            <a href="index.html" class="nav-home">🏠 返回首页</a>\n            <a href="day${String(nextDay).padStart(3,'0')}.html" class="nav-arrow">第${nextDay}天 →</a>\n        </div>`;
    } else {
        // 新格式但没有返回首页：在中间插入
        const parts = navContent.split('\n');
        const homeLink = '            <a href="index.html" class="nav-home">🏠 返回首页</a>';
        
        // 在第一个</a>之后插入
        let insertIndex = -1;
        for (let i = 0; i < parts.length; i++) {
            if (parts[i].includes('</a>') && !parts[i].includes('nav-home')) {
                insertIndex = i + 1;
                break;
            }
        }
        
        if (insertIndex === -1) {
            console.log(`  ❌ ${fileName}: 无法插入返回首页按钮`);
            errorCount++;
            return;
        }
        
        parts.splice(insertIndex, 0, homeLink);
        newNavContent = parts.join('\n');
    }
    
    // 替换原nav-bottom
    content = content.substring(0, navStart) + newNavContent + content.substring(navEnd);
    
    // 写回文件
    fs.writeFileSync(filePath, content, 'utf8');
    fixedCount++;
    console.log(`  ✅ ${fileName}: 已修复nav-bottom`);
});

console.log(`\n修复完成:`);
console.log(`  - 成功修复: ${fixedCount} 个文件`);
console.log(`  - 失败: ${errorCount} 个文件`);
