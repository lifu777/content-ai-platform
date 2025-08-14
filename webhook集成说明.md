# N8N Webhook 集成说明

## 1. 修改内容概述

我已经将您的N8N工作流从表单触发器改为webhook触发器，以便与网页应用集成。

## 2. 主要修改

### 2.1 触发器更改
- **原来**: `formTrigger` (表单触发器)
- **现在**: `webhook` (Webhook触发器)
- **路径**: `/generate-content`
- **方法**: POST

### 2.2 数据格式调整
- **原来**: 表单字段 `保险主题` 和 `创作平台`
- **现在**: JSON格式 `topic` 和 `platforms`

### 2.3 新增响应节点
- 添加了 `Webhook Response` 节点
- 返回标准化的JSON响应格式

## 3. API接口规范

### 3.1 请求格式
```json
POST /webhook/generate-content
Content-Type: application/json

{
  "topic": "人工智能在保险行业的应用",
  "platforms": ["小红书", "微信朋友圈", "Twitter"]
}
```

### 3.2 响应格式
```json
{
  "success": true,
  "data": {
    "content": "生成的内容...",
    "topic": "人工智能在保险行业的应用",
    "platforms": ["小红书", "微信朋友圈", "Twitter"],
    "timestamp": "2024-08-14T07:54:00.000Z"
  }
}
```

## 4. 网页端集成示例

### 4.1 JavaScript调用示例
```javascript
async function generateContent(topic, platforms) {
  try {
    const response = await fetch('YOUR_N8N_WEBHOOK_URL/generate-content', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        topic: topic,
        platforms: platforms
      })
    });
    
    const result = await response.json();
    
    if (result.success) {
      return result.data;
    } else {
      throw new Error('生成失败');
    }
  } catch (error) {
    console.error('API调用失败:', error);
    throw error;
  }
}

// 使用示例
generateContent('人工智能在保险行业的应用', ['小红书', '微信朋友圈'])
  .then(data => {
    console.log('生成的内容:', data.content);
  })
  .catch(error => {
    console.error('错误:', error);
  });
```

### 4.2 React组件示例
```jsx
import React, { useState } from 'react';

function ContentGenerator() {
  const [topic, setTopic] = useState('');
  const [platforms, setPlatforms] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const data = await generateContent(topic, platforms);
      setResult(data);
    } catch (error) {
      alert('生成失败: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea 
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="请输入主题..."
      />
      
      <div>
        {['小红书', '微信朋友圈', 'Twitter'].map(platform => (
          <label key={platform}>
            <input
              type="checkbox"
              checked={platforms.includes(platform)}
              onChange={(e) => {
                if (e.target.checked) {
                  setPlatforms([...platforms, platform]);
                } else {
                  setPlatforms(platforms.filter(p => p !== platform));
                }
              }}
            />
            {platform}
          </label>
        ))}
      </div>
      
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? '生成中...' : '生成内容'}
      </button>
      
      {result && (
        <div>
          <h3>生成结果:</h3>
          <pre>{result.content}</pre>
        </div>
      )}
    </div>
  );
}
```

## 5. 部署步骤

### 5.1 N8N部署
1. 将修改后的JSON文件导入到N8N
2. 确保所有凭据配置正确（OpenAI API、Google Drive等）
3. 激活工作流
4. 记录webhook URL

### 5.2 网页部署
1. 开发前端应用
2. 配置N8N webhook URL
3. 处理CORS问题（如果需要）
4. 部署到服务器

## 6. 测试建议

### 6.1 API测试
使用Postman或curl测试webhook：
```bash
curl -X POST "YOUR_N8N_WEBHOOK_URL/generate-content" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "测试主题",
    "platforms": ["小红书"]
  }'
```

### 6.2 集成测试
1. 测试不同平台组合
2. 测试错误处理
3. 测试响应时间
4. 测试并发请求

## 7. 注意事项

### 7.1 安全考虑
- 考虑添加API密钥验证
- 限制请求频率
- 验证输入数据

### 7.2 错误处理
- 网络超时处理
- N8N工作流执行失败处理
- 无效输入处理

### 7.3 性能优化
- 考虑添加缓存机制
- 优化工作流执行时间
- 监控API响应时间
