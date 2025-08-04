<template>
    <div class="containerform">
        <h2 style="text-align: center; margin-top: 0px;">Оставьте контакты для связи</h2>
        <div>
            <div>
                <p>Имя*</p>
                <input v-model="firstname" type="text" class="secondname" placeholder="Иван" required>
            </div>
            <div style="">
                <p>Фамилия*</p>
                <input v-model="sname" type="text" class="firstname" placeholder="Иванов" required>
            </div>
        </div>
        <div>
            <p>Онлайн продукт (например сайт под ключ)</p>
            <div>
                <div class="radio-group">
                    <input type="radio" id="option1" name="idea" value="Сайт под заказ" v-model="idea">
                    <label for="option1">Сайт под ключ</label>
                </div>

                <div class="radio-group">
                    <input type="radio" id="option2" name="idea" value="Чат-бот" v-model="idea">
                    <label for="option2">Чат-бот</label>
                </div>

                <div class="radio-group">
                    <input type="radio" id="option3" name="idea" value="Верстка сайта" v-model="idea">
                    <label for="option3">Верстка сайта</label>
                </div>

                <div class="radio-group">
                    <input type="radio" id="option4" name="idea" value="Другое" v-model="idea">
                    <label for="option4">Другое</label>
                </div>
            </div>
        </div>
        <div>
            <p>Контакт для связи* (номер телефона)</p>
            <input v-model="number" type="tel" id="tel" data-tel-input name="tel" placeholder="+7 (999) 999-99-99" minlength="11" required>
        </div>
        <div style="text-align: center; margin-top: 30px">
            <button class="buttonConnectWithMe" @click="onClickSend" style="font-family: 'Bounded'" >Оставить заявку</button>
        </div>
    </div>
</template>



<script setup>
import axios from 'axios';

let firstname = '';
let sname = '';
let number = '';
let idea = '';

const onClickSend = () => {
    if (firstname == '' || sname == '' || idea == '' || number == '') {
        alert("Заполните все поля!")
    }
    else {
        confirm("Отправить данные?")
        axios.post('http://aksenovegor.ru/api/form', {
            name: firstname,
            sname: sname,
            number: number,
            comment: idea
        }).catch(error => {
            alert(error)
        })
    }
    
};
</script>


<style scoped>
.containerform {
    padding: 40px;
    border-radius: 30px;
    max-width: 600px;
    height: auto;
    border: 1px solid #ffffff;

    text-align: start;
}

@media(max-width: 1024px) {
    .containerform {
        width: 80%;
        padding: 20px;

        margin: auto;
    }
    .buttonConnectWithMe {
        font-size: 4.5vw;
        width: 100%;
    }
}



input[type="radio"] {
    /* Делаем ее невидимой, но оставляем функциональной и доступной для фокусировки */
    opacity: 0;
    position: absolute;
    width: 0;
    height: 0;
    pointer-events: none; /* Не реагирует на события мыши напрямую */
}

/* Стили для контейнера вокруг радио-кнопки и метки */
.radio-group {
    margin-bottom: 10px;
    display: flex; /* Для выравнивания кастомной кнопки и текста */
    align-items: center;
}

/* Стили для метки (label), которая будет содержать наш кастомный элемент */
.radio-group label {
    position: relative; /* Для позиционирования псевдо-элемента */
    padding-left: 25px; /* Отступ для нашей кастомной кнопки */
    cursor: pointer;
    user-select: none; /* Запрещает выделение текста при двойном клике */
    min-height: 15px; /* Гарантируем минимальную высоту для выравнивания */
    display: flex;
    align-items: center;
}

/* Создаем кастомную кнопку с помощью ::before псевдо-элемента */
.radio-group label::before {
    content: ''; /* Обязательно для псевдо-элементов */
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%); /* Центрирование по вертикали */

    width: 15px;
    height: 15px;
    border: 1px solid white; /* Белый контур, 1px */
    border-radius: 50%; /* Круглая форма */
    background-color: transparent; /* Без заднего фона */
    box-sizing: border-box; /* Убедимся, что border учитывается в размерах */

    /* Добавляем плавный переход для эффекта нажатия */
    transition: background-color 0.2s ease, border-color 0.2s ease;
}

/* Состояние, когда радио-кнопка НАЖАТА (checked) */
input[type="radio"]:checked + label::before {
    background-color: white; /* Полностью белая */
    border-color: white; /* Контур тоже белый, чтобы сливался */
}

/* Состояние фокусировки для доступности (когда на кнопку перешли по Tab) */
input[type="radio"]:focus + label::before {
    box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.4); /* Легкая белая тень для фокуса */
}

/* Опционально: стиль для отключенных (disabled) кнопок */
input[type="radio"]:disabled + label {
    opacity: 0.6;
    cursor: not-allowed;
}

input[type="radio"]:disabled + label::before {
    border-color: rgba(255, 255, 255, 0.4);
    background-color: transparent;
}

input[type="radio"]:disabled:checked + label::before {
    background-color: rgba(255, 255, 255, 0.4);
}
</style>