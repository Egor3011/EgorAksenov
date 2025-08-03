<template>
    <div>
        <priceComp v-for="el in this.listItems" :title="el.title" :info="el.info" :price="el.price" :linkExample="el.linkExample" :imgLogo="el.imgLogo" :date="el.date"/>
    </div>
</template>

<script>
import { onMounted } from 'vue';
import priceComp from './priceComp.vue';
import axios from 'axios';

export default {
  props: {
    linkBackend: String
  },  
  mounted() { 
    axios.get(this.linkBackend).then((datas) => {
        console.log(datas)
        this.listItems = datas.data
      }).catch(error => {console.log(error)})
      const res = fetch(this.linkBackend)
  },
  data() {
    return {
        listItems: []
    }
  },
  components: {
    priceComp
  }
}
</script>