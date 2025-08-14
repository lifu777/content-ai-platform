#!/usr/bin/env python3
"""
N8N Webhook测试脚本
用于测试自媒体内容生成平台的webhook连接
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

def test_webhook():
    """测试webhook连接"""
    print("🔧 测试N8N Webhook连接...")
    print(f"📡 Webhook URL: {WEBHOOK_URL}")
    print()
    
    # 测试数据 (使用中文平台名称，与N8N工作流匹配)
    test_data = {
        "topic": "人工智能在现代教育中的应用与挑战",
        "platforms": ["微信", "小红书"],
        "requestId": f"test_{int(time.time())}",
        "timestamp": datetime.now().isoformat()
    }
    
    print("📤 发送测试数据:")
    print(json.dumps(test_data, indent=2, ensure_ascii=False))
    print()
    
    try:
        # 发送请求
        print("⏳ 发送请求中...")
        start_time = time.time()
        
        # 先尝试POST请求
        try:
            response = requests.post(
                WEBHOOK_URL,
                json=test_data,
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'ContentAI-Platform/1.0'
                },
                timeout=30,
                verify=False  # 跳过SSL验证
            )
        except Exception as post_error:
            print(f"POST请求失败: {post_error}")
            print("尝试GET请求...")

            # 如果POST失败，尝试GET请求
            response = requests.get(
                WEBHOOK_URL,
                params=test_data,
                headers={
                    'User-Agent': 'ContentAI-Platform/1.0'
                },
                timeout=30,
                verify=False
            )
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        
        print(f"⏱️  响应时间: {duration}秒")
        print(f"📊 状态码: {response.status_code}")
        print(f"📋 响应头: {dict(response.headers)}")
        print()
        
        if response.status_code == 200:
            print("✅ 请求成功!")
            
            # 尝试解析JSON响应
            try:
                response_data = response.json()
                print("📥 响应数据 (JSON):")
                print(json.dumps(response_data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                print("📥 响应数据 (文本):")
                print(response.text)
                
        else:
            print(f"❌ 请求失败: {response.status_code} {response.reason}")
            print("📥 错误响应:")
            print(response.text)
            
    except requests.exceptions.Timeout:
        print("⏰ 请求超时 (30秒)")
        print("💡 建议检查N8N工作流是否正常运行")
        
    except requests.exceptions.ConnectionError:
        print("🌐 连接错误")
        print("💡 建议检查:")
        print("   - 网络连接是否正常")
        print("   - Webhook URL是否正确")
        print("   - N8N服务是否运行")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求异常: {e}")
        
    except Exception as e:
        print(f"❌ 未知错误: {e}")

def test_simple_ping():
    """简单的连通性测试"""
    print("🏓 测试基础连通性...")
    
    try:
        # 测试基础连接
        base_url = WEBHOOK_URL.split('/webhook/')[0]
        response = requests.get(base_url, timeout=10, verify=False)
        print(f"✅ 服务器可达，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 服务器不可达: {e}")

    # 也测试webhook端点
    try:
        response = requests.options(WEBHOOK_URL, timeout=10, verify=False)
        print(f"✅ Webhook端点可达，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ Webhook端点不可达: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 自媒体内容生成平台 - Webhook测试工具")
    print("=" * 60)
    print()
    
    # 基础连通性测试
    test_simple_ping()
    print()
    
    # 完整webhook测试
    test_webhook()
    
    print()
    print("=" * 60)
    print("🎯 测试完成")
    print("💡 如果测试失败，请检查:")
    print("   1. N8N服务是否正常运行")
    print("   2. Webhook URL是否正确")
    print("   3. 工作流是否已激活")
    print("   4. 网络连接是否正常")
    print("=" * 60)
