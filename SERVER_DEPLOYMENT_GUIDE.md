### 服务器部署完整指南

请通过 SSH 连接到你的 Ubuntu 服务器，然后依次执行以下命令。

#### **第 1 步：准备服务器环境**

1.  **更新系统包列表**：
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2.  **安装 Git 和 Curl**：
    ```bash
    sudo apt install -y git curl
    ```

3.  **安装 Node.js (使用 NVM)**：
    我们使用 `nvm` (Node Version Manager) 来安装 Node.js，这能让你轻松管理和切换 Node 版本。
    ```bash
    # 下载并运行 nvm 安装脚本
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

    # 使 nvm 命令生效 (重要！运行后可能需要重新连接 SSH)
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    
    # 验证 nvm 是否安装成功，如果看到版本号则表示成功
    nvm --version

    # 安装 Node.js v18 并设为默认版本
    nvm install 18
    nvm use 18
    nvm alias default 18
    ```

4.  **全局安装 PM2**：
    `PM2` 是一个强大的进程管理器，能让你的应用在后台持续运行。
    ```bash
    npm install -g pm2
    ```

#### **第 2 步：部署项目代码**

1.  **克隆你的项目代码**：
    在你希望存放项目的目录（例如 `~` 主目录）下，克隆你的 Git 仓库。
    ```bash
    # 确保替换为你的项目仓库地址！
    git clone https://github.com/your-username/your-repo.git
    
    # 进入项目目录 (目录名通常和你的仓库名一致)
    cd your-repo
    ```

#### **第 3 步：构建和运行应用**

1.  **安装所有项目依赖**：
    进入项目目录后，安装 `package.json` 中定义的所有依赖（包括开发依赖）。
    ```bash
    npm install
    ```

2.  **构建项目**：
    这个命令会编译你的代码，并生成一个 `dist` 目录用于生产环境。
    ```bash
    npm run build
    ```

3.  **使用 PM2 启动应用**：
    现在，使用我们之前修复好的 `ecosystem.config.cjs` 文件来启动应用。
    ```bash
    # 确保你位于项目根目录
    pm2 start ecosystem.config.cjs
    ```

4.  **设置 PM2 开机自启**：
    这个命令会生成一个配置，确保在服务器重启后，PM2 管理的应用会自动运行。
    ```bash
    pm2 startup
    # (根据提示，复制并执行它生成的那一行命令)
    pm2 save
    ```

5.  **检查应用状态**：
    ```bash
    pm2 status
    ```
    你应该能看到 `dev-profile-ai` 应用的状态是 `online`，并且 CPU 和内存占用正常。

#### **第 4 步：配置防火墙**

这是允许外网访问的关键一步。你需要告诉服务器的防火墙放行 `3001` 端口。

1.  **允许 3001 端口的 TCP 流量**：
    ```bash
    sudo ufw allow 3001/tcp
    ```

2.  **启用防火墙 (如果尚未启用)**：
    ```bash
    sudo ufw enable
    ```
    *在启用过程中，它可能会提示你 SSH 连接可能会断开，输入 `y` 并回车即可。*

3.  **查看防火墙状态**：
    ```bash
    sudo ufw status
    ```
    你应该能在列表中看到 `3001/tcp` 的状态是 `ALLOW`。

#### **第 5 步：验证部署**

现在，一切准备就绪！打开你的浏览器，访问你的服务器地址：

**`http://47.116.196.136:3001/`**

你应该能看到你的个人主页已经成功运行。
