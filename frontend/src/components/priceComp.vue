<template>
    <div class="priceContainer">
        <img :src="imgLogo" alt="">
        <div class="mainText">
            <h2 class="nameUslugi" style="margin-top: 0px;">{{title}}</h2>
            <p>{{info}}</p>
            <a :href="linkExample">Таблица с расчетом</a>
        </div>
        <div class="priceText">
            <h2>Цена:</h2>
            <div class="price-A-dateText">
                <h3>{{price}}</h3>
                <p>{{date}}</p>
            </div>
        </div>
    </div>
</template>

<style>
.priceContainer {
    border-radius: 30px;
    border: 1px solid var(--textMain);

    margin: auto;
    padding: 30px;

    height: auto;

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

.priceText {
    width: 30%;
    p {
        font-size: 15px;
    }
}

@media(max-width: 1024px) {
    .priceContainer {
        display: block;
        text-align: center;
    }

    .priceText {
        display: flex;
        justify-content: space-between;
        align-items: start;
        width: 100%;
    }

    .price-A-dateText {
        display: block;
        text-align: end;

    }

    .price-A-dateText p {
        font-size: 3vw;
    }
}
</style>


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


