<template>
  <section class="skills-section" id="skills">
    <div class="container">
      <h2 class="section-title">技术栈</h2>
      
      <div class="skills-grid">
        <div 
          v-for="(category, index) in profileStore.getSkills" 
          :key="index"
          class="skill-card"
        >
          <div class="card-header">
            <i :class="`fas ${category.icon}`"></i>
            <h3>{{ category.name }}</h3>
          </div>
          
          <div class="skills-list">
            <div 
              v-for="(skill, sIndex) in category.items" 
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
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()
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
    bottom: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 4px;
    background: linear-gradient(135deg, $accent-blue 0%, $accent-purple 100%);
    border-radius: 2px;
  }
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 32px;
}

.skill-card {
  background: $bg-primary;
  border: 1px solid $border-color;
  border-radius: 16px;
  padding: 32px;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
    border-color: $accent-blue;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  
  i {
    font-size: 1.5rem;
    color: $accent-blue;
  }
  
  h3 {
    font-size: 1.25rem;
    color: $text-primary;
  }
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.skill-tag {
  padding: 8px 16px;
  background: $bg-secondary;
  border: 1px solid $border-color;
  border-radius: 8px;
  font-family: $font-mono;
  font-size: 0.9rem;
  color: $text-secondary;
  transition: all 0.2s ease;
  
  &:hover {
    color: $text-primary;
    background: $bg-tertiary;
    transform: scale(1.05);
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .skills-grid {
    grid-template-columns: 1fr;
  }
}
</style>
