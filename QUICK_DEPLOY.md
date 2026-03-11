# 服务器部署快速指南 ⚡

## 🎯 最简单的方式（3 步完成）

### 第一步：上传代码到服务器

```bash
# 方式 1: 使用 Git
git clone <你的仓库地址>
cd dev_profile_ai

# 方式 2: 使用 SCP 上传
scp -r ./project user@server:/path/to/project
```

### 第二步：运行一键部署脚本

```bash
# 给脚本执行权限
chmod +x deploy.sh

# 执行部署
./deploy.sh
```

### 第三步：访问网站

```
http://服务器IP:3001
```

---

## 📋 手动部署步骤

如果不想用脚本，可以手动执行：

### 1. 安装 PM2

```bash
npm install -g pm2
```

### 2. 安装 serve

```bash
npm install -g serve
```

### 3. 安装依赖并构建

```bash
npm install --production
npm run build
```

### 4. 启动应用

```bash
pm2 start ecosystem.config.js
```

### 5. 设置开机自启

```bash
pm2 startup
pm2 save
```

---

## 🔧 配置说明

### Vite 配置已修改

`vite.config.ts` 已经配置好：

```typescript
server: {
  host: '0.0.0.0', // 允许所有 IP 访问
 port:3001,      // 端口号
  open: false,     // 不自动打开浏览器
}
```

### PM2 配置文件

`ecosystem.config.js` 配置了：
- 应用名称：dev-profile-ai
- 端口：3001
- 自动重启
- 内存限制：1G

---

## 🛡️ 防火墙配置

### Ubuntu (UFW)

```bash
sudo ufw allow 3001/tcp
sudo ufw reload
```

### CentOS (firewalld)

```bash
sudo firewall-cmd --permanent --add-port=3001/tcp
sudo firewall-cmd --reload
```

### 云服务器

如果是阿里云/腾讯云/AWS：
1. 登录控制台
2. 找到安全组
3. 添加入站规则：端口 3001，协议 TCP，授权对象 0.0.0.0/0

---

## 📊 常用 PM2 命令

```bash
# 查看状态
pm2 status

# 查看日志
pm2 logs dev-profile-ai

# 实时监控
pm2 monit

# 重启应用
pm2 restart dev-profile-ai

# 停止应用
pm2 stop dev-profile-ai

# 删除应用
pm2 delete dev-profile-ai

# 查看所有应用列表
pm2 list
```

---

## 🔄 更新代码

```bash
# 1. 拉取最新代码
git pull

# 2. 重新构建
npm run build

# 3. 重启应用
pm2 restart dev-profile-ai
```

---

## 🐳 Docker 部署（可选）

如果有 Docker 环境：

```bash
# 构建镜像
docker build -t dev-profile-ai.

# 运行容器
docker run -d -p 3001:80 --name profile-app dev-profile-ai
```

---

## ✅ 验证部署

1. **检查进程**
   ```bash
   pm2 status
   # 应该显示 online 状态
   ```

2. **检查端口**
   ```bash
   netstat -tunlp | grep 3001
   # 应该显示监听 0.0.0.0:3001
   ```

3. **本地访问**
   ```bash
   curl http://localhost:3001
   # 应该返回 HTML 内容
   ```

4. **远程访问**
   ```
   浏览器打开：http://服务器IP:3001
   ```

---

## 🆘 故障排查

### 问题 1：无法访问

**检查清单：**
- [ ] 防火墙是否开放 3001 端口
- [ ] 云服务器安全组是否配置
- [ ] PM2 进程是否在运行
- [ ] 端口是否被占用

```bash
# 查看进程
pm2 status

# 查看端口
netstat -tunlp | grep 3001

# 查看防火墙
sudo ufw status
```

### 问题 2：页面空白

**解决方案：**
```bash
# 查看错误日志
pm2 logs dev-profile-ai

# 重启应用
pm2 restart dev-profile-ai
```

### 问题 3：刷新 404

这是 SPA 应用的正常现象，需要配置 Nginx：

```nginx
location/ {
   try_files $uri $uri/ /index.html;
}
```

---

## 📈 性能优化建议

1. **启用 Gzip 压缩** - 减少传输体积
2. **配置 CDN** - 加速静态资源
3. **开启缓存** - 减少重复请求
4. **使用 Nginx** - 反向代理和负载均衡

详细配置见 `DEPLOYMENT_SERVER.md`

---

## 🎉 完成！

部署成功后，你可以：
- ✅ 通过 `http://服务器IP:3001` 访问
- ✅ 应用会自动重启（崩溃时）
- ✅ 服务器重启后自动启动
- ✅ 实时监控应用状态

---

**技术支持**: 查看完整文档 `DEPLOYMENT_SERVER.md`  
**最后更新**: 2026-03-10
