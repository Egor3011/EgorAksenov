<template>
  <div class="priceList">
    <h1 class="headingBlock">Прайс лист</h1>
    <div id="turnkeywebsite">
      <h1 class="titlePriceComp">Сайт под ключ</h1>
      <priceCompContainer link-backend="https://c1bd7fa3efd9e6d1.mokky.dev/turnkeywebsite"/>
    </div>
    <div id="designwebsite">
      <h1 class="titlePriceComp">Дизайн сайта</h1>
      <priceCompContainer link-backend="https://c1bd7fa3efd9e6d1.mokky.dev/designwebsite"/>
    </div>
    <div id="chatbot">
      <h1 class="titlePriceComp">Чат-боты</h1>
      <priceCompContainer link-backend="https://c1bd7fa3efd9e6d1.mokky.dev/chatbot"/>
    </div>
    <div id="ddwebsait">
      <h1 class="titlePriceComp">Сайт по готовому макету</h1>
      <priceCompContainer link-backend="http://176.109.111.74:8000/pricesInfo/fullSait"/>
    </div>
  </div>
</template>
<style>
.headingBlock {
  text-decoration: underline;
  margin-bottom: 80px;
}

.headingBlockSecond {
  font-size: 16px;
}

.titlePriceComp {
  position: sticky;
  transform: translate(calc(-2rem + 10px), 0px);
  top: 35px;
}
</style>

<script setup>
import priceComp from '@/components/priceComp.vue';
import priceCompContainer from '@/components/priceCompContainer.vue';

const fullSait = [{"title":"Визитная карточка","info":"Разработка сайта под ключ позволяет вам не искать различных програмистов, дизайнеров, и т.д. Всю работу выполню я","price":"от 6.000 р","date":"от 3 дней","linkExample":"-","imgLogo":"-"},{"title":"Визитная карточка","info":"Разработка сайта под ключ позволяет вам не искать различных програмистов, дизайнеров, и т.д. Всю работу выполню я","price":"от 6.000 р","date":"от 3 дней","linkExample":"-","imgLogo":"-"},{"title":"Визитная карточка","info":"Разработка сайта под ключ позволяет вам не искать различных програмистов, дизайнеров, и т.д. Всю работу выполню я","price":"от 6.000 р","date":"от 222 дней","linkExample":"-","imgLogo":"-"}]
</script>
