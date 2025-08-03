<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div class="headerContainer">
        <div class="headerItem">
            <p>EGOR AKSENOV</p>
        </div>
        <div class="routerHeader">
            <RouterLink class="headerItem" to="/" style="margin-right: 60px;">
                <p>Главная</p>
            </RouterLink>
            <RouterLink class="headerItem" to="/price">
                <p>Заказать</p>
            </RouterLink>
        </div>
    </div>
</template>


<style>
.headerContainer {
    display: flex;
    justify-content: space-between;
}

.headerItem {
    font-family: "Bounded";
    height: auto;
    padding: 10px;
    width: auto;
    border-radius: 30px;
    background: var(--textMain);
    color: var(--background);
    margin-bottom: 0px;
    z-index: 4;
    transition: 0.3s;
    p {
        margin: 0px;
    }
}

.headerItem:hover     
{
    background: var(--background);
    color: var(--textMain);
    transition: 0.3s;
}



.routerHeader {
    display: flex;

}
</style>