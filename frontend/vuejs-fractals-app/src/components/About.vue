<template>
    <div class="container">
        <app-menu></app-menu>
        <div class = contentContainer> 
            <h1>About</h1>
        </div>
    </div>
</template>

<script>
import Menu from './Menu.vue'

export default {
    components: {
        'app-menu': Menu
    },
    data(){
        return{

        }
    },
    methods: {
    }
}
</script>
