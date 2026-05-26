const fs = require('fs');
const path = require('path');

// 配置
const TRAINING_DIR = 'd:\\365培训';
const DAY_PATTERN = /^day(\d+)\.html$/;

// 读取day001.html作为标准格式参考
function loadStandardFormat() {
    const day001Path = path.join(TRAINING_DIR, 'day001.html');
    const content = fs.readFileSync(day001Path, 'utf8');
    return content;
}

// 检查单个文件
function checkFile(filePath) {
    const fileName = path.basename(filePath);
    const match = fileName.match(DAY_PATTERN);
    if (!match) return null;
    
    const dayNum = parseInt(match[1]);
    const content = fs.readFileSync(filePath, 'utf8');
    
    const issues = [];
    
    // 1. 检查DOCTYPE和html标签
    if (!content.includes('<!DOCTYPE html>')) {
        issues.push('缺少DOCTYPE声明');
    }
    if (!content.includes('<html lang="zh-CN">') && !content.includes("<html lang='zh-CN'>")) {
        issues.push('html标签lang属性可能不正确');
    }
    
    // 2. 检查head部分
    if (!content.includes('<meta charset="UTF-8">')) {
        issues.push('缺少UTF-8 meta标签');
    }
    if (!content.includes('<meta name="viewport" content="width=device-width, initial-scale=1.0">')) {
        issues.push('缺少viewport meta标签');
    }
    if (!content.includes('<link rel="stylesheet" href="training-styles.css">')) {
        issues.push('缺少training-styles.css链接');
    }
    
    // 3. 检查页面标题格式
    const titlePattern = new RegExp(`<title>第${dayNum}天 \\| .+ - 365天眼镜门店员工晋级培训</title>`);
    if (!titlePattern.test(content)) {
        issues.push('标题格式可能不正确');
    }
    
    // 4. 检查container div
    if (!content.includes('<div class="container">')) {
        issues.push('缺少container div');
    }
    
    // 5. 检查page-header
    if (!content.includes('<div class="page-header">')) {
        issues.push('缺少page-header div');
    }
    if (!content.includes(`<div class="day-number">第 ${dayNum} 天</div>`)) {
        issues.push('day-number格式可能不正确');
    }
    
    // 6. 检查进度条
    if (!content.includes('<div class="progress-bar-container">')) {
        issues.push('缺少progress-bar-container');
    }
    
    // 7. 检查learning-card
    if (!content.includes('<div class="learning-card">')) {
        issues.push('缺少learning-card div');
    }
    
    // 8. 检查practice-section
    if (!content.includes('<div class="practice-section">')) {
        issues.push('缺少practice-section div');
    }
    
    // 9. 检查底部导航
    if (!content.includes('<div class="nav-bottom">')) {
        issues.push('缺少nav-bottom div');
    }
    
    // 10. 检查底部技术支持署名
    if (!content.includes('技术支持：闫胜君视光工作室')) {
        issues.push('缺少技术支持署名或内容不正确');
    }
    
    // 11. 检查JavaScript函数 - 接受多架构和函数名变体
    // 架构1（新版/day001标准）：initChoiceQuestions, toggleOption, getSelectedIndices, submitAll, showReference
    // 架构2（旧版变体A）：submitAll, showReference, toggleAnswer
    // 架构3（旧版变体B）：checkAnswer, toggleAnswer（day085-104等）
    // 架构4（其他变体）：submit_all, show_reference等
    
    // 检查提交函数（多种可能的函数名）
    const hasSubmitFunc = content.includes('function submitAll') || 
                        content.includes('function checkAnswer') || 
                        content.includes('function submit_all') ||
                        content.includes('function checkQuestion');
    
    // 检查显示参考答案函数（多种可能的函数名）
    const hasShowRefFunc = content.includes('function showReference') || 
                          content.includes('function toggleAnswer') || 
                          content.includes('function show_answer') ||
                          content.includes('function toggleAnswer');
    
    // 检查新架构特有函数
    const hasNewArch = content.includes('function initChoiceQuestions') && 
                      content.includes('function toggleOption') && 
                      content.includes('function getSelectedIndices');
    
    // 如果没有任何有效的JavaScript架构，才报告问题
    if (!hasNewArch && !hasSubmitFunc && !hasShowRefFunc) {
        // 完全没有JavaScript功能
        if (!hasSubmitFunc) {
            issues.push('缺少JavaScript提交函数(submitAll/checkAnswer等)');
        }
        if (!hasShowRefFunc) {
            issues.push('缺少JavaScript显示参考答案函数(showReference/toggleAnswer等)');
        }
    }
    
    // 12. 检查表格格式 - 应该使用class="comparison-table"
    const tableMatches = content.match(/<table[^>]*>/g);
    if (tableMatches) {
        for (const tableTag of tableMatches) {
            if (!tableTag.includes('class="comparison-table"') && !tableTag.includes("class='comparison-table'")) {
                issues.push('表格未使用class="comparison-table"');
                break; // 只报告一次
            }
        }
    }
    
    return {
        fileName,
        dayNum,
        issues,
        content
    };
}

// 主函数
function main() {
    console.log('开始检查所有dayXXX.html文件...');
    console.log('标准格式参考: day001.html');
    console.log('表格格式参考: day026.html (class="comparison-table")');
    console.log('');
    
    const files = fs.readdirSync(TRAINING_DIR)
        .filter(f => DAY_PATTERN.test(f))
        .sort((a, b) => {
            const numA = parseInt(a.match(DAY_PATTERN)[1]);
            const numB = parseInt(b.match(DAY_PATTERN)[1]);
            return numA - numB;
        });
    
    console.log(`找到 ${files.length} 个dayXXX.html文件`);
    console.log('');
    
    const results = [];
    const problemFiles = [];
    
    for (const file of files) {
        const filePath = path.join(TRAINING_DIR, file);
        const result = checkFile(filePath);
        if (result) {
            results.push(result);
            if (result.issues.length > 0) {
                problemFiles.push(result);
            }
        }
    }
    
    // 输出报告
    console.log('========== 检查报告 ==========');
    console.log(`总文件数: ${results.length}`);
    console.log(`有问题文件数: ${problemFiles.length}`);
    console.log('');
    
    if (problemFiles.length > 0) {
        console.log('========== 问题文件列表 ==========');
        for (const pf of problemFiles) {
            console.log(`\n${pf.fileName} (第${pf.dayNum}天):`);
            for (const issue of pf.issues) {
                console.log(`  - ${issue}`);
            }
        }
    } else {
        console.log('✅ 所有文件格式正确！');
    }
    
    // 保存详细报告到文件
    const reportPath = path.join(TRAINING_DIR, 'format_check_report.txt');
    const reportLines = [
        '365天培训文件格式检查报告',
        '生成时间: ' + new Date().toLocaleString('zh-CN'),
        '标准格式参考: day001.html',
        '表格格式参考: day026.html',
        '',
        `总文件数: ${results.length}`,
        `有问题文件数: ${problemFiles.length}`,
        '',
        '========== 问题详情 ==========',
    ];
    
    for (const pf of problemFiles) {
        reportLines.push('');
        reportLines.push(`${pf.fileName} (第${pf.dayNum}天):`);
        for (const issue of pf.issues) {
            reportLines.push(`  - ${issue}`);
        }
    }
    
    fs.writeFileSync(reportPath, reportLines.join('\n'), 'utf8');
    console.log('');
    console.log(`详细报告已保存到: ${reportPath}`);
}

main();
