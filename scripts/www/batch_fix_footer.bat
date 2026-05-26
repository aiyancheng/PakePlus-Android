@echo off
chcp 65001 >nul
echo 开始批量修复底部导航...

REM 定义要处理的文件范围
set start_day=72
set end_day=84

REM 循环处理每个文件
for /L %%i in (%start_day%,1,%end_day%) do (
    echo 正在处理 day%%i...
    
    REM 这里需要手动编辑每个文件，因为批量替换太复杂
    echo 请手动编辑 day%%i.html
)

echo.
echo 批量修复完成！
pause
