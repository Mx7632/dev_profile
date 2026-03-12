/**
 * Profile 数据 Store
 * 管理个人信息相关的所有数据
 */

import { defineStore } from 'pinia'
import type { ProfileData } from '@/types/profile'
import profileData from '@/data/profile.json'

export const useProfileStore = defineStore('profile', {
  state: (): { profile: ProfileData | null } => ({
    profile: profileData as ProfileData,
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
     * 目前直接使用导入的 profile.json，后续可扩展为从 API 加载
     */
    loadProfile() {
      if (profileData) {
        this.profile = profileData as ProfileData
      }
    },
  },
})
