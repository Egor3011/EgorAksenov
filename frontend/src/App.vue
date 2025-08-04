<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
import headerMain from './components/headerMain.vue';

import test_____ from './components/test_____.vue';

let choice = 'v1'

</script>

<template>
  <header>

    <div class="wrapper">
      <headerMain/>
    </div>
  </header>
  <div>
    <input name="radio" type="radio" v-model="choice" value="v1">
	  <input name="radio" type="radio" v-model="choice" value="v2">
	  <input name="radio" type="radio" v-model="choice" value="v3">
    <h3>you choosed: {{ choice }}</h3>
  </div>
  <RouterView />
  <Footer></Footer>
</template>
