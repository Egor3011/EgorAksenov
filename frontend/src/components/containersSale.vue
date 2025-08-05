<template>
    <div class="container">
        
        <div class="item">
            <div class="itemContainer">
                <h2>Разработка сайта под ключ</h2>
                <div class="infoBots">
                    <p style="margin-bottom: 15px;">Ваша идея → Готовый проект</p>
                    <p>Полностью разработаю ваш проект от идеи до готового продукта в интернете, который будет помогать в продаже</p>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="itemContainer">
                <div style="display: block;">
                    <h2>Чат-боты</h2>
                    <div class="infoBots">
                        <p>Телеграмм боты</p>
                        <p>ВК боты</p>
                        <p>Дискорд боты</p>
                        <p>Боты для сайта</p>
                    </div>
                    <a href="" style="align-content: end;">Подробнее</a>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="itemContainer">
                <h2>Разработка сайта по готовому макету</h2>
            </div>
        </div>
        <div class="item">
            <div class="itemContainer"></div>
        </div>
    </div>
</template>

<style>
.container {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
  min-height: 800px;
}




.item {
    border-radius: 30px;
    color: var(--textMain);
    border: 1px solid var(--textMain);
    overflow: hidden;
    transition: 0.5s;
    min-height: 370px;
}

.item:hover {
    color: var(--background);
    background: var(--textMain);
    box-shadow: 0px 0px 10px var(--textMain);
    transition: 0.3s;
    a {
        color: var(--background); ;
    }
}

.itemContainer {
    padding: 20px;
    .photoImgContent {
        width: 200px;
        height: 200px;
    }
}


.infoBots p {
    margin: 10px;
}


.item:nth-child(1),
.item:nth-child(4) {
  flex-grow: 1;
  width: 50%;
  height: 30%;
}

.item:nth-child(2),
.item:nth-child(3) {
  flex-grow: 1;
  width: 30%;
  height: 50%;
}

@media(max-width: 1024px) {
    .item:nth-child(1),
    .item:nth-child(3),
    .item:nth-child(4),
    .item:nth-child(2) {
        width: 100%;
    }

    .item {
        width: 90vw;
    }

    .container {
        gap: 30px
    }
}
</style>