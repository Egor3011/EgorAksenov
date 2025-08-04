<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import headerMain from './components/headerMain.vue';

</script>

<template>
  <header>

    <div class="wrapper">
      <headerMain/>
    </div>
  </header>
  <RouterView />
  <Footer></Footer>
</template>
