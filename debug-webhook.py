#!/usr/bin/env python3
"""
N8N Webhook调试脚本
尝试不同的数据格式来找出工作流期望的格式
"""

import requests
import json
import time
from datetime import datetime
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置
WEBHOOK_URL = "https://n8nprd.aifunbox.com/webhook/48ef356d-4393-46af-ab0e-2bbc93801629"

def test_format(test_name, data):
    """测试特定的数据格式"""
    print(f"\n🧪 测试 {test_name}")
    print("=" * 40)
    print("发送数据:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(
            WEBHOOK_URL,
            json=data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'ContentAI-Debug/1.0'
            },
            timeout=30,
            verify=False
        )
        
        print(f"\n状态码: {response.status_code}")
        
        try:
            response_data = response.json()
            print("响应数据:")
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
        except:
            print("响应文本:")
            print(response.text)
            
        return response.status_code == 200
        
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return False

def main():
    print("🔍 N8N Webhook调试工具")
    print("=" * 60)
    
    # 测试不同的数据格式
    test_cases = [
        # 格式1：最简单的格式
        ("最简格式", {
            "topic": "AI测试",
            "platforms": ["微信"]
        }),
        
        # 格式2：英文平台名
        ("英文平台名", {
            "topic": "AI测试",
            "platforms": ["wechat"]
        }),
        
        # 格式3：单个平台字符串
        ("单个平台字符串", {
            "topic": "AI测试",
            "platforms": "微信"
        }),
        
        # 格式4：添加更多字段
        ("完整格式", {
            "topic": "人工智能在现代教育中的应用",
            "platforms": ["微信"],
            "requestId": f"debug_{int(time.time())}",
            "timestamp": datetime.now().isoformat()
        }),
        
        # 格式5：尝试不同的字段名
        ("不同字段名", {
            "content": "人工智能在现代教育中的应用",
            "platform": ["微信"]
        }),
        
        # 格式6：嵌套格式
        ("嵌套格式", {
            "data": {
                "topic": "人工智能在现代教育中的应用",
                "platforms": ["微信"]
            }
        }),
        
        # 格式7：简单文本
        ("纯文本", "人工智能在现代教育中的应用"),
        
        # 格式8：空数据测试
        ("空数据", {}),
    ]
    
    success_count = 0
    
    for test_name, data in test_cases:
        if test_format(test_name, data):
            success_count += 1
            print("✅ 成功!")
            break  # 找到成功的格式就停止
        else:
            print("❌ 失败")
    
    print("\n" + "=" * 60)
    print(f"🎯 测试完成，成功: {success_count}/{len(test_cases)}")
    
    if success_count == 0:
        print("\n💡 建议检查:")
        print("1. N8N工作流是否已激活")
        print("2. OpenAI API凭据是否有效")
        print("3. 工作流节点配置是否正确")
        print("4. 查看N8N执行日志获取详细错误信息")

if __name__ == "__main__":
    main()
