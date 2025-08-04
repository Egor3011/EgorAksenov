<script>
import Review from './Review.vue';

export default {
  components: {
    Review
  },
  data() {
    return {
        elements: [{title: "Аксенов Егор", info: "CRM Pro полностью изменила наш подход к продажам. Автоматизация задач сэкономила нам десятки часов в месяц, а отчеты помогают принимать взвешенные решения.", img: "dsaddsadsad", link: "fdsdfsfsdf"},{title: "Ghb", info: "sadasdasd", img: "dsaddsadsad", link: "fdsdfsfsdf"},{title: "Ghb", info: "sadasdasd", img: "dsaddsadsad", link: "fdsdfsfsdf"},{title: "Ghb", info: "sadasdasd", img: "dsaddsadsad", link: "fdsdfsfsdf"},{title: "Ghb", info: "sadasdasd", img: "dsaddsadsad", link: "fdsdfsfsdf"}]
    }
  }
}
</script>


<style>
.reviewContainer {
  display: flex;
  flex-wrap: wrap; 
  justify-content: space-between;
}

@media(max-width: 1024px) {
  .reviewContainer {
    display: block;
    text-align: center;
    gap: 40px;
  }
}
</style>


<template>
    <div class="reviewContainer">
        <Review v-for="el in elements" style="text-align: left;" :title="el.title" :info="el.info" :logo-img="el.img" :link="el.link"/>
    </div>
</template>
