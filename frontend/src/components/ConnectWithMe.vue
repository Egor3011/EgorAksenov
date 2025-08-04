<template>
    <div class="connectWithMEContainer">
        <div style="display: inline-block" class="formInConWMe">
            <Form></Form>
        </div>
        <div class="connectWithMe-MyInfo">
            <h1 style="margin-top: 0px;">Мои контакты</h1>
            <h2 class="links_cwm">ТГ: @aksenovegor_web</h2>
            <h2 class="links_cwm">Почта: aksenovegorweb@gmail.com</h2>
            <img src="../assets/img/Artboard 33.png">
        </div>
    </div>
</template>

<style scoped>
.links_cwm:hover {
    text-decoration: underline;
    cursor: pointer;
    transition: 0.3s;
}

.connectWithMEContainer {
    gap: 10px;
    display: flex; 
    align-items: start; 
    flex-wrap: wrap;
}

.connectWithMe-MyInfo {
    img {
        width: 30%;
        height: auto;
    }
}

.formInConWMe {
    display: inline-block
}

@media(max-width: 1024px) {
    img {
        visibility: hidden;
        display: none;
    }
    .connectWithMEContainer {
        text-align: center;
    }
    .formInConWMe {
        text-align: center;
    }
}
</style>

<script setup>
import Form from '@/components/Form.vue';

</script>