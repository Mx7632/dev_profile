# 服务器部署指南

## 📋 目录

1. [Vite 配置修改](#vite-配置修改)
2. [PM2 进程管理](#pm2-进程管理)
3. [Nginx 反向代理](#nginx-反向代理)
4. [Docker 容器化部署](#docker-容器化部署)
5. [系统服务配置](#系统服务配置)

---

## 🚀 Vite 配置修改

### 修改 vite.config.ts

为了让服务器可以访问，需要配置 host：

```typescript
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    vue(),
  ],
 resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0', // 允许外部访问
   port:3001,       // 指定端口
    open: false       // 不自动打开浏览器
  }
})
```

---

## 📦 方案一：PM2 进程管理（推荐）

### 1. 安装 PM2

```bash
# 全局安装 PM2
npm install -g pm2

# 或者使用 yarn
yarn global add pm2
```

### 2. 构建生产版本

```bash
# 安装生产依赖
npm install --production

# 构建项目
npm run build
```

### 3. 创建 PM2 配置文件

创建 `ecosystem.config.js`：

```javascript
module.exports = {
  apps: [{
   name: 'dev-profile-ai',
    script: 'serve',
    cwd: './dist',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      PORT: 3001,
      NODE_ENV: 'production'
    }
  }]
}
```

### 4. 安装 serve

```bash
npm install -g serve
```

### 5. 启动应用

```bash
# 启动
pm2 start ecosystem.config.js

# 或者直接使用命令
pm2 start npm --name "dev-profile-ai" -- run preview

# 查看状态
pm2 status

# 查看日志
pm2 logs dev-profile-ai

# 重启
pm2 restart dev-profile-ai

# 停止
pm2 stop dev-profile-ai

# 删除
pm2 delete dev-profile-ai
```

### 6. 设置开机自启

```bash
# 生成启动脚本
pm2 startup

# 保存当前应用列表
pm2 save
```

---

## 🌐 方案二：Nginx 反向代理

### 1. 安装 Nginx

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install nginx
```

### 2. 构建项目

```bash
npm run build
```

### 3. 配置 Nginx

编辑 `/etc/nginx/sites-available/dev-profile-ai`：

```nginx
server {
    listen 80;
    server_name your_domain.com;  # 或服务器 IP
    
    root /path/to/your/project/dist;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    # Gzip 压缩
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript 
               application/x-javascript application/xml+rss 
               application/json application/javascript;
    
    # 缓存静态资源
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

### 4. 启用配置

```bash
# 创建软链接
sudo ln -s /etc/nginx/sites-available/dev-profile-ai /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启 Nginx
sudo systemctl restart nginx

# 设置开机自启
sudo systemctl enable nginx
```

---

## 🐳 方案三：Docker 容器化部署

### 1. 创建 Dockerfile

在项目根目录创建 `Dockerfile`：

```dockerfile
# 构建阶段
FROM node:18-alpine as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# 生产阶段
FROM nginx:alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### 2. 创建 nginx.conf

```nginx
server {
    listen 80;
    server_name _;
    
    root /usr/share/nginx/html;
    index index.html;
    
    location/ {
        try_files $uri $uri/ /index.html;
    }
    
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
}
```

### 3. 创建 .dockerignore

```
node_modules
dist
.git
.gitignore
*.md
.qoder
docs
blog
deploy
```

### 4. 构建和运行

```bash
# 构建镜像
docker build -t dev-profile-ai .

# 运行容器
docker run -d -p 80:80 --name profile-app dev-profile-ai

# 或者指定其他端口
docker run -d -p 3001:80 --name profile-app dev-profile-ai
```

### 5. Docker Compose（可选）

创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  app:
    build:
     context: .
      dockerfile: Dockerfile
   ports:
      - "80:80"
    restart: always
    environment:
      - NODE_ENV=production
```

运行：
```bash
docker-compose up -d
```

---

## 🔧 方案四：Systemd 系统服务

### 1. 创建服务文件

创建 `/etc/systemd/system/dev-profile-ai.service`：

```ini
[Unit]
Description=Dev Profile AI Application
Documentation=https://github.com/your-repo
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/usr/bin/npm run preview
Restart=always
RestartSec=10
Environment=NODE_ENV=production
Environment=PORT=3001

# 日志
StandardOutput=journal
StandardError=journal
SyslogIdentifier=dev-profile-ai

[Install]
WantedBy=multi-user.target
```

### 2. 管理服务

```bash
# 重新加载 systemd
sudo systemctl daemon-reload

# 启动服务
sudo systemctl start dev-profile-ai

# 设置开机自启
sudo systemctl enable dev-profile-ai

# 查看状态
sudo systemctl status dev-profile-ai

# 查看日志
sudo journalctl -u dev-profile-ai -f

# 重启服务
sudo systemctl restart dev-profile-ai

# 停止服务
sudo systemctl stop dev-profile-ai
```

---

## 🔐 防火墙配置

### Ubuntu (UFW)

```bash
# 允许 HTTP
sudo ufw allow 80/tcp

# 允许 HTTPS（如果需要）
sudo ufw allow 443/tcp

# 允许特定端口
sudo ufw allow 3001/tcp

# 查看状态
sudo ufw status
```

### CentOS (firewalld)

```bash
# 开放端口
sudo firewall-cmd --permanent --add-port=3001/tcp

# 重新加载
sudo firewall-cmd --reload

# 查看开放的端口
sudo firewall-cmd --list-ports
```

### 云服务器安全组

如果使用阿里云、腾讯云、AWS 等云服务，需要在控制台配置安全组规则：

1. 登录云服务器控制台
2. 找到安全组配置
3. 添加入站规则：
   - 端口：3001（或 80）
   - 协议：TCP
   - 授权对象：0.0.0.0/0（或指定 IP）

---

## 📊 监控和维护

### PM2 监控

```bash
# 实时监控
pm2 monit

# 详细信息
pm2 show dev-profile-ai

# CPU/内存使用
pm2 list

# 集群模式（多实例）
pm2 start ecosystem.config.js -i max
```

### 日志管理

```bash
# PM2 日志轮转
pm2 install pm2-logrotate

# 设置日志大小
pm2 set pm2-logrotate:max_size 10M
pm2 set pm2-logrotate:retain 7
```

---

## ✅ 快速部署流程（推荐）

### 最简单的方式：

```bash
# 1. 安装 PM2
npm install -g pm2

# 2. 安装 serve
npm install -g serve

# 3. 构建项目
npm run build

# 4. 启动应用
pm2 start serve --name "profile" -- dist -l 3001

# 5. 设置开机自启
pm2 startup
pm2 save
```

### 访问地址

```
http://服务器IP:3001
```

---

## 🎯 生产环境优化建议

### 1. 性能优化

- 开启 Gzip 压缩
- 配置 CDN
- 启用浏览器缓存
- 代码分割和懒加载

### 2. 安全加固

- 配置 HTTPS（Let's Encrypt）
- 隐藏服务器信息
- 限制请求频率
- 配置 CSP 策略

### 3. 高可用

- 使用负载均衡
- 多实例部署
- 自动故障转移
- 定期备份

### 4. 监控告警

- 接入监控平台
- 配置告警通知
- 日志分析
- 性能追踪

---

## 🆘 常见问题

### Q1: 无法通过 IP 访问？

**检查清单：**
1. 确认防火墙已开放端口
2. 确认云服务器安全组已配置
3. 确认 vite.config.ts 中 host 设置为 '0.0.0.0'
4. 使用 `netstat -tunlp | grep 3001` 检查端口是否监听

### Q2: 刷新页面 404？

**解决方案：**
确保 Nginx 配置了 `try_files $uri $uri/ /index.html;`

### Q3: PM2 重启后应用丢失？

**解决方案：**
执行 `pm2 save` 和 `pm2 startup` 设置开机自启

### Q4: 如何更新代码？

```bash
# 拉取最新代码
git pull

# 安装依赖
npm install

# 重新构建
npm run build

# 重启应用
pm2 restart all
```

---

## 📞 技术支持

如有问题，请查看：
- [Vue 部署文档](https://cn.vuejs.org/guide/scaling-up/deployment.html)
- [Vite 部署指南](https://cn.vitejs.dev/guide/static-deploy.html)
- [PM2 官方文档](https://pm2.keymetrics.io/docs/usage/quick-start/)

---

**最后更新**: 2026-03-10  
**适用版本**: Vue3 + Vite 5
