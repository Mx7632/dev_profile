# 个人信息配置 (Profile Configuration)

在此文件中填写你的个人信息，这些信息将用于生成你的个人主页。

## 1. 基础信息 (Basic Info)

- **姓名 (Name):** 李柄科
- **职位 (Role):** 后端开发工程师 / AI 开发爱好者
- **标语 (Greeting):** // Hello World
- **简介 (Bio):** 南京航空航天大学计算机专业应届毕业生，热衷于用代码解决复杂问题。专注后端架构设计，擅长从0到1构建高性能、可扩展的系统。持续学习，探索未知世界。
- **状态 (Status):** 求职中 🚀
- **头像路径 (Profile Photo):** vibe_images/profile-photo_1773051777.png

## 2. 联系方式 (Contact)

- **Email:** limx7632@gmail.com
- **GitHub:** https://github.com/Mx7632
- **Blog:** https://blog.limxbyte.sbs

## 3. 关于我 (About Me)

- **学历 (Education):** 南京航空航天大学 | CS本科
- **亮点 (Highlights):**
    - 1段后端实习经历
    - 字节工程训练营
- **详细描述 (Description):**
    我是一名即将毕业的计算机科学本科生。大学四年间，我不断探索技术的边界，从数据结构与算法、计算机底层基础，到 Java 核心与 JVM 底层原理，从数据库内核实现到分布式高并发系统设计，从单体业务开发到企业级 RAG 智能系统工程落地，积累了扎实的理论功底和全链路的项目实战经验。

    我相信优秀的代码不仅仅是"能跑"，更应该是**可维护的、可扩展的、优雅的**。在每一个项目中，我都追求代码质量与工程实践的最佳平衡。

## 4. 项目经历 (Projects)

### Project 1: RAG知识库 
- **类型:** 实习项目
- **描述:** 参与构建基于 RAG 的企业级智能知识库，聚焦公司资源与项目知识的统一存储、高效检索及智能问答，解决教学资源管理痛点。
- **难点与方案:** 文件上传过程中的各种异常情况  - 采用 Redis bitmap 设计断点续传机制。
- **技术栈:** Spring Boot、Spring Security、MinIO、Elasticsearch、Kafka、JWT、WebSocket

### Project 2: MiniDB - 简易数据库系统
- **类型:** 个人项目
- **描述:** 一个模拟 MySQL 的轻量级数据库系统，覆盖了数据库核心机制如数据管理、事务管理、并发控制、索引构建等，旨在深入理解数据库底层运行原理和关键模块的协作关系。

### Project 3: SaaS短链接系统
- **类型:** 个人项目
- **描述:** 全栈项目，前端使用 **React** + **TypeScript**，后端基于 **Python FastAPI**。集成人脸识别门禁、课表智能推荐、校园论坛等模块，日活跃用户 **2000+**。
- **难点与方案:** 人脸识别的实时性要求 - 引入模型量化与边缘推理，将识别延迟从 800ms 降至 120ms，同时采用 WebSocket 实现前后端实时通信。
- **技术栈:** Spring Boot、Spring Cloud、Redis、RocketMQ

### Project 4: 基于工业异常检测的智能体（开发中）
- **类型:** 毕业设计
- **描述:** 通过agent的CoT和RAG系统，实现工业异常检测的快速更新和推理
- **技术栈:** python、langchain、vue3

## 5. 技术栈 (Skills)

### 编程语言
- **Java:** 90%
- **Python:** 85%
- **Go:** 50%

### 数据库
- **MySQL:** 88%
- **Redis:** 85%
- **PostgreSQL:** 70%
- **MongoDB:** 65%

### 框架与中间件
- **Spring Boot / Cloud:** 88%
- **FastAPI / Flask:** 80%
- **Gin / Fiber (Go):** 75%

### DevOps & 工具
- **Git / GitHub Actions:** 85%
- **Docker / K8s:** 78%
- **Linux / Shell:** 62%
- **Nginx / Apache:** 70%

### 其他标签
- 微服务架构, RESTful API, 消息队列, RabbitMQ, Kafka, 数据结构与算法, 设计模式, ElasticSearch, gRPC, GraphQL, Prometheus, WebSocket, OAuth2.0, JWT, Swagger, MyBatis, HTML/CSS
