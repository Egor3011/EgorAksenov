<template>
    <div class="priceContainer">
        <img :src="imgLogo" alt="">
        <div class="mainText">
            <h2 class="nameUslugi" style="margin-top: 0px;">{{title}}</h2>
            <p>{{info}}</p>
            <a :href="linkExample">Посмотреть примеры</a>
        </div>
        <div class="priceText" style="width: 15%;">
            <h2>Цена:</h2>
            <p>{{price}}</p>
            <h3>{{date}}</h3>
        </div>
    </div>
</template>


<script>
export default {
  props: {
    title: String,
    info: String,
    price: String,
    date: String,
    linkExample: String,
    imgLogo: String
  }
}
</script>

<style>
.priceContainer {
    border-radius: 30px;
    border: 1px solid var(--textMain);
    padding: 30px;
    height: auto;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: 0.3s;
    margin: 20px;
    img {
        width: 70px;
        height: 70px;
        margin: 3%;
    }
}

.priceContainer:hover {
    box-shadow: 0px 0px 20px #b8b8b8;
    transition: 0.2s;
    transform: translate(0px, -5px);
}
</style>
