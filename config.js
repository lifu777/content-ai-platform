// 自媒体内容生成平台配置文件

const CONFIG = {
    // N8N Webhook配置
    WEBHOOK_URL: 'https://n8nprd.aifunbox.com/webhook/48ef356d-4393-46af-ab0e-2bbc93801629', // Production webhook URL
    
    // API配置
    API_TIMEOUT: 60000, // 60秒超时 (AI生成需要更长时间)
    RETRY_ATTEMPTS: 3,   // 重试次数
    
    // 支持的平台配置 (与N8N工作流中的AI Agent完全匹配)
    PLATFORMS: [
        {
            id: 'Twitter',
            name: 'Twitter',
            agent: 'X Agent',
            icon: '🐦',
            description: '简洁明了的推文格式'
        },
        {
            id: '小红书',
            name: '小红书',
            agent: 'Rednote Agent',
            icon: '📱',
            description: '年轻化、生活化的内容风格'
        },
        {
            id: '朋友圈',
            name: '朋友圈',
            agent: 'Wechat Agent',
            icon: '💬',
            description: '适合朋友圈分享的内容格式'
        }
    ],
    
    // 内容验证规则
    VALIDATION: {
        TOPIC_MIN_LENGTH: 2,     // 降低到2个字符，支持简短主题
        TOPIC_MAX_LENGTH: 500,
        MIN_PLATFORMS: 1,
        MAX_PLATFORMS: 3
    },
    
    // UI配置
    UI: {
        ANIMATION_DURATION: 300,
        SUCCESS_MESSAGE_DURATION: 2000,
        ERROR_MESSAGE_DURATION: 5000
    },
    
    // 错误信息
    ERROR_MESSAGES: {
        NETWORK_ERROR: '网络连接失败，请检查网络后重试',
        SERVER_ERROR: '服务暂时不可用，请稍后重试',
        VALIDATION_ERROR: '输入信息不完整，请检查后重试',
        TIMEOUT_ERROR: '请求超时，请重试',
        UNKNOWN_ERROR: '发生未知错误，请重试'
    },
    
    // 成功信息
    SUCCESS_MESSAGES: {
        CONTENT_GENERATED: '内容生成成功！',
        CONTENT_COPIED: '内容已复制到剪贴板',
        CONTENT_SAVED: '内容已保存到历史记录'
    }
};

// 导出配置（如果使用模块化）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}

// 全局配置（用于HTML页面）
window.CONFIG = CONFIG;
