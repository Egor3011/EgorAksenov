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

<template>
    <div style="display: flex;flex-wrap: wrap; justify-content: space-between;">
        <Review v-for="el in elements" :title="el.title" :info="el.info" :logo-img="el.img" :link="el.link"/>
    </div>
</template>