<template>
  <section class="hero-section" id="home">
   <!-- 代码雨背景 -->
   <div class="code-rain" ref="codeRainRef"></div>
   
   <div class="hero-content">
     <div class="hero-text">
       <h1>
         <span class="greeting">{{ profileStore.getProfile?.basic.greeting || '// Hello World' }}</span>
         <br />
         我是 <span class="name">{{ profileStore.getName || '李柄科' }}</span>
       </h1>
       
       <div class="role">
         <span class="typing-text">{{ typedRole }}</span>
       </div>
       
       <p class="bio">
         {{ profileStore.getProfile?.basic.bio || '' }}
       </p>
       
       <div class="hero-buttons">
         <a href="#projects" class="btn btn-primary">
           <i class="fas fa-code"></i> 查看项目
         </a>
         <a href="#contact" class="btn btn-outline">
           <i class="fas fa-paper-plane"></i> 联系我
         </a>
         <a :href="profileStore.getProfile?.contact.github" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
           <i class="fab fa-github"></i> GitHub
         </a>
       </div>
     </div>
     
     <div class="hero-visual">
       <div class="terminal-window">
         <div class="terminal-header">
           <div class="terminal-dots">
             <span></span><span></span><span></span>
           </div>
           <span class="terminal-title">developer.json</span>
         </div>
         <div class="terminal-body">
           <div class="line"><span class="comment">// About me in JSON</span></div>
           <div class="line">{</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"name"</span>: <span class="string">"{{ profileStore.getName }}"</span>,</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"role"</span>: <span class="string">"{{ profileStore.getRole }}"</span>,</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"education"</span>: <span class="string">"CS 本科"</span>,</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"languages"</span>: [</div>
           <div class="line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="string">"Java"</span>, <span class="string">"Python"</span>,</div>
           <div class="line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="string">"Go"</span></div>
           <div class="line">&nbsp;&nbsp;],</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"passion"</span>: <span class="string">"构建优雅的系统"</span>,</div>
           <div class="line">&nbsp;&nbsp;<span class="key">"status"</span>: <span class="string">"{{ profileStore.getProfile?.basic.status }}"</span></div>
           <div class="line">}</div>
         </div>
       </div>
     </div>
   </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()
const codeRainRef = ref<HTMLElement | null>(null)
const typedRole = ref('')

// 打字效果
const roles = [
  '后端开发工程师',
  'AI 开发爱好者',
  '问题解决者',
  '开源贡献者'
]
let roleIndex = 0
let charIndex = 0
let isDeleting = false
let typingTimer: ReturnType<typeof setTimeout>

const typeRole = () => {
  const currentRole = roles[roleIndex]
  
  if (isDeleting) {
    typedRole.value = currentRole.substring(0, charIndex - 1)
    charIndex--
  } else {
    typedRole.value = currentRole.substring(0, charIndex + 1)
    charIndex++
  }
  
  let speed = isDeleting ? 50 : 100
  
  if (!isDeleting && charIndex === currentRole.length) {
    speed = 2000
    isDeleting = true
  } else if (isDeleting && charIndex === 0) {
    isDeleting= false
    roleIndex = (roleIndex +1) % roles.length
    speed = 500
  }
  
  typingTimer = setTimeout(typeRole, speed)
}

// 代码雨效果
const createCodeRain = () => {
  if (!codeRainRef.value) return
  
  const codeSnippets = [
    'public static void main()',
    'func main() {',
    'import React from "react"',
    'SELECT * FROM users',
    'docker-compose up -d',
    'git push origin main',
    'npm install',
    'class Solution {',
    'async def handler():',
    'kubectl apply -f',
    'const app = express()',
    'return HttpResponse(200)',
    '@Autowired',
    'impl Iterator for',
    'go func() {',
  ]
  
  const span = document.createElement('span')
  span.textContent = codeSnippets[Math.floor(Math.random() * codeSnippets.length)]
  span.style.left = Math.random() * 100 + '%'
  span.style.animationDuration = `${Math.random() * 10 + 10}s`
  span.style.fontSize = `${Math.random() * 6 +10}px`
  span.style.opacity = `${Math.random() * 0.5 + 0.1}`
  codeRainRef.value.appendChild(span)
  
  setTimeout(() => span.remove(), 20000)
}

onMounted(() => {
  typeRole()
  const rainInterval = setInterval(createCodeRain, 800)
  
  onUnmounted(() => {
    clearTimeout(typingTimer)
    clearInterval(rainInterval)
  })
})
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: calc(#{$nav-height} + 40px) 24px 40px;
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
   position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
   background:
      radial-gradient(ellipse 800px 600px at 20% 30%, rgba($accent-blue, 0.06) 0%, transparent 70%),
      radial-gradient(ellipse 600px 400px at 80% 70%, rgba($accent-purple, 0.04) 0%, transparent 70%);
   pointer-events: none;
  }
}

.code-rain {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
  
  span {
   position: absolute;
    top: -50px;
    color: $accent-green;
    font-family: $font-mono;
    white-space: nowrap;
    animation: fall linear infinite;
  }
}

@keyframes fall {
  to {
    transform: translateY(100vh);
  }
}

.hero-content {
  max-width: $max-width;
  width: 100%;
  display: grid;
  grid-template-columns:1fr 1fr;
  gap: 60px;
  align-items: center;
  position: relative;
  z-index: 1;
  
  @media(max-width: 968px) {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.hero-text {
  h1 {
    font-size: 3rem;
   margin-bottom: 16px;
    line-height: 1.2;
    
    .greeting {
     display: block;
      font-size: 1.5rem;
      color: $accent-green;
      font-family: $font-mono;
     margin-bottom: 8px;
    }
    
    .name {
     background: linear-gradient(135deg, $accent-blue, $accent-purple);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
     background-clip: text;
    }
  }
  
  .role {
    font-size: 1.5rem;
    color: $text-secondary;
   margin-bottom: 24px;
   min-height: 2em;
    
    .typing-text {
      border-right: 2px solid $accent-blue;
      animation: blink 0.7s infinite;
    }
  }
  
  .bio {
    font-size: 1.1rem;
    line-height: 1.8;
    color: $text-secondary;
   margin-bottom: 32px;
  }
}

.hero-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  
  .btn {
   padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
   text-decoration: none;
    transition: all 0.3s ease;
   display: inline-flex;
   align-items: center;
    gap: 8px;
    
    i {
      font-size: 1.1rem;
    }
    
    &.btn-primary {
     background: linear-gradient(135deg, $accent-blue, $accent-purple);
      color: white;
      border: none;
      
      &:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba($accent-blue, 0.4);
      }
    }
    
    &.btn-outline {
     background: transparent;
      color: $text-secondary;
      border: 1px solid $border-color;
      
      &:hover {
        border-color: $accent-blue;
        color: $accent-blue;
        transform: translateY(-2px);
      }
    }
  }
}

@keyframes blink {
  50% { opacity: 0; }
}

.terminal-window {
  background: $bg-secondary;
  border: 1px solid $border-color;
  border-radius:12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.terminal-header {
  background: $bg-tertiary;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid $border-color;
  
  .terminal-dots {
   display: flex;
    gap: 8px;
    
    span {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      
      &:nth-child(1) { background: #ff5f56; }
      &:nth-child(2) { background: #ffbd2e; }
      &:nth-child(3) { background: #27c93f; }
    }
  }
  
  .terminal-title {
    font-family: $font-mono;
    font-size: 0.85rem;
    color: $text-muted;
  }
}

.terminal-body {
  padding: 20px;
  font-family: $font-mono;
  font-size: 0.9rem;
  line-height: 1.8;
  
  .line {
    white-space: pre-wrap;
    
    .comment { color: $text-muted; }
    .key { color: $accent-purple; }
    .string { color: $accent-green; }
  }
}

@media(max-width: 768px) {
  .hero-content {
    grid-template-columns: 1fr;
  }
  
  .hero-text h1 {
    font-size: 2rem;
  }
  
  .terminal-window {
   display: none;
  }
}
</style>
