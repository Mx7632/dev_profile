# Profile.md 自动解析脚本使用指南

## 📋 概述

本指南介绍如何将 `profile.md` Markdown 文件自动解析为 JSON 数据，供 Vue3 前端应用使用。

---

## 🎯 方案选择

### 方案一：Python 脚本 (推荐) ⭐

**优点：**
- ✅ 代码简洁易读
- ✅ 正则表达式强大
- ✅ 跨平台兼容

**缺点：**
- ❌ 需要安装 Python 环境

### 方案二：Node.js 脚本

**优点：**
- ✅ 与前端技术栈一致
- ✅ 无需额外安装（已有 Node.js）

**缺点：**
- ❌ 正则表达式稍复杂

---

## 🔧 使用方法

### Python 版本

1. **确保已安装 Python 3.6+**
   ```bash
   python --version
   ```

2. **运行脚本**
   ```bash
   python parse_profile.py
   ```

3. **查看输出**
   - 生成文件：`src/data/profile.json`
   - 终端显示解析统计信息

### Node.js 版本

1. **确保已安装 Node.js 14+**
   ```bash
  node --version
   ```

2. **运行脚本**
   ```bash
  node parse_profile.mjs
   ```

3. **查看输出**
   - 生成文件：`src/data/profile.json`

---

## 📊 生成的 JSON 数据结构

```json
{
  "meta": {
    "version": "1.0.0",
    "generatedAt": "2025-03-10T15:30:00.000Z",
    "source": "profile.md"
  },
  "basic": {
    "name": "李柄科",
    "role": "后端开发工程师 / AI 开发爱好者",
    "greeting": "// Hello World",
    "bio": "南京航空航天大学...",
    "status": "求职中 🚀",
    "avatar": "vibe_images/..."
  },
  "contact": {
    "email": "limx7632@gmail.com",
    "github": "https://github.com/Mx7632",
    "blog": "https://blog.limxbyte.sbs"
  },
  "about": {
    "education": "南京航空航天大学 | CS 本科",
    "highlights": ["1 段后端实习经历", "字节工程训练营"],
    "description": "我是一名即将毕业..."
  },
  "projects": [
    {
      "id": 1,
      "name": "RAG 知识库",
      "type": "实习项目",
      "description": "参与构建基于 RAG...",
      "solution": "采用 Redis bitmap...",
      "techStack": ["Spring Boot", "Spring Security", ...],
      "icon": "fa-code",
      "color": "linear-gradient(...)"
    }
  ],
  "skills": [
    {
      "name": "编程语言",
      "icon": "fa-code",
      "items": [
        {
          "name": "Java",
          "level": 90,
          "color": "linear-gradient(...)"
        }
      ]
    }
  ]
}
```

---

## 🚀 集成到 Vue3 应用

### 方法 1: 直接导入 JSON

```typescript
// src/stores/profile.ts
import profileData from '../data/profile.json'

export const useProfileStore = defineStore('profile', () => {
  const profile = ref(profileData)
  
  const getName = computed(() => profile.value.basic.name)
  const getProjects = computed(() => profile.value.projects)
  
 return {
   profile,
    getName,
    getProjects,
    // ...其他 getter
  }
})
```

### 方法 2: 运行时加载

```typescript
// src/stores/profile.ts
export const useProfileStore = defineStore('profile', () => {
  const profile = ref(null)
  
  async function loadProfile() {
    const response = await fetch('/src/data/profile.json')
   profile.value = await response.json()
  }
  
  onMounted(() => {
    loadProfile()
  })
  
 return {
   profile,
    loadProfile
  }
})
```

---

## 🔄 自动化工作流

### 开发时自动解析

在 `package.json` 中添加脚本：

```json
{
  "scripts": {
    "parse-profile": "node parse_profile.mjs",
    "dev": "npm run parse-profile && vite",
    "build": "npm run parse-profile && vite build"
  }
}
```

这样每次启动开发服务器或构建时都会自动解析最新的 profile.md。

### Git Hooks 自动解析

创建 `.git/hooks/pre-commit`:

```bash
#!/bin/bash
echo "🔄 自动解析 profile.md..."
node parse_profile.mjs
git add src/data/profile.json
```

这样每次提交前都会自动更新 JSON 文件。

---

## 📝 自定义配置

### 修改解析规则

编辑解析脚本中的正则表达式：

```javascript
// 示例：修改姓名提取规则
const patterns = {
  name: /\*\*姓名 \(Name\):\*\*\s*(.+)/,
  // 可以改为更宽松的匹配
  name: /\*\*姓名.*?:\s*(.+)/,
}
```

### 添加新字段

1. 在 `profile.md` 中添加新字段
2. 在解析脚本中添加对应的正则表达式
3. 在 TypeScript 类型定义中添加接口

---

## 🛠️ 故障排除

### 问题 1: 找不到文件

**错误：** `FileNotFoundError: profile.md`

**解决：** 确保在项目根目录运行脚本

### 问题 2: 解析结果为空

**检查：**
- profile.md 格式是否正确
- 章节标题是否匹配（如 `## 1. 基础信息`）
- 正则表达式是否匹配当前格式

### 问题 3: JSON 格式错误

**调试：**
```bash
# 使用 jq 验证 JSON 格式
cat src/data/profile.json | jq .
```

---

## 📦 完整示例

### 完整的 profile.md 片段

```markdown
## 1. 基础信息

- **姓名 (Name):** 张三
- **职位 (Role):** 全栈开发工程师
- **标语 (Greeting):** // Hello World
- **简介 (Bio):** 热爱编程...
- **状态 (Status):** 求职中
- **头像路径:** images/avatar.jpg

## 2. 联系方式

- **Email:** zhangsan@example.com
- **GitHub:** https://github.com/zhangsan
- **Blog:** https://zhangsan.com
```

### 运行结果

```bash
$ python parse_profile.py
============================================================
🚀 Profile Markdown 解析器
============================================================

📖 正在解析 profile.md...
💾 正在生成 JSON 文件...

============================================================
✅ 解析完成！
============================================================
📊 数据统计:
   - 基本信息：✓
   - 联系方式：✓
   - 关于我：✓
   - 项目数量：4
   - 技能类别：5

📁 输出文件：src/data/profile.json

🎉 现在可以在前端中使用这些数据了！
============================================================
```

---

## ✨ 最佳实践

1. **保持 profile.md 格式一致**
   - 使用标准的 Markdown 语法
   - 遵循既定的字段命名规范

2. **版本控制**
   - 将 profile.md 纳入 Git 管理
   - JSON 文件可以选择性忽略

3. **定期备份**
   - 保存 profile.md 的历史版本
   - 使用 Git 标签标记重要版本

4. **测试验证**
   - 每次修改后运行解析脚本
   - 检查生成的 JSON 是否符合预期

---

## 🎉 总结

通过自动化脚本，您可以：

- ✅ **一次编写，多处使用** - 只需维护 profile.md
- ✅ **实时更新** - 修改后立即生效
- ✅ **减少错误** - 避免手动复制粘贴
- ✅ **提高效率** - 专注于内容而非格式转换

**立即开始：**
```bash
python parse_profile.py
# 或
node parse_profile.mjs
```

享受自动化带来的便利吧！🚀
