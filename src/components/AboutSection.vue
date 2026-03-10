<template>
  <section class="about-section" id="about">
    <div class="container">
      <h2 class="section-title">关于我</h2>
      
      <div class="about-content">
        <div class="about-text">
          <p class="lead">{{ profileStore.getProfile?.basic.bio }}</p>
          
          <div class="info-grid">
            <div class="info-item">
              <i class="fas fa-user"></i>
              <div>
                <strong>姓名</strong>
                <span>{{ profileStore.getName }}</span>
              </div>
            </div>
            
            <div class="info-item">
              <i class="fas fa-briefcase"></i>
              <div>
                <strong>职位</strong>
                <span>{{ profileStore.getRole }}</span>
              </div>
            </div>
            
            <div class="info-item">
              <i class="fas fa-graduation-cap"></i>
              <div>
                <strong>学历</strong>
                <span>计算机科学与技术 本科</span>
              </div>
            </div>
            
            <div class="info-item">
              <i class="fas fa-map-marker-alt"></i>
              <div>
                <strong>所在地</strong>
                <span>中国</span>
              </div>
            </div>
          </div>
          
          <div class="description">
            <h3>个人简介</h3>
            <p>
              作为一名热爱技术的后端开发工程师，我专注于构建高性能、可扩展的分布式系统。
              对 AI 技术充满热情，喜欢探索新技术并将其应用于实际项目中。
            </p>
            <p>
              在工作中，我注重代码质量和系统架构设计，追求简洁优雅的解决方案。
              业余时间会参与开源项目，持续学习新技术，保持对技术的热情和好奇心。
            </p>
          </div>
        </div>
        
        <div class="about-image">
          <div class="image-wrapper">
            <img 
              :src="profileStore.getProfile?.basic.avatar || '/avatar.jpg'" 
             alt="李柄科"
              class="profile-image"
            />
            <div class="experience-badge">
              <span class="number">3+</span>
              <span class="text">年经验</span>
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

.about-section {
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

.about-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
  
  @media(max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.about-text {
  .lead {
    font-size: 1.2rem;
    line-height: 1.8;
    color: $text-primary;
   margin-bottom: 32px;
  }
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}

.info-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 20px;
  background: $bg-primary;
  border-radius:12px;
  border: 1px solid $border-color;
  transition: all 0.3s ease;
  
  &:hover {
    border-color: $accent-blue;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba($accent-blue, 0.1);
  }
  
  i {
    font-size: 1.5rem;
    color: $accent-blue;
   margin-top: 4px;
  }
  
  strong {
   display: block;
    font-size: 0.9rem;
    color: $text-muted;
   margin-bottom: 4px;
  }
  
  span {
   display: block;
    font-size: 1rem;
    color: $text-primary;
  }
}

.description {
  h3 {
    font-size: 1.5rem;
   margin-bottom: 16px;
    color: $text-primary;
  }
  
  p {
    font-size: 1rem;
    line-height: 1.8;
    color: $text-secondary;
   margin-bottom: 16px;
  }
}

.about-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-wrapper {
  position: relative;
  width: 100%;
  max-width: 400px;
  aspect-ratio: 1;
  border-radius:20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.experience-badge {
  position: absolute;
  bottom: 24px;
  right: 24px;
  background: linear-gradient(135deg, $accent-blue, $accent-purple);
  color: white;
  padding: 16px 24px;
  border-radius:12px;
  text-align: center;
  box-shadow: 0 8px 24px rgba($accent-blue, 0.4);
  
  .number {
   display: block;
    font-size: 2rem;
    font-weight: bold;
  }
  
  .text {
    font-size: 0.9rem;
    opacity: 0.9;
  }
}

@media(max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .about-content {
    gap: 40px;
  }
  
  .image-wrapper {
   max-width: 300px;
  }
}
</style>
