# Vue3 项目 - 快速启动指南

## 🚀 立即开始

### 1. 安装依赖

```bash
cd e:\Computer\Projects\dev_profile_ai
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

浏览器会自动打开：**http://localhost:3000**

### 3. 构建生产版本

```bash
npm run build
```

构建产物在 `dist/` 目录

### 4. 预览生产构建

```bash
npm run preview
```

---

## 📁 项目结构

```
dev_profile_ai/
├── src/
│   ├── main.ts                    # 入口文件
│   ├── App.vue                    # 根组件
│   ├── components/                # 组件
│   │   ├── Navbar.vue            # 导航栏 ✅
│   │   ├── HeroSection.vue       # TODO
│   │   ├── AboutSection.vue      # TODO
│   │   ├── ProjectsSection.vue   # TODO
│   │   ├── SkillsSection.vue     # TODO
│   │   ├── ContactSection.vue    # TODO
│   │   └── Footer.vue            # TODO
│   ├── views/
│   │   └── HomeView.vue          # 主页 ✅
│   ├── stores/
│   │   └── profile.ts            # Profile 数据 ✅
│   ├── router/
│   │   └── index.ts              # 路由 ✅
│   ├── types/
│   │   └── profile.ts            # 类型定义 ✅
│   └── styles/
│       ├── variables.scss        # SCSS 变量 ✅
│       └── main.scss             # 全局样式 ✅
├── package.json                   # 依赖配置 ✅
├── vite.config.ts                # Vite 配置 ✅
├── tsconfig.json                 # TS 配置 ✅
└── index.html                    # HTML 模板 ✅
```

---

## 🎯 NPM 命令

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动开发服务器 |
| `npm run build` | 构建生产版本 |
| `npm run preview` | 预览生产构建 |
| `npm run lint` | ESLint 检查 |

---

## 📝 当前进度

### ✅ 已完成
- [x] 项目基础配置（Vite + TS + SCSS）
- [x] 类型定义系统
- [x] Pinia Store
- [x] 路由配置
- [x] 主页视图框架
- [x] Navbar 组件
- [x] 全局样式和变量

### ⏳ 待完成
- [ ] HeroSection 组件
- [ ] AboutSection 组件
- [ ] ProjectsSection 组件
- [ ] SkillsSection 组件
- [ ] ContactSection 组件
- [ ] Footer 组件
- [ ] profile.md 自动解析脚本

---

## 🔧 故障排除

### 问题 1: 依赖安装失败
```bash
# 清除缓存重试
npm cache clean --force
npm install
```

### 问题 2: 端口被占用
```bash
# 修改 vite.config.ts 中的 port
server: {
  port: 3001  // 改为其他端口
}
```

### 问题 3: TypeScript 报错
```bash
# 检查类型定义
npm run build
```

---

## 📖 详细文档

- [Vue3 重构完整指南](./VUE3_MIGRATION_GUIDE.md)
- [部署指南](./DEPLOY_GUIDE.md)

---

## 💡 提示

1. **热更新**: 修改代码后会自动刷新浏览器
2. **TypeScript**: 使用严格模式，确保类型安全
3. **组件化**: 每个组件职责单一，易于维护
4. **响应式**: 使用 Composition API + `<script setup>`

---

**祝您开发愉快！** 🎉

如有问题，请查看 `VUE3_MIGRATION_GUIDE.md` 获取详细帮助。
