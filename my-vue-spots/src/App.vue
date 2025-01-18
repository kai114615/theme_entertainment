<template>
  <div class="app-container">
    <Banner />
    <SightSpot />
    <Footer />
  </div>
</template>

<script>
import SightSpot from './components/SightSpot.vue'
import Banner from './components/Banner.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    SightSpot,
    Banner,
    Footer
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: 'Microsoft JhengHei', Arial, sans-serif;
  background-color: #f5f6fa;
}

* {
  box-sizing: border-box;
}

.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>