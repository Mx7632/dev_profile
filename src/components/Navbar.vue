<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-container">
      <a href="#" class="nav-logo">
        <span class="prompt">&gt;</span>
        <span>{{ profileStore.getName || '李柄科' }}</span>
        <span class="cursor"></span>
      </a>

      <button class="mobile-toggle" @click="toggleMenu" aria-label="Toggle menu">
        <i :class="isMenuOpen ? 'fa-times' : 'fa-bars'"></i>
      </button>

      <ul class="nav-links" :class="{ open: isMenuOpen }">
        <li><a href="#home">首页</a></li>
        <li><a href="#about">关于我</a></li>
        <li><a href="#projects">项目经历</a></li>
        <li><a href="#skills">技术栈</a></li>
        <li><a href="#contact">联系方式</a></li>
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useProfileStore } from '@/stores/profile'

const profileStore = useProfileStore()
const isScrolled = ref(false)
const isMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped lang="scss">
@use '@/styles/variables' as *;

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: $nav-height;
  background: rgba($bg-primary, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid $border-color;
  z-index: 1000;
  transition: all 0.3s ease;

  &.scrolled {
   box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
  }
}

.nav-container {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 24px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  font-family: $font-mono;
  font-size: 1.2rem;
  font-weight: 700;
  color: $accent-blue;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;

  .prompt {
    color: $accent-green;
  }

  .cursor {
    display: inline-block;
    width: 2px;
    height: 1.2em;
    background: $accent-blue;
    animation: blink 1s step-end infinite;
   margin-left: 2px;
  }
}

@keyframes blink {
  50% {
   opacity: 0;
  }
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 8px;

  a {
   font-family: $font-mono;
   font-size: 0.85rem;
    color: $text-secondary;
    text-decoration: none;
   padding: 8px 16px;
   border-radius: 6px;
    transition: all 0.2s ease;
   position: relative;

    &:hover,
    &.active {
      color: $accent-blue;
      background: rgba($accent-blue, 0.1);
    }

    &::before {
      content: '//';
      color: $text-muted;
     margin-right: 4px;
     font-size: 0.75rem;
    }
  }
}

.mobile-toggle {
  display: none;
  background: none;
  border: none;
  color: $text-primary;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 8px;
}

@media (max-width: 768px) {
  .mobile-toggle {
    display: block;
  }

  .nav-links {
   position: fixed;
    top: $nav-height;
    left: 0;
    right: 0;
    background: $bg-secondary;
    flex-direction: column;
   padding: 24px;
    transform: translateY(-100%);
   opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;

    &.open {
      transform: translateY(0);
     opacity: 1;
      visibility: visible;
    }
  }
}
</style>
