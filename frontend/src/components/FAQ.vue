<template>
    <details name="how">
        <p>{{info}}</p>
        <summary>
            <span style="font-size: 20px; font-family: 'Bounded';">{{title}}</span>
        </summary>
    </details>
</template>


<script setup>
defineProps({
    title: String,
    info: String
});
</script>