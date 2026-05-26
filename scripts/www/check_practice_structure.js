const fs = require('fs');
const path = require('path');

// 查找所有dayXXX.html文件
function findDayFiles(dir) {
    const files = [];
    const items = fs.readdirSync(dir);
    
    for (const item of items) {
        if (item.match(/^day\d+\.html$/)) {
            files.push(path.join(dir, item));
        }
    }
    
    return files.sort();
}

// 检查练习题结构
function checkPracticeStructure(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const issues = [];
    
    // 检查1: choice-questions (应该是 choice-question)
    if (content.includes('class="choice-questions"')) {
        issues.push('使用 choice-questions (应该是 choice-question 单数)');
    }
    
    // 检查2: essay-questions (应该是 essay-question)
    if (content.includes('class="essay-questions"')) {
        issues.push('使用 essay-questions (应该是 essay-question 单数)');
    }
    
    // 检查3: question-card (不是标准结构)
    if (content.includes('class="question-card"')) {
        issues.push('使用 question-card (不是标准结构，应该是 choice-question 或 essay-question)');
    }
    
    // 检查4: h4 标题 (day001.html 没有 h4)
    if (content.includes('<h4>') || content.includes('<h4 ')) {
        issues.push('练习题区有 h4 标题 (day001.html 没有 h4)');
    }
    
    // 检查5: input type="radio" (day001.html 使用动态生成，不是静态 input)
    if (content.includes('type="radio"') || content.includes('type="checkbox"')) {
        issues.push('使用静态 input radio/checkbox (day001.html 使用动态生成选项)');
    }
    
    // 检查6: 独立的提交按钮 (每个题目一个提交按钮，不是统一提交)
    const submitButtons = (content.match(/onclick="checkAnswer\(this\)"/g) || []);
    if (submitButtons.length > 0) {
        issues.push(`有 ${submitButtons.length} 个独立提交按钮 (应该是统一提交按钮 submitAll())`);
    }
    
    // 检查7: 缺少标准 JavaScript 函数
    const standardFunctions = ['initChoiceQuestions', 'toggleOption', 'getSelectedIndices', 'submitAll', 'showReference'];
    const missingFunctions = [];
    
    // 先检查是否是新版架构 (有 choiceQuestions 数组)
    const hasChoiceQuestionsArray = content.includes('const choiceQuestions');
    
    if (hasChoiceQuestionsArray) {
        // 新版架构：应该有标准函数
        for (const func of standardFunctions) {
            if (!content.includes(`function ${func}`)) {
                missingFunctions.push(func);
            }
        }
    } else {
        // 旧版架构：可能有 correctAnswers 对象 + 不同的函数名
        const hasCorrectAnswers = content.includes('const correctAnswers');
        if (hasCorrectAnswers) {
            // 旧版架构，检查是否有 submitAll 或类似的提交函数
            if (!content.includes('function submitAll') && !content.includes('function checkAnswer')) {
                issues.push('旧版架构但缺少提交函数 (submitAll 或 checkAnswer)');
            }
        }
    }
    
    if (missingFunctions.length > 0) {
        issues.push(`缺少标准 JavaScript 函数: ${missingFunctions.join(', ')}`);
    }
    
    return issues;
}

// 主函数
function main() {
    const workspaceDir = 'd:\\365培训';
    const dayFiles = findDayFiles(workspaceDir);
    
    console.log('开始检查所有dayXXX.html文件的练习题结构...\\n');
    console.log(`找到 ${dayFiles.length} 个dayXXX.html文件\\n`);
    
    const problemFiles = [];
    
    for (const file of dayFiles) {
        const fileName = path.basename(file);
        const issues = checkPracticeStructure(file);
        
        if (issues.length > 0) {
            const dayMatch = fileName.match(/day(\d+)\.html/);
            const dayNum = dayMatch ? parseInt(dayMatch[1]) : 0;
            
            problemFiles.push({
                file: fileName,
                day: dayNum,
                issues: issues
            });
        }
    }
    
    // 输出报告
    console.log('========== 练习题结构检查报告 ==========');
    console.log(`总文件数: ${dayFiles.length}`);
    console.log(`有问题文件数: ${problemFiles.length}\\n`);
    
    if (problemFiles.length > 0) {
        console.log('========== 问题文件列表 ==========\\n');
        
        for (const item of problemFiles) {
            console.log(`${item.file} (第${item.day}天):`);
            for (const issue of item.issues) {
                console.log(`  - ${issue}`);
            }
            console.log('');
        }
        
        // 保存到文件
        const reportPath = path.join(workspaceDir, 'practice_structure_check_report.txt');
        let report = '========== 练习题结构检查报告 ==========\\n';
        report += `检查时间: ${new Date().toLocaleString('zh-CN')}\\n`;
        report += `总文件数: ${dayFiles.length}\\n`;
        report += `有问题文件数: ${problemFiles.length}\\n\\n`;
        report += '========== 问题文件列表 ==========\\n\n';
        
        for (const item of problemFiles) {
            report += `${item.file} (第${item.day}天):\n`;
            for (const issue of item.issues) {
                report += `  - ${issue}\n`;
            }
            report += '\n';
        }
        
        fs.writeFileSync(reportPath, report, 'utf8');
        console.log(`\\n详细报告已保存到: ${reportPath}`);
    } else {
        console.log('✅ 所有文件的练习题结构都正确！');
    }
}

main();
