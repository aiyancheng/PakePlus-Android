const fs = require('fs');
const path = require('path');

const TRAINING_DIR = 'd:\\365培训';
const DAY_PATTERN = /^day(\d+)\.html$/;

// 修复单个文件的表格
function fixFileTables(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;
    
    // 查找所有<table标签，修复class
    // 匹配 <table 后面可能跟着其他属性，然后是 >
    const tableRegex = /<table([^>]*)>/g;
    
    content = content.replace(tableRegex, (match, attrs) => {
        // 检查是否已经有class="comparison-table"
        if (attrs.includes('class="comparison-table"') || attrs.includes("class='comparison-table'")) {
            return match; // 已经有正确的class，不需要修改
        }
        
        // 需要添加或修改class
        modified = true;
        
        // 检查是否已有class属性
        const classMatch = attrs.match(/class\s*=\s*["']([^"']*)["']/);
        if (classMatch) {
            // 已有class，替换为comparison-table
            const newAttrs = attrs.replace(
                /class\s*=\s*["'][^"']*["']/,
                'class="comparison-table"'
            );
            return '<table' + newAttrs + '>';
        } else {
            // 没有class，添加class="comparison-table"
            // 在<table后面、其他属性之前添加class
            const newAttrs = ' class="comparison-table"' + attrs;
            return '<table' + newAttrs + '>';
        }
    });
    
    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        return true;
    }
    return false;
}

// 主函数
function main() {
    console.log('开始修复表格格式...');
    console.log('目标: 所有<table>标签添加class="comparison-table"');
    console.log('');
    
    const files = fs.readdirSync(TRAINING_DIR)
        .filter(f => DAY_PATTERN.test(f))
        .sort((a, b) => {
            const numA = parseInt(a.match(DAY_PATTERN)[1]);
            const numB = parseInt(b.match(DAY_PATTERN)[1]);
            return numA - numB;
        });
    
    console.log('找到 ' + files.length + ' 个dayXXX.html文件');
    console.log('');
    
    let fixedCount = 0;
    const fixedFiles = [];
    
    for (const file of files) {
        const filePath = path.join(TRAINING_DIR, file);
        try {
            const fixed = fixFileTables(filePath);
            if (fixed) {
                fixedCount++;
                fixedFiles.push(file);
            }
        } catch (err) {
            console.error('处理 ' + file + ' 时出错:', err.message);
        }
    }
    
    console.log('========== 修复完成 ==========');
    console.log('总共修复了 ' + fixedCount + ' 个文件');
    console.log('');
    
    if (fixedFiles.length > 0) {
        console.log('修复的文件列表（前20个）:');
        for (let i = 0; i < Math.min(20, fixedFiles.length); i++) {
            console.log('  - ' + fixedFiles[i]);
        }
        if (fixedFiles.length > 20) {
            console.log('  ... 还有 ' + (fixedFiles.length - 20) + ' 个文件');
        }
    }
    
    // 保存修复报告
    const reportPath = path.join(TRAINING_DIR, 'table_fix_report.txt');
    const reportLines = [
        '表格格式修复报告',
        '生成时间: ' + new Date().toLocaleString('zh-CN'),
        '',
        '总共修复了 ' + fixedCount + ' 个文件',
        '',
        '========== 修复的文件列表 ==========',
        ''
    ];
    
    for (const f of fixedFiles) {
        reportLines.push(f);
    }
    
    fs.writeFileSync(reportPath, reportLines.join('\n'), 'utf8');
    console.log('');
    console.log('详细报告已保存到: ' + reportPath);
}

main();
