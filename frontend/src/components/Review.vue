<template>
    <div class="containerReview">
        <div style="display: flex; align-items: center;">
            <h2 style="margin-left: 20px;">{{title}}</h2>
        </div>
        <p>{{ info }}</p>
        <a :href="linf" target="_blank">Посмотреть проект</a>
    </div>
</template>

<script>
export default {
  props: {
    title: String,
    info: String,
    logoImg: String,
    link: String
  }
}
</script>

<style>
.containerReview {
    display: inline-block;

    border: 1px solid #ffffff;
    border-radius: 35px;

    padding: 20px;
    height: auto;
    margin: 20px;
    transition: 1s;
    overflow: hidden;
    min-width: 350px;
    width: 40%;
    a {
        text-decoration: underline;
        cursor: pointer;
        transform: translate(0px, 150px);
    }
}

.containerReview:hover {
    box-shadow: 0px 0px 30px #444444;
    transform: translate(-10px, -10px);
    transition: 0.2s;
    a {
        transform: translate(0px, 0px);
    }
}

@media(max-width: 1024px) {
    .containerReview {
        width: calc(80% - 60px);
        min-width: none;
        margin: 0;
    }
}
</style>