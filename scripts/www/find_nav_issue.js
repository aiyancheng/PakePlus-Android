// 找出nav-bottom格式有问题的文件
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
const problemFiles = [];

for (let i = 2; i <= 365; i++) {
    const fileName = `day${String(i).padStart(3, '0')}.html`;
    const filePath = path.join(baseDir, fileName);
    
    if (!fs.existsSync(filePath)) continue;
    
    const content = fs.readFileSync(filePath, 'utf8');
    
    // 检查是否有nav-bottom但没有"返回首页"
    if (content.includes('nav-bottom') && !content.includes('返回首页')) {
        problemFiles.push(fileName);
    }
}

console.log('nav-bottom格式有问题的文件（缺少"返回首页"）:');
problemFiles.forEach(f => console.log(f));
console.log(`\n总计: ${problemFiles.length} 个文件`);
