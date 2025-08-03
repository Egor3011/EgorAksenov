<template>
    <div style="text-align: center;">
        <div class="firstBlock">
            <img src="../assets/img/E5424_33.png">
            <h1>Разработка сайтов которые работают</h1>
        </div>
    </div>
</template>

<style>
.firstBlock {
    position: relative;
    height: 100vh;
    width: 90%;
    display: flex;
    align-items: center;
    margin: auto;
    img {
        width: 100%;
        height: auto;
        z-index: 0;
        position: absolute;
    }
    h1 {
        font-size: 65px;
        z-index: 1;
        position: absolute;
    }
}

@media(max-width: 1024px) {
    .firstBlock {
        h1 {
            font-size: 7vw;
        }
    }
}
</style>