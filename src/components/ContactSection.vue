<template>
  <section class="contact-section" id="contact">
    <div class="container">
      <h2 class="section-title">联系方式</h2>
      
      <div class="contact-content">
        <div class="contact-info">
          <p class="lead">如果您有任何问题或合作意向，欢迎通过以下方式联系我：</p>
          
          <div class="contact-cards">
            <a 
              :href="`mailto:${profileStore.getProfile?.contact.email}`"
              class="contact-card"
            >
              <div class="icon-wrapper">
                <i class="fas fa-envelope"></i>
              </div>
              <div class="info">
                <strong>邮箱</strong>
                <span>{{ profileStore.getProfile?.contact.email }}</span>
              </div>
            </a>
            
            <a 
              :href="profileStore.getProfile?.contact.github" 
              target="_blank"
              rel="noopener noreferrer"
              class="contact-card"
            >
              <div class="icon-wrapper">
                <i class="fab fa-github"></i>
              </div>
              <div class="info">
                <strong>GitHub</strong>
                <span>@{{ githubUsername }}</span>
              </div>
            </a>
            
            <a 
              :href="profileStore.getProfile?.contact.blog" 
              target="_blank"
              rel="noopener noreferrer"
              class="contact-card"
            >
              <div class="icon-wrapper">
                <i class="fas fa-globe"></i>
              </div>
              <div class="info">
                <strong>博客</strong>
                <span>访问我的博客</span>
              </div>
            </a>
            
            <div class="contact-card">
              <div class="icon-wrapper">
                <i class="fas fa-map-marker-alt"></i>
              </div>
              <div class="info">
                <strong>所在地</strong>
                <span>中国</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="contact-form-wrapper">
          <form class="contact-form" @submit.prevent="handleSubmit">
            <h3>发送消息</h3>
            
            <div class="form-group">
              <label for="name">姓名</label>
              <input 
                type="text" 
                id="name" 
                v-model="formData.name"
                placeholder="您的姓名"
                required
              />
            </div>
            
            <div class="form-group">
              <label for="email">邮箱</label>
              <input 
                type="email" 
                id="email" 
                v-model="formData.email"
                placeholder="您的邮箱"
                required
              />
            </div>
            
            <div class="form-group">
              <label for="message">消息</label>
              <textarea 
                id="message" 
                v-model="formData.message"
                placeholder="请输入消息内容..."
                rows="5"
                required
              ></textarea>
            </div>
            
            <button type="submit" class="btn-submit">
              <i class="fas fa-paper-plane"></i> 发送消息
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()

const formData = ref({
  name: '',
  email: '',
  message: ''
})

const githubUsername = computed(() => {
  const url = profileStore.getProfile?.contact.github || ''
 return url.split('/').filter(Boolean).pop() || 'github'
})

const handleSubmit = () => {
  // TODO: 实现表单提交逻辑
  alert('感谢您的留言！我会尽快回复您。')
  formData.value = { name: '', email: '', message: '' }
}
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.contact-section {
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

.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  
  @media(max-width: 768px) {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.contact-info {
  .lead {
    font-size: 1.1rem;
    line-height: 1.8;
    color: $text-secondary;
  margin-bottom: 32px;
  }
}

.contact-cards {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.contact-card {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px;
  background: $bg-secondary;
  border: 1px solid $border-color;
  border-radius:12px;
  transition: all 0.3s ease;
  text-decoration: none;
  
  &:hover {
    border-color: $accent-blue;
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba($accent-blue, 0.15);
  }
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

.info {
  display: flex;
  flex-direction: column;
  
  strong {
    font-size: 0.9rem;
    color: $text-muted;
  margin-bottom: 4px;
  }
  
  span {
    font-size: 1rem;
    color: $text-primary;
  }
}

.contact-form-wrapper {
  background: $bg-secondary;
  border: 1px solid $border-color;
  border-radius:16px;
  padding: 40px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.contact-form {
  h3 {
    font-size: 1.8rem;
  margin-bottom: 32px;
    color: $text-primary;
  }
}

.form-group {
  margin-bottom: 24px;
  
  label {
  display: block;
    font-size: 0.95rem;
    font-weight: 600;
    color: $text-primary;
  margin-bottom: 8px;
  }
  
  input,
  textarea {
    width: 100%;
   padding: 14px 18px;
   background: $bg-primary;
    border: 1px solid $border-color;
    border-radius: 8px;
    color: $text-primary;
    font-size: 1rem;
    font-family: inherit;
    transition: all 0.3s ease;
    
    &:focus {
      outline: none;
      border-color: $accent-blue;
      box-shadow: 0 0 0 3px rgba($accent-blue, 0.1);
    }
    
    &::placeholder {
     color: $text-muted;
    }
  }
  
  textarea {
   resize: vertical;
  min-height: 120px;
  }
}

.btn-submit {
  width: 100%;
  padding: 16px;
  background: linear-gradient(135deg, $accent-blue, $accent-purple);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  
  i {
    font-size: 1.1rem;
  }
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba($accent-blue, 0.4);
  }
}

@media(max-width: 768px) {
  .contact-content {
    grid-template-columns: 1fr;
  }
  
  .contact-form-wrapper {
   padding: 32px 24px;
  }
}
</style>
