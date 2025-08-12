<script setup>
import ConnectWithMe from '@/components/ConnectWithMe.vue';
import ReviewContainer from '@/components/ReviewContainer.vue';
import faqContainer from '@/components/faqContainer.vue';
import containersSale from '@/components/containersSale.vue';
import mainBlock from '@/components/mainBlock.vue';

import { onMounted, Transition } from 'vue';

import gsap from 'gsap';
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

onMounted(() => {
  gsap.from(".mainBlock", {
    opacity: 0,
    x: 50,
    duration: 0.5
  })
}) 
</script>

<template>
  <main class="mainBlock">
    <mainBlock/>
    

    <div class="line">
    </div>

    <div>
      <h1 class="headingBlock" id="orderdevelopment">Заказать</h1>
      <containersSale/>
    </div>

    <div class="line"></div>

    <div>
      <h1 class="headingBlock" id="connectWithMe">Связь со мной</h1>
      <ConnectWithMe/>
    </div>

    <div class="line"></div>

    <div>
      <h1 class="headingBlock" id="reviews">Отзывы</h1>
      <ReviewContainer/>
    </div>

    <div class="line"></div>

    <div>
      <h1 class="headingBlock" id="faq">Частые вопросы</h1>
      <faqContainer style="margin-bottom: 120px;"/>
    </div>
  </main>
</template>

<style>
.headingBlock {
  text-decoration: underline;
  margin-bottom: 80px;
}
.line {
  height: 3px;
  width: 100%;
  background: #ffffff;
  border-radius: 2px;
  margin: 120px 0px 120px 0px;
}
</style>
