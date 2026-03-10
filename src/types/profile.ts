/**
 * 个人信息数据类型定义
 */

export interface ProfileData {
  /** 基础信息 */
  basic: BasicInfo
  /**联系方式 */
  contact: ContactInfo
  /** 关于我 */
  about: AboutInfo
  /** 项目经历 */
  projects: ProjectInfo[]
  /** 技术栈 */
  skills: SkillCategory[]
}

export interface BasicInfo {
  name: string
  role: string
  greeting: string
  bio: string
  status: string
  avatar: string
}

export interface ContactInfo {
  email: string
  github: string
  blog: string
}

export interface AboutInfo {
  education: string
  highlights: string[]
  description: string
}

export interface ProjectInfo {
  id: number
  name: string
  type: string
  description: string
  difficulty?: string
  solution?: string
  techStack: string[]
  icon?: string
  color?: string
}

export interface SkillCategory {
  name: string
  icon: string
  items: SkillItem[]
}

export interface SkillItem {
  name: string
  level: number
  color?: string
}
