const fs = require('fs');
const path = require('path');

// 需要修复的文件列表
const filesToFix = [
    'day333.html', 'day334.html', 'day335.html',
    'day339.html', 'day340.html'
];

console.log('修复剩余5个文件的nav-bottom格式...\n');

filesToFix.forEach(filename => {
    const filepath = path.join('.', filename);
    let content = fs.readFileSync(filepath, 'utf8');
    
    // 提取天数
    const dayMatch = filename.match(/day(\d+)/);
    const dayNum = parseInt(dayMatch[1]);
    const prevDay = dayNum - 1;
    const nextDay = dayNum + 1;
    
    // 替换各种可能的nav-bottom格式
    // 模式1: ← 上一天 或 ←上一天
    content = content.replace(
        /<a href="day\d+\.html" class="nav-btn">← 上一天<\/a>/g,
        `<a href="day${String(prevDay).padStart(3,'0')}.html" class="nav-arrow">← 第${prevDay}天</a>`
    );
    content = content.replace(
        /<a href="day\d+\.html" class="nav-btn">←上一天<\/a>/g,
        `<a href="day${String(prevDay).padStart(3,'0')}.html" class="nav-arrow">← 第${prevDay}天</a>`
    );
    
    // 模式2: 下一天 → 或 后一天 →
    content = content.replace(
        /<a href="day\d+\.html" class="nav-btn">下一天 →<\/a>/g,
        `<a href="day${String(nextDay).padStart(3,'0')}.html" class="nav-arrow">第${nextDay}天 →</a>`
    );
    content = content.replace(
        /<a href="day\d+\.html" class="nav-btn">后一天 →<\/a>/g,
        `<a href="day${String(nextDay).padStart(3,'0')}.html" class="nav-arrow">第${nextDay}天 →</a>`
    );
    
    // 模式3: 中间按钮 - 目录 -> 返回首页, nav-btn -> nav-home
    content = content.replace(
        /<a href="index\.html" class="nav-btn">🏠 目录<\/a>/g,
        `<a href="index.html" class="nav-home">🏠 返回首页</a>`
    );
    content = content.replace(
        /<a href="index\.html" class="nav-btn">目录<\/a>/g,
        `<a href="index.html" class="nav-home">🏠 返回首页</a>`
    );
    
    // 写回文件
    fs.writeFileSync(filepath, content, 'utf8');
    console.log(`✅ ${filename} (第${dayNum}天) - 已修复`);
});

console.log('\n完成！');
