<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import headerMain from './components/headerMain.vue';
import { gsap } from "gsap";
    
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

gsap.from(".headerTestGSAP", {
  y: 300,
})
</script>

<template>
  <header>

    <div class="wrapper">
      <headerMain class="headerTestGSAP"/>
    </div>
  </header>
  <RouterView />
  <Footer></Footer>
</template>
