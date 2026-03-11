### 手动部署指南 (Ubuntu)

这份指南将引导你完成从获取代码到启动应用的完整过程。

---

#### **第 1 步：环境准备**

首先，确保你的服务器上安装了 `git`、`Node.js` (版本 18 或更高) 和 `npm`。

1.  **检查 Git:**
    ```bash
    git --version
    ```
    如果未安装，请运行：`sudo apt update && sudo apt install git`

2.  **检查 Node.js 和 npm:**
    ```bash
    node -v
    npm -v
    ```
    如果未安装或版本过低，推荐使用 `nvm` (Node Version Manager) 来安装：
    ```bash
    # 安装 nvm
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    # 使 nvm 生效 (可能需要重新登录或打开新的终端)
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    # 安装并使用 Node.js 18
    nvm install 18
    nvm use 18
    ```

#### **第 2 步：获取项目代码**

将你的项目代码克隆到服务器上。

```bash
# 替换为你的项目 Git 仓库地址
git clone <你的项目Git仓库地址>
# 进入项目目录
cd <你的项目目录>
```

#### **第 3 步：安装全局依赖**

`deploy.sh` 脚本会自动安装 `pm2` 和 `serve`，手动部署时我们也需要它们。

1.  **安装 pm2:**
    ```bash
    sudo npm install -g pm2
    ```

2.  **安装 serve:**
    ```bash
    sudo npm install -g serve
    ```

#### **第 4 步：安装项目依赖**

进入你的项目目录，然后安装 `package.json` 中定义的依赖。

```bash
npm install --production
```
*   `--production` 标志会跳过开发环境专用的依赖，减小安装体积。

#### **第 5 步：构建项目**

运行构建命令，这将生成用于生产环境的静态文件，并存放在 `dist` 目录中。

```bash
npm run build
```
*   如果此步骤出错，请仔细查看终端输出的错误信息，这通常是部署失败的根源。

#### **第 6 步：使用 PM2 启动应用**

现在，我们将手动执行 `ecosystem.config.js` 中定义的启动任务。

1.  **确保 `dist` 目录存在**：
    运行 `ls` 命令，确认 `dist` 目录已成功生成。

2.  **停止旧的应用实例 (如果存在)**：
    为了避免冲突，最好先停止并删除任何同名的旧实例。
    ```bash
    pm2 stop dev-profile-ai || true
    pm2 delete dev-profile-ai || true
    ```
    *   `|| true` 可以防止在应用不存在时命令报错。

3.  **启动应用**：
    `pm2` 可以直接使用 `serve` 来托管静态文件目录。
    ```bash
    pm2 start serve dist --name "dev-profile-ai" -- --port 3001
    ```
    *   `serve dist`：告诉 `pm2` 使用 `serve` 命令来托管 `dist` 目录。
    *   `--name "dev-profile-ai"`：为应用命名，方便管理。
    *   `-- --port 3001`：`--` 后面的参数会直接传递给 `serve` 命令，这里是指定端口为 `3001`。

#### **第 7 步：验证部署**

1.  **检查 PM2 状态**：
    ```bash
    pm2 status
    ```
    你应该能看到 `dev-profile-ai` 应用的状态是 `online`。

2.  **查看日志**：
    如果应用状态不是 `online`，或者你想确认是否有错误，可以查看日志。
    ```bash
    pm2 logs dev-profile-ai
    ```

3.  **保存 PM2 进程列表**：
    为了确保服务器重启后应用能自动恢复，运行：
    ```bash
    pm2 save
    ```

#### **第 8 步：访问你的应用**

现在，你可以通过服务器的 IP 地址和端口 `3001` 来访问你的个人主页了。

`http://<你的服务器IP>:3001`
