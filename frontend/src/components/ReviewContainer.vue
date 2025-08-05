<script>
import Review from './Review.vue';
import axios from 'axios';

export default {
  components: {
    Review
  },  
  mounted() { 
    axios.get("https://c1bd7fa3efd9e6d1.mokky.dev/reviews").then((datas) => {
        console.log(datas)
        this.elements = datas.data
      }).catch(error => {console.log(error)})
  },
  data() {
    return {
        elements: [],
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
