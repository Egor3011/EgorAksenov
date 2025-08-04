<template>
    <div class="radio-group">
        <input type="radio" id="option1" name="myRadio" value="1">
        <label for="option1">Опция 1</label>
    </div>

    <div class="radio-group">
        <input type="radio" id="option2" name="myRadio" value="2" checked>
        <label for="option2">Опция 2</label>
    </div>

    <div class="radio-group">
        <input type="radio" id="option3" name="myRadio" value="3">
        <label for="option3">Опция 3</label>
    </div>
</template>

<style>
/* Для наглядности, устанавливаем темный фон для всего тела страницы */
/* Скрываем нативную радио-кнопку */
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