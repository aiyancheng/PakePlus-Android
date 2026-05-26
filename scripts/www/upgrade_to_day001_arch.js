const fs = require('fs');
const path = require('path');

/**
 * 升级脚本：将"静态HTML+correctAnswers"架构升级到"choiceQuestions数组+动态生成"架构
 * 
 * 处理的问题文件：
 * day009, day010, day117, day118, 
 * day154-day161 (8个), day176, day178-day188 (11个)
 * 
 * 总共24个文件
 */

// 需要升级的文件列表
const filesToUpgrade = [
    'day009.html', 'day010.html',
    'day117.html', 'day118.html',
    'day154.html', 'day155.html', 'day156.html', 'day157.html',
    'day158.html', 'day159.html', 'day160.html', 'day161.html',
    'day176.html',
    'day178.html', 'day179.html', 'day180.html', 'day181.html',
    'day182.html', 'day183.html', 'day184.html', 'day185.html',
    'day186.html', 'day187.html', 'day188.html'
];

console.log('============================================================');
console.log('升级脚本：将24个文件升级到day001.html架构');
console.log('============================================================\n');

filesToUpgrade.forEach(filename => {
    console.log(`处理: ${filename}`);
    
    const filepath = path.join('.', filename);
    if (!fs.existsSync(filepath)) {
        console.log(`  [SKIP] 文件不存在`);
        return;
    }
    
    let content = fs.readFileSync(filepath, 'utf8');
    const dayNum = parseInt(filename.match(/day(\d+)/)[1]);
    
    // ============================================================
    // 步骤1: 提取选择题数据，构建choiceQuestions数组
    // ============================================================
    
    // 查找所有选择题（.choice-question）
    const choiceQuestionRegex = /<div class="choice-question">[\s\S]*?<\/div>\s*<\/div>/g;
    const choiceQuestions = [];
    let qIdx = 0;
    
    // 更简单的提取方法：逐题处理
    const questionBlocks = content.match(/<div class="choice-question">[\s\S]*?<\/div>\s*<\/div>/g);
    
    if (!questionBlocks) {
        console.log(`  [WARN] 未找到选择题块`);
        return;
    }
    
    console.log(`  找到 ${questionBlocks.length} 个选择题块`);
    
    // 由于每个文件结构不同，这里需要更复杂的解析逻辑
    // 暂时先跳过，输出需要手工处理的信息
    
    console.log(`  [INFO] ${filename} 需要手工升级（架构差异大）`);
    console.log(`         选择题数量: ${questionBlocks.length}`);
});

console.log('\n============================================================');
console.log('升级脚本完成');
console.log('============================================================');
console.log('\n由于24个文件的JavaScript架构差异很大，无法用统一脚本自动化升级。');
console.log('建议采用手工升级方式，或分批次处理。');
