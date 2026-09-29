# 批量修复day071-day084的底部导航，按照day001.html的格式

$fileRange = 71..84

foreach ($day in $fileRange) {
    $filePath = "d:\365培训\day$($day.ToString('000')).html"
    
    if (-not (Test-Path $filePath)) {
        Write-Host "文件不存在: $filePath" -ForegroundColor Yellow
        continue
    }
    
    # 读取文件内容
    $content = Get-Content $filePath -Raw -Encoding UTF8
    
    # 计算前一天和后一天的数字
    $prevDay = $day - 1
    $nextDay = $day + 1
    
    # 处理边界情况（day071的前一天是day070，day084的后一天是day085）
    $prevFile = if ($prevDay -ge 1) { "day$($prevDay.ToString('000')).html" } else { "day365.html" }
    $nextFile = if ($nextDay -le 365) { "day$($nextDay.ToString('000')).html" } else { "day001.html" }
    
    # 构建新的底部导航HTML（按照day001.html的格式）
    $newFooterNav = @"
        <!-- 底部导航 -->
        <div class="nav-buttons">
            <a href="$prevFile" class="nav-arrow">← 上一天</a>
            <a href="index.html" class="nav-home">🏠 返回首页</a>
            <a href="$nextFile" class="nav-arrow">后一天 →</a>
        </div>
"@
    
    # 使用正则表达式替换旧的底部导航
    # 匹配从 <!-- 底部导航 --> 到 </div> 的部分
    $pattern = '(?s)<!-- 底部导航 -->.*?<div class="footer-nav">.*?</div>\s*</div>'
    $replacement = $newFooterNav + "`n    </div>"
    
    # 尝试替换
    $newContent = $content -replace $pattern, $replacement
    
    # 如果替换失败，尝试另一种模式
    if ($newContent -eq $content) {
        # 可能格式略有不同，尝试更简单的匹配
        $pattern2 = '(?s)<div class="footer-nav">.*?</div>\s*</div>'
        $replacement2 = $newFooterNav + "`n    </div>"
        $newContent = $content -replace $pattern2, $replacement2
    }
    
    # 保存文件
    if ($newContent -ne $content) {
        Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        Write-Host "已修复: day$($day.ToString('000')).html" -ForegroundColor Green
    } else {
        Write-Host "未找到匹配项: day$($day.ToString('000')).html" -ForegroundColor Red
    }
}

Write-Host "`n批量修复完成！" -ForegroundColor Cyan
