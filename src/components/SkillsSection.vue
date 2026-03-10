<template>
  <section class="skills-section" id="skills">
    <div class="container">
      <h2 class="section-title">技术栈</h2>
      
      <div class="skills-grid">
        <div 
          v-for="(category, index) in skillCategories" 
          :key="index"
          class="skill-card"
        >
          <div class="card-header">
            <i :class="`fas ${category.icon}`"></i>
            <h3>{{ category.name }}</h3>
          </div>
          
          <div class="skills-list">
            <div 
              v-for="(skill, sIndex) in category.skills" 
              :key="sIndex"
              class="skill-tag"
              :style="{ borderColor: skill.color || '' }"
            >
              {{ skill.name }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 示例技能数据（后续可从 profile store 加载）
const skillCategories = ref([
  {
    name: '编程语言',
    icon: 'fa-code',
    skills: [
      { name: 'Java', color: '#667eea' },
      { name: 'Python', color: '#764ba2' },
      { name: 'Go', color: '#00f2fe' },
      { name: 'TypeScript', color: '#4facfe' }
    ]
  },
  {
    name: '后端框架',
    icon: 'fa-server',
    skills: [
      { name: 'Spring Boot', color: '#f093fb' },
      { name: 'Django', color: '#f5576c' },
      { name: 'Gin', color: '#43e97b' },
      { name: 'FastAPI', color: '#38f9d7' }
    ]
  },
  {
    name: '数据库',
    icon: 'fa-database',
    skills: [
      { name: 'MySQL', color: '#fa709a' },
      { name: 'PostgreSQL', color: '#fee140' },
      { name: 'Redis', color: '#30cfd0' },
      { name: 'MongoDB', color: '#330867' }
    ]
  },
  {
    name: '云原生 & DevOps',
    icon: 'fa-cloud',
    skills: [
      { name: 'Docker', color: '#667eea' },
      { name: 'Kubernetes', color: '#764ba2' },
      { name: 'AWS', color: '#f093fb' },
      { name: 'CI/CD', color: '#f5576c' }
    ]
  },
  {
    name: '前端技术',
    icon: 'fa-laptop-code',
    skills: [
      { name: 'Vue.js', color: '#4facfe' },
      { name: 'React', color: '#00f2fe' },
      { name: 'Next.js', color: '#43e97b' },
      { name: 'TailwindCSS', color: '#38f9d7' }
    ]
  },
  {
    name: 'AI & 其他',
    icon: 'fa-brain',
    skills: [
      { name: 'PyTorch', color: '#fa709a' },
      { name: 'LangChain', color: '#fee140' },
      { name: 'RAG', color: '#30cfd0' },
      { name: 'Fine-tuning', color: '#330867' }
    ]
  }
])
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.skills-section {
  padding: 80px 24px;
  background: $bg-secondary;
}

.container {
  max-width: $max-width;
  margin: 0 auto;
}

.section-title {
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 60px;
  position: relative;
  
  &::after {
    content: '';
  position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 4px;
  background: linear-gradient(90deg, $accent-blue, $accent-purple);
    border-radius: 2px;
  }
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 32px;
  
  @media(max-width: 768px) {
    grid-template-columns: 1fr;
  }
}

.skill-card {
  background: $bg-primary;
  border: 1px solid $border-color;
  border-radius:16px;
  padding: 32px;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 48px rgba($accent-blue, 0.15);
    border-color: $accent-blue;
  }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  
  i {
    font-size: 2rem;
   background: linear-gradient(135deg, $accent-blue, $accent-purple);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
   background-clip: text;
  }
  
  h3 {
    font-size: 1.5rem;
    color: $text-primary;
  }
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.skill-tag {
  background: rgba($accent-blue, 0.08);
  color: $text-secondary;
  padding: 10px 20px;
  border-radius:20px;
  font-size: 0.95rem;
  font-weight: 500;
  border: 2px solid transparent;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba($accent-blue, 0.2);
  }
}

@media(max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .skills-grid {
    gap: 24px;
  }
}
</style>
