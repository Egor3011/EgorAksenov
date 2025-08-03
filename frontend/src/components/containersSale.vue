<template>
    <div class="container">
        <div class="item">
            <div class="itemContainer" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div>
                    <h2>Чат-боты</h2>
                    <div class="infoBots">
                        <p>Телеграмм боты</p>
                        <p>ВК боты</p>
                        <p>Дискорд боты</p>
                        <p>Боты для сайта</p>
                    </div>
                </div>
                <img src="../assets/img/Artboard75.png" class="photoImgContent" style="rotate: 15deg;">
            </div>
        </div>
        <div class="item">
            <div class="itemContainer">
                <h2>Разработка сайта под ключ</h2>
                <div class="infoBots">
                    <p style="margin-bottom: 15px;">Ваша идея > План > Готовый проект</p>
                    <p>Полностью разработаем ваш проект от идеи до готового продукта в интернете, который будет помогать в продаже</p>
                </div>
            </div>
        </div>
        <div class="item">
            <div class="itemContainer"></div>
        </div>
        <div class="item">
            <div class="itemContainer"></div>
        </div>
    </div>
</template>

<style>
.container {
  display: flex;
  gap: 50px;
  flex-wrap: wrap;
  min-height: 700px;
}

.item:nth-child(1) {
  flex-grow: 1;
  width: 50%;
  height: 50%;
}

.item:nth-child(2),
.item:nth-child(3) {
  flex-grow: 1;
  width: 40%;
  height: 50%;
}

.item:nth-child(4) {
  width: 50%;
  height: 50%;
}

.item {
    border-radius: 30px;
    color: var(--textMain);
    border: 1px solid var(--textMain);
    overflow: hidden;
    transition: 0.5s;
    min-width: 400px;
    min-height: 370px;
}

.item:hover {
    color: var(--background);
    background: var(--textMain);
    box-shadow: 0px 0px 10px var(--textMain);
    transition: 0.3s;
}

.itemContainer {
    padding: 20px;
    h2 {
        font-size: 38px;
    }
    .photoImgContent {
        width: 330px;
        height: 330px;
    }
}


.infoBots p {
    margin: 10px;
}

@media(max-width: 1024px) {
    .itemContainer {
        width: 100%;
    }
}
</style>