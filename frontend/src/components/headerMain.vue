<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div class="headerContainer">
        <RouterLink class="headerItem" to="/">
            <p>EGOR AKSENOV</p>
        </RouterLink>
        <RouterLink class="headerItem" to="/price">
            <p>Заказать</p>
        </RouterLink>
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
    width: auto;

    padding: 10px;
    
    text-align: center;
    align-items: center;

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