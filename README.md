# 🚀 ContentAI - 自媒体内容创作平台

一个基于AI技术的自媒体内容生成平台，支持多平台内容创作。

## ✨ 功能特点

- 🤖 AI驱动的智能内容生成
- 📱 支持多平台内容适配（微信、微博、抖音等）
- 🎨 现代化UI设计，响应式布局
- ⚡ 快速部署，一键生成
- 📋 一键复制生成内容

## 🚀 快速开始

### 本地运行

1. 克隆项目
```bash
git clone https://github.com/yourusername/content-ai-platform.git
cd content-ai-platform
```

2. 启动本地服务器
```bash
# 使用Python
python -m http.server 8000

# 或使用Node.js
npx serve .
```

3. 打开浏览器访问 `http://localhost:8000`

### 部署到Vercel

1. 安装Vercel CLI
```bash
npm i -g vercel
```

2. 登录Vercel
```bash
vercel login
```

3. 部署项目
```bash
vercel
```

## 📁 项目结构

```
content-ai-platform/
├── index.html          # 主页面文件
├── user_version.html   # 用户版本页面
├── styles.css          # 样式文件
├── config.js           # 配置文件
├── package.json        # 项目配置
├── vercel.json         # Vercel部署配置
├── README.md           # 项目说明
└── .gitignore          # Git忽略文件
```

## ⚙️ 配置说明

### Webhook配置

在 `config.js` 文件中配置你的N8N webhook URL：

```javascript
const CONFIG = {
    WEBHOOK_URL: "https://your-n8n-instance.com/webhook/your-webhook-id",
    // 其他配置...
};
```

### 平台配置

支持的自媒体平台：
- 微信公众号
- 微博
- 抖音
- 小红书
- B站
- 知乎

## 🛠️ 技术栈

- HTML5
- CSS3 (现代CSS特性)
- JavaScript (ES6+)
- Vercel (部署平台)

## 📝 使用说明

1. 在文本框中输入你想要创作的主题
2. 选择目标发布平台
3. 点击"生成内容"按钮
4. 等待AI生成内容
5. 复制生成的内容到目标平台

## 🔧 故障排除

### 常见问题

1. **Webhook连接失败**
   - 检查N8N webhook URL是否正确
   - 确认N8N工作流已激活
   - 检查网络连接

2. **内容生成失败**
   - 检查OpenAI API配置
   - 查看N8N执行日志
   - 确认平台名称配置正确

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

如有问题，请通过GitHub Issues联系。
