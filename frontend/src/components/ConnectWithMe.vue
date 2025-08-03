<template>
    <div style="display: flex; align-items: start; flex-wrap: wrap;">
        <div style="display: inline-block">
            <Form style="margin-bottom: 60px;"></Form>
        </div>
        <div style="padding-left: 50px;">
            <h1 style="margin-top: 0px;">Мои контакты</h1>
            <h2 class="links_cwm">ТГ: @aksenovegor_web</h2>
            <h2 class="links_cwm">Почта: aksenovegorweb@gmail.com</h2>
            <img src="../assets/img/Artboard 33.png" style="width: 500px; height: auto;">
        </div>
    </div>
</template>

<style scoped>
.links_cwm:hover {
    text-decoration: underline;
    cursor: pointer;
    transition: 0.3s;
}
</style>

<script setup>
import Form from '@/components/Form.vue';
</script>