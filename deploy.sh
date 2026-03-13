#!/bin/bash

# ==========================================
# 一键部署脚本 - Dev Profile AI
# ==========================================

echo "🚀 开始部署 Dev Profile AI..."

# 1. 检查 Node.js
echo "📦 检查 Node.js..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未安装，请先安装 Node.js 18+"
    exit 1
fi
echo "✅ Node.js 版本：$(node -v)"

# 2. 检查 PM2
echo "📦 检查 PM2..."
if ! command -v pm2 &> /dev/null; then
    echo "⚠️  PM2 未安装，正在安装..."
    npm install -g pm2
fi
echo "✅ PM2 版本：$(pm2 -v)"

# 3. 检查 serve
echo "📦 检查 serve..."
if ! command -v serve &> /dev/null; then
    echo "⚠️  serve 未安装，正在安装..."
    npm install -g serve
fi
echo "✅ serve 已安装"

# 4. 安装依赖（包含开发依赖，保证可以运行构建工具）
echo "📦 安装项目依赖..."
npm install

# 5. 构建项目
echo "🔨 构建项目..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ 构建失败，请检查错误信息"
    exit 1
fi
echo "✅ 构建完成"

# 6. 停止旧应用
echo "🛑 停止旧应用..."
pm2 stop dev-profile-ai 2>/dev/null || true
pm2 delete dev-profile-ai 2>/dev/null || true

# 7. 启动新应用
echo "🚀 启动应用..."
pm2 start ecosystem.config.cjs

# 8. 保存 PM2 配置
echo "💾 保存 PM2 配置..."
pm2 save

# 9. 显示状态
echo "📊 应用状态:"
pm2 status

# 10. 输出访问地址（优先公网 IP）
echo ""
echo "🌐 访问地址:"
PUBLIC_IP=""
if command -v curl &> /dev/null; then
  PUBLIC_IP=$(curl -fsS --max-time 5 https://api.ipify.org 2>/dev/null || true)
fi
if [ -n "$PUBLIC_IP" ]; then
  echo "   http://$PUBLIC_IP:3001"
else
  IP=$(hostname -I | awk '{print $1}')
  echo "   http://$IP:3001"
fi
echo "   http://localhost:3001"
echo ""
echo "🎉 部署完成！"
echo ""
echo "📋 常用命令:"
echo "   pm2 status          - 查看状态"
echo "   pm2 logs            - 查看日志"
echo "   pm2 restart all     - 重启应用"
echo "   pm2 stop all        - 停止应用"
echo "   pm2 monit           - 监控面板"
echo ""
