const fs = require('fs');
const path = require('path');

console.log('============================================================');
console.log('严格检查脚本：以day001.html为标准的全面检查');
console.log('============================================================\n');

const files = fs.readdirSync('.').filter(f => /^day\d+\.html$/.test(f)).sort((a, b) => {
    const numA = parseInt(a.match(/day(\d+)/)[1]);
    const numB = parseInt(b.match(/day(\d+)/)[1]);
    return numA - numB;
});

console.log(`找到 ${files.length} 个dayXXX.html文件\n`);

const problems = [];

files.forEach(file => {
    const filePath = path.join('.', file);
    const content = fs.readFileSync(filePath, 'utf8');
    const dayNum = file.match(/day(\d+)/)[1];
    const issues = [];
    
    // 检查1: 标题格式
    const titleMatch = content.match(/<title>(.*?)<\/title>/);
    if (titleMatch) {
        const title = titleMatch[1];
        // 标准格式: 第X天 | [主题] - 365天眼镜门店员工晋级培训
        if (!title.match(/第\d+天\s*\|.+-\s*365天眼镜门店员工晋级培训/)) {
            issues.push('标题格式不正确');
        }
    }
    
    // 检查2: container div
    if (!content.includes('<div class="container">')) {
        issues.push('缺少 <div class="container">');
    }
    
    // 检查3: page-header结构
    if (!content.includes('class="page-header"')) {
        issues.push('缺少 page-header');
    }
    if (!content.includes('class="day-number"')) {
        issues.push('缺少 day-number');
    }
    if (!content.includes('class="page-title"')) {
        issues.push('缺少 page-title');
    }
    
    // 检查4: 进度条
    if (!content.includes('class="progress-bar-container"')) {
        issues.push('缺少 progress-bar-container');
    }
    
    // 检查5: learning-card结构
    if (!content.includes('class="learning-card"')) {
        issues.push('缺少 learning-card');
    }
    if (!content.includes('class="card-header"')) {
        issues.push('缺少 card-header');
    }
    
    // 检查6: 练习题结构 (关键检查!)
    const hasChoiceQuestions = content.includes('class="choice-questions"'); // 错误
    const hasChoiceQuestion = content.includes('class="choice-question"'); // 正确
    const hasEssayQuestions = content.includes('class="essay-questions"'); // 错误
    const hasEssayQuestion = content.includes('class="essay-question"'); // 正确
    const hasQuestionCard = content.includes('class="question-card"'); // 错误
    const hasH4InPractice = content.match(/class="practice-section[\s\S]*?<h4/); // 错误
    
    if (hasChoiceQuestions && !hasChoiceQuestion) {
        issues.push('练习题使用错误类名 choice-questions (应为 choice-question)');
    }
    if (hasEssayQuestions && !hasEssayQuestion) {
        issues.push('练习题使用错误类名 essay-questions (应为 essay-question)');
    }
    if (hasQuestionCard) {
        issues.push('练习题使用错误结构 question-card (应改为 choice-question/essay-question)');
    }
    if (hasH4InPractice) {
        issues.push('练习题区有 h4 标题 (day001.html无h4)');
    }
    
    // 检查7: JavaScript函数
    const hasInitChoiceQuestions = content.includes('function initChoiceQuestions');
    const hasToggleOption = content.includes('function toggleOption');
    const hasGetSelectedIndices = content.includes('function getSelectedIndices');
    const hasSubmitAll = content.includes('function submitAll');
    const hasShowReference = content.includes('function showReference');
    
    // day001.html的标准函数
    const standardFunctions = ['initChoiceQuestions', 'toggleOption', 'getSelectedIndices', 'submitAll', 'showReference'];
    const missingFunctions = standardFunctions.filter(f => !content.includes(`function ${f}`));
    
    if (missingFunctions.length > 0 && content.includes('<script>')) {
        // 只检查有JavaScript的文件
        issues.push(`缺少标准JavaScript函数: ${missingFunctions.join(', ')}`);
    }
    
    // 检查8: nav-bottom格式
    const navBottomMatch = content.match(/class="nav-bottom"[\s\S]*?<\/div>/);
    if (navBottomMatch) {
        const navContent = navBottomMatch[0];
        // 标准格式: ← 第X天 / 第Y天 →
        if (!navContent.includes('第') || (!navContent.includes('←') && !navContent.includes('→'))) {
            issues.push('nav-bottom格式可能不正确');
        }
    } else {
        issues.push('缺少 nav-bottom');
    }
    
    // 检查9: footer-support位置
    const footerSupportIdx = content.indexOf('<div class="footer-support">');
    const containerCloseIdx = content.lastIndexOf('</div>'); // 最后一个</div>应该是container的关闭
    if (footerSupportIdx !== -1 && containerCloseIdx !== -1) {
        // footer-support应该在最后一个</div>之后
        const lastDivBeforeFooter = content.lastIndexOf('</div>', footerSupportIdx);
        if (footerSupportIdx < lastDivBeforeFooter) {
            issues.push('footer-support位置可能不正确 (应在container关闭之后)');
        }
    }
    
    // 检查10: 表格格式
    const hasTable = content.includes('<table');
    if (hasTable && !content.includes('class="comparison-table"')) {
        issues.push('表格缺少 class="comparison-table"');
    }
    
    if (issues.length > 0) {
        problems.push({
            file: file,
            day: dayNum,
            issues: issues
        });
    }
});

console.log('============================================================');
console.log(`检查结果: ${files.length} 个文件, ${problems.length} 个有问题`);
console.log('============================================================\n');

if (problems.length > 0) {
    console.log('问题文件列表:\n');
    problems.forEach(p => {
        console.log(`${p.file} (第${p.day}天):`);
        p.issues.forEach(issue => {
            console.log(`  - ${issue}`);
        });
        console.log('');
    });
    
    // 保存到文件
    const report = problems.map(p => `${p.file}\t${p.day}\t${p.issues.join('; ')}`).join('\n');
    fs.writeFileSync('strict_check_report.txt', report, 'utf8');
    console.log(`详细报告已保存到: d:\\365培训\\strict_check_report.txt`);
} else {
    console.log('✅ 所有文件都符合day001.html标准格式！');
}
