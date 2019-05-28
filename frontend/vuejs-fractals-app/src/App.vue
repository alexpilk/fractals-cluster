<template>
  <div>
    <app-menu></app-menu>
    <router-view></router-view>
  </div>
</template>

<script>
// imports 
import Menu from './components/Menu.vue'

export default {
  components: {
    'app-menu': Menu,
  },
  data () {
    return {
    }
  }
}

</script>

<style>
html {
    background: url(./assets/background.jpg) no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}

body {
    font-family: 'Lato', sans-serif;
    color: #FFF;
    font-weight: bold;
    margin: 0;
    padding: 0;
}
#app {
  display: grid;
  grid-template-columns: 100%;
  grid-template-rows: min-content;
}

/* content */
.contentContainer {
    position: relative;
    left: 50%;
    display: flex;
    flex-wrap: nowrap;
    align-items: center;
    /* ******** dopracować wyśrodkowanie w przypadku HOME ********** */
    justify-content: center;
    height: 70vh;
    width: 400px;
    flex-direction: column;
}

.contentContainer h1 {
    font-size:3em;
    text-align: center;
}

.contentContainer h1, form, .buttonContainer {
     position: relative;
}

.contentContainer .inputBox {
    position: relative;
}

.contentContainer .inputBox input {
    border: 0;
    text-align: left;
    font-weight: bold;
    /* padding: 14px 10px; */
    margin: 3px;
    width: 210px;
    height: 40px;
    background: none;
    border: 3px solid #09002b;
    border-radius: 24px;
    outline: none;
    transition: 0.25s;
} 
.contentContainer label {
    color: #98eaff;
    position: absolute;
    top: 10px;
    left: 15px;
    pointer-events: none;
    transition: .3s;
}

.contentContainer.inputBox input:focus ~ label,
.contentContainer .inputBox input:valid ~ label {
    top: 2px;
    font-size: .8em;
    outline: none;
}

.contentContainer .inputBox :required {
    box-shadow: none;
}
.contentContainer .inputBox input:focus {
    /* width: 280px; */
    border-color: #98eaff;
    color: #09002b;
} 

.buttonContainer button{
    border: 0;
    background-color: #09002b;
    margin: 10px;
    width: 200px;
    height: 40px;
    text-align: center;
    font-size: 1em;
    color: white;
    font-weight: bold;
    border: 3px solid rgb(9, 0, 43);
    outline: none;
    border-radius: 24px;
    transition: 0.25s;
}

.buttonContainer button:hover {
    color: rgb(9, 0, 43);
    background-color: #98eaff;
    border-color: #98eaff;
    
}
</style>
