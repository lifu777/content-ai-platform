#!/usr/bin/env python3
"""
简单的HTTP服务器启动脚本
用于本地测试自媒体内容生成平台
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# 配置
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """自定义HTTP请求处理器，添加CORS支持"""
    
    def end_headers(self):
        # 添加CORS头部
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    # 确保在正确的目录中运行
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"🚀 启动自媒体内容生成平台...")
    print(f"📁 工作目录: {os.getcwd()}")
    print(f"🌐 服务器地址: http://{HOST}:{PORT}")
    print(f"📱 主页面: http://{HOST}:{PORT}/index.html")
    print(f"🔧 测试工具: http://{HOST}:{PORT}/webhook-test.html")
    print(f"📖 使用说明: http://{HOST}:{PORT}/README.md")
    print()
    
    try:
        # 创建服务器
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print(f"✅ 服务器已启动在 http://{HOST}:{PORT}")
            print("💡 按 Ctrl+C 停止服务器")
            print("🔄 修改文件后刷新浏览器即可看到更新")
            print()
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://{HOST}:{PORT}/index.html')
                print("🌐 已自动打开浏览器")
            except Exception as e:
                print(f"⚠️  无法自动打开浏览器: {e}")
                print(f"请手动访问: http://{HOST}:{PORT}/index.html")
            
            print()
            print("=" * 50)
            print("服务器日志:")
            print("=" * 50)
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用")
            print(f"💡 请尝试使用其他端口或停止占用该端口的程序")
            print(f"🔍 查看占用进程: lsof -i :{PORT}")
        else:
            print(f"❌ 启动服务器失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
