<template>
  <div id="menu">
    <h2>Fractals</h2>
    <nav id="nav">
      <ul>
        <li><router-link to="/online">Fractal</router-link></li>
        <li><router-link to="/online">Profile</router-link></li>
        <li v-on:click="logout"><router-link to="/signin">Log out</router-link></li>
        <!-- <li><router-link to="/about">About</router-link></li> -->
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Fractals App',
  data () {
    return {
    }
  },
  methods: {
      logout: function() {
          localStorage.removeItem('username');
      }
  }
}
</script>

<style scoped>
#menu {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

h2 { 
    font-size: 2em;
}
#nav a {
    color: #fff;
    text-decoration: none;
    display: block;
    padding: 15px;
}

#nav ul {
    list-style: none;
    display: flex;
}

#nav ul li {
    font-size: 1.4em;
    color: #fff;
    text-decoration: none;
    display: block;
    padding: 15px;
}

#nav a:hover {
    color: #000;
    background: #fff;
}
</style>
