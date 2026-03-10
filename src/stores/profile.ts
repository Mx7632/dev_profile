/**
 * Profile 数据 Store
 * 管理个人信息相关的所有数据
 */

import { defineStore } from 'pinia'
import type { ProfileData } from '@/types/profile'

export const useProfileStore = defineStore('profile', {
  state: (): { profile: ProfileData | null } => ({
   profile: null,
  }),

  getters: {
    getProfile: (state) => state.profile,
    getName: (state) => state.profile?.basic.name || '',
    getRole: (state) => state.profile?.basic.role || '',
    getProjects: (state) => state.profile?.projects || [],
    getSkills: (state) => state.profile?.skills || [],
  },

  actions: {
    /**
     * 加载 Profile 数据
     * 从 profile.md 或其他数据源加载
     */
    loadProfile() {
      // TODO: 解析 profile.md 文件
      // 这里先使用硬编码数据，后续会通过 Python 脚本自动生成 JSON
      this.profile = {
        basic: {
          name: '李柄科',
          role: '后端开发工程师 / AI 开发爱好者',
          greeting: '// Hello World',
          bio: '南京航空航天大学计算机专业应届毕业生，热衷于用代码解决复杂问题。专注后端架构设计，擅长从 0 到 1 构建高性能、可扩展的系统。持续学习，探索未知世界。',
          status: '求职中 🚀',
          avatar: 'vibe_images/profile-photo_1773051777.png',
        },
        contact: {
          email: '1790405816@qq.com',
         github: 'https://github.com/Mx7632',
          blog: 'https://blog.limxbyte.sbs',
        },
        about: {
          education: '南京航空航天大学 | CS 本科',
          highlights: ['1 段后端实习经历', '字节工程训练营'],
          description:
            '我是一名即将毕业的计算机科学本科生。大学四年间，我不断探索技术的边界，从数据结构与算法、计算机底层基础，到 Java 核心与 JVM 底层原理，从数据库内核实现到分布式高并发系统设计，从单体业务开发到企业级 RAG 智能系统工程落地，积累了扎实的理论功底和全链路的项目实战经验。\n\n我相信优秀的代码不仅仅是"能跑"，更应该是**可维护的、可扩展的、优雅的**。在每一个项目中，我都追求代码质量与工程实践的最佳平衡。',
        },
       projects: [
          {
            id: 1,
            name: 'RAG 知识库',
            type: '实习项目',
            description:
              '参与构建基于 RAG 的企业级智能知识库，聚焦公司资源与项目知识的统一存储、高效检索及智能问答，解决教学资源管理痛点。',
            difficulty: '文件上传过程中的各种异常情况',
            solution: '采用 Redis bitmap 设计断点续传机制',
            techStack: [
              'Spring Boot',
              'Spring Security',
              'MinIO',
              'Elasticsearch',
              'Kafka',
              'JWT',
              'WebSocket',
            ],
            icon: 'fa-database',
            color: 'blue',
          },
          {
            id: 2,
            name: 'MiniDB - 简易数据库系统',
            type: '个人项目',
            description:
              '一个模拟 MySQL 的轻量级数据库系统，覆盖了数据库核心机制如数据管理、事务管理、并发控制、索引构建等，旨在深入理解数据库底层运行原理和关键模块的协作关系。',
            techStack: ['Java', 'MySQL', '数据库内核'],
            icon: 'fa-database',
            color: 'green',
          },
          {
            id: 3,
            name: 'SaaS 短链接系统',
            type: '个人项目',
            description:
              '全栈项目，集成人脸识别门禁、课表智能推荐、校园论坛等模块，日活跃用户 2000+。',
            difficulty: '人脸识别的实时性要求',
            solution:
              '引入模型量化与边缘推理，将识别延迟从 800ms 降至 120ms，同时采用 WebSocket 实现前后端实时通信。',
            techStack: ['Spring Boot', 'Spring Cloud', 'Redis', 'RocketMQ'],
            icon: 'fa-link',
            color: 'purple',
          },
          {
            id: 4,
            name: '基于工业异常检测的智能体（开发中）',
            type: '毕业设计',
            description: '通过 agent 的 CoT 和 RAG 系统，实现工业异常检测的快速更新和推理。',
            techStack: ['Python', 'LangChain', 'Vue3', 'RAG'],
            icon: 'fa-brain',
            color: 'orange',
          },
        ],
        skills: [
          {
            name: '编程语言',
            icon: 'fa-code',
            items: [
              { name: 'Java', level: 90, color: '#f89820' },
              { name: 'Python', level: 85, color: '#3776ab' },
              { name: 'Go', level: 50, color: '#00add8' },
            ],
          },
          {
            name: '数据库',
            icon: 'fa-database',
            items: [
              { name: 'MySQL', level: 88, color: '#00758f' },
              { name: 'Redis', level: 85, color: '#dc382d' },
            ],
          },
          {
            name: '框架与中间件',
            icon: 'fa-layer-group',
            items: [
              { name: 'Spring Boot / Cloud', level: 88, color: '#6db33f' },
              { name: 'FastAPI / Flask', level: 80, color: '#009688' },
            ],
          },
          {
            name: 'DevOps & 工具',
            icon: 'fa-tools',
            items: [
              { name: 'Git / GitHub Actions', level: 85, color: '#f05032' },
              { name: 'Docker/ K8s', level: 78, color: '#2496ed' },
            ],
          },
        ],
      }
    },
  },
})
