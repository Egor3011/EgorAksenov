<template>
    <h1>AKSENOV EGOR</h1>
    <div style="display: flex; flex-wrap: wrap;" class="footerContainer">
        
        <div class="links itemFooter">
            <button @click="scrolToById('connectWithMe')">Связаться со мной</button>
            <button @click="scrolToById('reviews')">Отзывы</button>
            <button @click="scrolToById('faq')">Частые вопросы</button>
        </div>
        <div class="myContacts itemFooter">
            <a href=" https://t.me/aksenovegor_web" target="_blank">@aksenovegor_web</a>
            <a href="" target="_blank">aksenovegorweb@gmail.com</a>
        </div>
        <div class="myContacts itemFooter">
            <a href="aksenovegor.ru">aksenovegor.ru</a>
        </div>
    </div>
    
</template>

<style>
a {
    display: block;
    margin-bottom: 19px;
    color: var(--textMain);
}

.itemFooter {
    width: 33%;
    min-width: 320px;
    margin-bottom: 40px;
    button {
        display: block;
        margin: 0%;
        margin-bottom: 19px;
        color: var(--textMain);

        border: none;
        background: none;

        text-decoration: underline;
        font-family: "Montserrat-Regular";

        text-align: start;
        align-items: start;

        width: auto;
        height: auto;

        padding: 0;

        transition: .2s;
    }
    button:hover {
        color: var(--textSecond);
        transition: .1s;
    }
}

@media(max-width: 1024px) {
    a {
        font-size: 4vw;
    }
    .itemFooter button {
        font-size: 4vw;
    }
}
</style>

<script setup>

const scrolToById = (idTo) => {
    const currentUrl = window.location.href;
    if (currentUrl == 'https://aksenovegor.ru/price') {
        window.open("https://aksenovegor.com");
    }
    const element = document.getElementById(idTo);
    element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
}
</script>