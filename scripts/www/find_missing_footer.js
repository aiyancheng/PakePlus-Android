// 找出缺少footer-support的文件
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
const missingFiles = [];

for (let i = 2; i <= 365; i++) {
    const fileName = `day${String(i).padStart(3, '0')}.html`;
    const filePath = path.join(baseDir, fileName);
    
    if (!fs.existsSync(filePath)) continue;
    
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (!content.includes('footer-support')) {
        missingFiles.push(fileName);
    }
}

console.log('缺少footer-support的文件:');
missingFiles.forEach(f => console.log(f));
console.log(`\n总计: ${missingFiles.length} 个文件`);
