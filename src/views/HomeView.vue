<template>
  <div class="home-page">
    <!-- Navbar -->
    <Navbar />

    <!-- Hero Section -->
    <HeroSection />

    <!-- About Section -->
    <AboutSection />

    <!-- Projects Section -->
    <ProjectsSection />

    <!-- Skills Section -->
    <SkillsSection />

    <!-- Contact Section -->
    <ContactSection />

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useProfileStore } from '@/stores/profile'
import Navbar from '@components/Navbar.vue'
import HeroSection from '@components/HeroSection.vue'
import AboutSection from '@components/AboutSection.vue'
import ProjectsSection from '@components/ProjectsSection.vue'
import SkillsSection from '@components/SkillsSection.vue'
import ContactSection from '@components/ContactSection.vue'
import Footer from '@components/Footer.vue'

const profileStore = useProfileStore()

onMounted(() => {
  profileStore.loadProfile()
})
</script>

<style scoped lang="scss">
.home-page {
  width: 100%;
  min-height: 100vh;
}
</style>
