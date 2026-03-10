<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <!-- 左侧信息 -->
        <div class="footer-left">
          <div class="logo">
            <span class="initial">L</span>
          </div>
          <p class="name">{{ profileStore.getName }}</p>
          <p class="role">{{ profileStore.getRole }}</p>
        </div>
        
        <!-- 中间导航 -->
        <div class="footer-nav">
          <h4>快速链接</h4>
          <ul>
            <li><a href="#home">首页</a></li>
            <li><a href="#about">关于我</a></li>
            <li><a href="#projects">项目经历</a></li>
            <li><a href="#skills">技术栈</a></li>
            <li><a href="#contact">联系方式</a></li>
          </ul>
        </div>
        
        <!-- 右侧社交链接 -->
        <div class="footer-social">
          <h4>关注我</h4>
          <div class="social-links">
            <a 
              :href="profileStore.getProfile?.contact.github" 
              target="_blank"
              rel="noopener noreferrer"
              class="social-link"
              title="GitHub"
            >
              <i class="fab fa-github"></i>
            </a>
            <a 
              href="#"
              class="social-link"
              title="LinkedIn"
            >
              <i class="fab fa-linkedin-in"></i>
            </a>
            <a 
              :href="`mailto:${profileStore.getProfile?.contact.email}`"
              class="social-link"
              title="Email"
            >
              <i class="fas fa-envelope"></i>
            </a>
            <a 
              :href="profileStore.getProfile?.contact.blog"
              target="_blank"
              rel="noopener noreferrer"
              class="social-link"
              title="Blog"
            >
              <i class="fas fa-rss"></i>
            </a>
          </div>
        </div>
      </div>
      
      <!-- 底部版权信息 -->
      <div class="footer-bottom">
        <div class="copyright">
          <p>&copy; {{ currentYear }} {{ profileStore.getName }}. All rights reserved.</p>
          <p>Built with ❤️ using Vue3 + TypeScript + Vite</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()
const currentYear = new Date().getFullYear()
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.footer {
  background: $bg-tertiary;
  border-top: 1px solid $border-color;
  padding: 60px 24px 30px;
}

.container {
  max-width: $max-width;
  margin: 0 auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
  
  @media(max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}

.footer-left {
  text-align: center;
  
  .logo {
  margin-bottom: 16px;
    
   .initial {
    display: inline-block;
     width: 60px;
     height: 60px;
    background: linear-gradient(135deg, $accent-blue, $accent-purple);
     color: white;
     font-size: 2rem;
     font-weight: bold;
     line-height: 60px;
    text-align: center;
     border-radius: 50%;
     box-shadow: 0 8px 24px rgba($accent-blue, 0.3);
    }
  }
  
  .name {
    font-size: 1.3rem;
    font-weight: 600;
    color: $text-primary;
  margin-bottom: 8px;
  }
  
  .role {
    font-size: 1rem;
    color: $text-secondary;
  }
}

.footer-nav {
  h4 {
    font-size: 1.1rem;
    font-weight: 600;
    color: $text-primary;
  margin-bottom: 20px;
  }
  
  ul {
    list-style: none;
  padding: 0;
  margin: 0;
    
    li {
   margin-bottom: 12px;
      
     a {
       color: $text-secondary;
     text-decoration: none;
      transition: all 0.3s ease;
      font-size: 0.95rem;
      
        &:hover {
         color: $accent-blue;
         transform: translateX(4px);
        }
      }
    }
  }
}

.footer-social {
  h4 {
    font-size: 1.1rem;
    font-weight: 600;
    color: $text-primary;
  margin-bottom: 20px;
  text-align: center;
  }
}

.social-links {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.social-link {
  width: 48px;
  height: 48px;
  background: $bg-primary;
  border: 1px solid $border-color;
  border-radius:50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: $text-secondary;
  font-size: 1.3rem;
  text-decoration: none;
  transition: all 0.3s ease;
  
  &:hover {
   background: linear-gradient(135deg, $accent-blue, $accent-purple);
    color: white;
    border-color: transparent;
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba($accent-blue, 0.3);
  }
}

.footer-bottom {
  border-top: 1px solid $border-color;
  padding-top: 30px;
}

.copyright {
  text-align: center;
  
  p {
    font-size: 0.95rem;
    color: $text-muted;
  margin-bottom: 8px;
    
    &:last-child {
   margin-bottom: 0;
    }
  }
}

@media(max-width: 768px) {
  .footer {
  padding: 48px 24px 24px;
  }
  
  .footer-content {
    gap: 32px;
  }
}
</style>
