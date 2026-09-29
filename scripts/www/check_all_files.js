// 检查所有HTML文件是否符合day001.html标准格式
const fs = require('fs');
const path = require('path');

const baseDir = 'd:/365培训';
const results = [];

// 检查单个文件
function checkFile(filePath) {
    const fileName = path.basename(filePath);
    const dayMatch = fileName.match(/day(\d+)\.html/);
    if (!dayMatch) return null;
    
    const dayNum = parseInt(dayMatch[1]);
    const content = fs.readFileSync(filePath, 'utf8');
    
    const issues = [];
    
    // 1. 检查标题格式
    const titleMatch = content.match(/<title>(第\d+天 \| .+? - 365天眼镜门店员工晋级培训)<\/title>/);
    if (!titleMatch) {
        issues.push('标题格式不正确');
    }
    
    // 2. 检查是否有container div
    if (!content.includes('<div class="container">')) {
        issues.push('缺少container div');
    }
    
    // 3. 检查是否有page-header
    if (!content.includes('page-header')) {
        issues.push('缺少page-header');
    }
    
    // 4. 检查是否有progress-bar
    if (!content.includes('progress-bar')) {
        issues.push('缺少progress-bar');
    }
    
    // 5. 检查是否有practice-section
    if (!content.includes('practice-section')) {
        issues.push('缺少practice-section');
    }
    
    // 6. 检查JavaScript函数
    const requiredFunctions = ['initChoiceQuestions', 'toggleOption', 'getSelectedIndices', 'submitAll'];
    requiredFunctions.forEach(func => {
        if (!content.includes(`function ${func}`)) {
            issues.push(`缺少函数: ${func}`);
        }
    });
    
    // 7. 检查footer-support位置（应该在</body></html>之后）
    const bodyEndIndex = content.indexOf('</body>');
    const htmlEndIndex = content.indexOf('</html>');
    const footerIndex = content.indexOf('footer-support');
    
    if (footerIndex > 0) {
        if (footerIndex < bodyEndIndex) {
            issues.push('footer-support位置不正确（应该在</body>之后）');
        }
    } else {
        issues.push('缺少footer-support');
    }
    
    // 8. 检查nav-bottom格式
    const navBottomMatch = content.match(/nav-bottom[\s\S]*?<\/div>/);
    if (navBottomMatch) {
        const navContent = navBottomMatch[0];
        if (!navContent.includes('nav-home') || !navContent.includes('返回首页')) {
            issues.push('nav-bottom格式不正确（缺少返回首页按钮）');
        }
    } else {
        issues.push('缺少nav-bottom');
    }
    
    return {
        file: fileName,
        day: dayNum,
        issues: issues,
        issueCount: issues.length
    };
}

// 扫描所有dayXXX.html文件
console.log('开始检查所有HTML文件...\n');

for (let i = 2; i <= 365; i++) {
    const fileName = `day${String(i).padStart(3, '0')}.html`;
    const filePath = path.join(baseDir, fileName);
    
    if (fs.existsSync(filePath)) {
        const result = checkFile(filePath);
        if (result) {
            results.push(result);
        }
    }
}

// 按问题数量排序
results.sort((a, b) => b.issueCount - a.issueCount);

// 输出报告
console.log('='.repeat(80));
console.log('检查报告');
console.log('='.repeat(80));
console.log(`总计检查: ${results.length} 个文件`);
console.log('');

// 统计
const issueStats = {};
results.forEach(r => {
    r.issues.forEach(issue => {
        issueStats[issue] = (issueStats[issue] || 0) + 1;
    });
});

console.log('问题统计:');
Object.keys(issueStats).sort((a, b) => issueStats[b] - issueStats[a]).forEach(issue => {
    console.log(`  ${issue}: ${issueStats[issue]} 个文件`);
});
console.log('');

// 输出详细结果（问题最多的前20个）
console.log('问题最多的文件（前20个）:');
console.log('-'.repeat(80));
results.slice(0, 20).forEach(r => {
    console.log(`\n${r.file} (第${r.day}天) - ${r.issueCount}个问题`);
    r.issues.forEach(issue => {
        console.log(`  ❌ ${issue}`);
    });
});

// 保存完整报告到文件
const reportPath = path.join(baseDir, 'format_check_report.txt');
let reportContent = '365天培训HTML文件格式检查报告\n';
reportContent += `生成时间: ${new Date().toLocaleString('zh-CN')}\n`;
reportContent += '='.repeat(80) + '\n\n';

reportContent += '问题统计:\n';
Object.keys(issueStats).sort((a, b) => issueStats[b] - issueStats[a]).forEach(issue => {
    reportContent += `  ${issue}: ${issueStats[issue]} 个文件\n`;
});
reportContent += '\n';

reportContent += '详细结果（按问题数量降序）:\n';
reportContent += '-'.repeat(80) + '\n';
results.forEach(r => {
    reportContent += `\n${r.file} (第${r.day}天) - ${r.issueCount}个问题\n`;
    r.issues.forEach(issue => {
        reportContent += `  ❌ ${issue}\n`;
    });
});

fs.writeFileSync(reportPath, reportContent, 'utf8');
console.log(`\n完整报告已保存到: ${reportPath}`);
