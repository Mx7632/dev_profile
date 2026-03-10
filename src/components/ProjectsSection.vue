<template>
  <section class="projects-section" id="projects">
    <div class="container">
      <h2 class="section-title">项目经历</h2>
      
      <div class="projects-grid">
        <article 
          v-for="(project, index) in profileStore.getProjects" 
          :key="index"
          class="project-card"
        >
          <div class="card-header">
            <div class="icon-wrapper">
              <i :class="`fas ${getIcon(project.icon)}`"></i>
            </div>
            <div class="tags">
              <span 
                v-for="(tech, techIndex) in project.techStack.slice(0, 3)" 
                :key="techIndex"
                class="tech-tag"
              >
                {{ tech }}
              </span>
            </div>
          </div>
          
          <div class="card-body">
            <h3>{{ project.name }}</h3>
            <p class="description">{{ project.description }}</p>
            
            <ul class="highlights">
              <li v-for="(highlight, hIndex) in getHighlights(project)" :key="hIndex">
                {{ highlight }}
              </li>
            </ul>
          </div>
          
          <div class="card-footer">
            <a 
              v-if="(project as any).github"
              :href="(project as any).github" 
              target="_blank" 
              rel="noopener noreferrer"
              class="btn-link"
            >
              <i class="fab fa-github"></i> 查看源码
            </a>
            <a 
              v-if="(project as any).demo"
              :href="(project as any).demo" 
              target="_blank" 
              rel="noopener noreferrer"
              class="btn-link primary"
            >
              <i class="fas fa-external-link-alt"></i> 在线演示
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useProfileStore } from '@/stores/profile'
import type { ProjectInfo } from '@/types/profile'

const profileStore = useProfileStore()

const getIcon = (icon?: string): string => {
  if (!icon) return 'fa-code'
 return icon.startsWith('fa-') ? icon: `fa-${icon}`
}

const getHighlights = (project: ProjectInfo): string[] => {
  // 如果有 highlights 字段，使用它
  if ('highlights' in project && Array.isArray((project as any).highlights)) {
   return (project as any).highlights
  }
  // 否则返回描述的一部分
 return [project.description]
}
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.projects-section {
  padding: 80px 24px;
  background: $bg-primary;
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

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 32px;
  
  @media(max-width: 768px) {
    grid-template-columns: 1fr;
  }
}

.project-card {
  background: $bg-secondary;
  border: 1px solid $border-color;
  border-radius:16px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 48px rgba($accent-blue, 0.15);
    border-color: $accent-blue;
  }
}

.card-header {
  padding: 24px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}

.icon-wrapper {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, $accent-blue, $accent-purple);
  border-radius:12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tech-tag {
  background: rgba($accent-blue, 0.1);
  color: $accent-blue;
  padding: 6px 12px;
  border-radius:20px;
  font-size: 0.85rem;
  font-weight: 500;
}

.card-body {
  padding: 0 24px 24px;
  flex: 1;
  
  h3 {
    font-size: 1.5rem;
   margin-bottom: 12px;
    color: $text-primary;
  }
  
  .description {
    font-size: 1rem;
    line-height: 1.6;
    color: $text-secondary;
  margin-bottom: 16px;
  }
  
  .highlights {
    list-style: none;
  padding: 0;
  margin: 0;
    
    li {
    position: relative;
     padding-left: 20px;
    margin-bottom: 8px;
     font-size: 0.95rem;
     color: $text-secondary;
     line-height: 1.6;
      
      &::before {
       content: '▹';
      position: absolute;
       left: 0;
       color: $accent-blue;
      }
    }
  }
}

.card-footer {
  padding: 16px 24px 24px;
  display: flex;
  gap: 16px;
  border-top: 1px solid $border-color;
}

.btn-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  border: 1px solid $border-color;
  color: $text-secondary;
  background: transparent;
  
  &:hover {
    border-color: $accent-blue;
    color: $accent-blue;
    transform: translateY(-2px);
  }
  
  &.primary {
   background: linear-gradient(135deg, $accent-blue, $accent-purple);
    color: white;
    border: none;
    
    &:hover {
      box-shadow: 0 8px 24px rgba($accent-blue, 0.3);
    }
  }
}

@media(max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-card {
  max-width: 100%;
  }
}
</style>