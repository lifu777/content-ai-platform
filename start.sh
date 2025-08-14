#!/bin/bash

# 自媒体内容生成平台启动脚本

echo "🚀 启动自媒体内容生成平台..."
echo ""

# 检查Python是否安装
if command -v python3 &> /dev/null; then
    echo "✅ 找到 Python3"
    python3 start-server.py
elif command -v python &> /dev/null; then
    echo "✅ 找到 Python"
    python start-server.py
else
    echo "❌ 未找到Python，尝试其他方式..."
    
    # 检查Node.js
    if command -v npx &> /dev/null; then
        echo "✅ 找到 Node.js，使用 serve"
        npx serve . -p 8000
    elif command -v node &> /dev/null; then
        echo "✅ 找到 Node.js，使用 http-server"
        npx http-server . -p 8000
    else
        echo "❌ 未找到Python或Node.js"
        echo "请安装Python或Node.js后重试"
        echo ""
        echo "或者直接在浏览器中打开 index.html 文件"
        echo "文件路径: $(pwd)/index.html"
        
        # 尝试直接打开文件
        if command -v open &> /dev/null; then
            echo "🌐 尝试直接打开文件..."
            open index.html
        fi
    fi
fi
