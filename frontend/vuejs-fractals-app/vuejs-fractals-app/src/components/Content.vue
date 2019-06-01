<template>
  <div id="content">
    <h1>{{ title }}</h1>
    <form> 
      <div class="inputBox">
        <input type="text" required="">
        <label>username</label>
      </div>
      <div class="inputBox">
        <input type="password" required="">
        <label>password</label>
      </div>
    </form>
    <div class="buttonContainer">
     <button>Log in</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      title: ""
    }
  }
}
</script>

<style>
</style>
