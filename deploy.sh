#!/bin/bash

# 🚀 ContentAI 自动部署脚本
# 这个脚本会帮你自动部署到GitHub和Vercel

echo "🚀 开始部署 ContentAI 平台..."

# 检查是否安装了必要的工具
check_requirements() {
    echo "📋 检查部署要求..."
    
    # 检查Git
    if ! command -v git &> /dev/null; then
        echo "❌ Git未安装，请先安装Git"
        exit 1
    fi
    
    # 检查Node.js
    if ! command -v node &> /dev/null; then
        echo "❌ Node.js未安装，请先安装Node.js"
        exit 1
    fi
    
    # 检查Vercel CLI
    if ! command -v vercel &> /dev/null; then
        echo "📦 安装Vercel CLI..."
        npm install -g vercel
    fi
    
    echo "✅ 所有要求已满足"
}

# 初始化Git仓库
init_git() {
    echo "🔧 初始化Git仓库..."
    
    if [ ! -d ".git" ]; then
        git init
        echo "✅ Git仓库已初始化"
    else
        echo "ℹ️ Git仓库已存在"
    fi
}

# 创建GitHub仓库
create_github_repo() {
    echo "🌐 创建GitHub仓库..."
    
    read -p "请输入GitHub用户名: " github_username
    read -p "请输入仓库名称 (默认: content-ai-platform): " repo_name
    repo_name=${repo_name:-content-ai-platform}
    
    echo "📝 创建GitHub仓库: $github_username/$repo_name"
    
    # 使用GitHub CLI创建仓库（如果安装了）
    if command -v gh &> /dev/null; then
        gh repo create "$repo_name" --public --description "AI驱动的自媒体内容创作平台"
        echo "✅ GitHub仓库已创建"
    else
        echo "⚠️ 未安装GitHub CLI，请手动创建仓库:"
        echo "   访问 https://github.com/new"
        echo "   仓库名: $repo_name"
        echo "   描述: AI驱动的自媒体内容创作平台"
        echo "   选择: Public"
        read -p "创建完成后按回车继续..."
    fi
}

# 提交代码到GitHub
push_to_github() {
    echo "📤 提交代码到GitHub..."
    
    # 添加所有文件
    git add .
    
    # 提交更改
    git commit -m "🚀 初始提交: AI自媒体内容创作平台"
    
    # 添加远程仓库
    read -p "请输入GitHub仓库URL (例如: https://github.com/username/repo.git): " repo_url
    
    if [ -n "$repo_url" ]; then
        git remote add origin "$repo_url"
        git branch -M main
        git push -u origin main
        echo "✅ 代码已推送到GitHub"
    else
        echo "⚠️ 跳过GitHub推送"
    fi
}

# 部署到Vercel
deploy_to_vercel() {
    echo "🚀 部署到Vercel..."
    
    # 检查是否已登录Vercel
    if ! vercel whoami &> /dev/null; then
        echo "🔐 登录Vercel..."
        vercel login
    fi
    
    # 部署项目
    echo "📦 开始部署..."
    vercel --prod
    
    echo "✅ 部署完成！"
    echo "🌐 你的网站已上线，请查看上面的URL"
}

# 主函数
main() {
    echo "🎉 欢迎使用ContentAI自动部署脚本！"
    echo "=================================="
    
    # 检查要求
    check_requirements
    
    # 初始化Git
    init_git
    
    # 询问是否创建GitHub仓库
    read -p "是否创建GitHub仓库？(y/n): " create_repo
    if [[ $create_repo =~ ^[Yy]$ ]]; then
        create_github_repo
        push_to_github
    fi
    
    # 询问是否部署到Vercel
    read -p "是否部署到Vercel？(y/n): " deploy_vercel
    if [[ $deploy_vercel =~ ^[Yy]$ ]]; then
        deploy_to_vercel
    fi
    
    echo "🎉 部署流程完成！"
    echo "📚 查看README.md了解更多信息"
}

# 运行主函数
main
