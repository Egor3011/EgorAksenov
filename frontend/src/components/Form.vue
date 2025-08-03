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
            <input v-model="idea" type="text" class="firstname" placeholder="Например Сайт под ключ">
        </div>
        <div>
            <p>Контакт для связи* (номер телефона)</p>
            <input v-model="number" type="tel" id="tel" data-tel-input name="tel" placeholder="+7 (999) 999-99-99" minlength="11" required>
        </div>
        <div style="text-align: center; margin-top: 30px">
            <button @click="onClickSend" style="font-family: 'Bounded'" >Оставить заявку</button>
        </div>
    </div>
</template>


<style scoped>
.containerform {
    padding: 40px;
    border-radius: 30px;
    max-width: 600px;
    height: auto;
    border: 1px solid #ffffff;
}
</style>


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
        axios.post('http://176.123.166.173:80/api/form', {
            name: firstname,
            sname: sname,
            number: number,
            comment: idea
        })
    }
    
};
</script>
