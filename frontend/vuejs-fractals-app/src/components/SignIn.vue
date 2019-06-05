<template>
  <div class="container">
    <app-menu></app-menu>
    <div class="contentContainer">
      <h1>Sign in</h1>
      <form class="login" @submit.prevent="login">
        <div class="inputBox">
          <input type="text" required v-model="user.username">
          <label>username</label>
        </div>
        <div class="inputBox">
          <input type="password" required v-model="user.password">
          <label>password</label>
          <div class="buttonContainer">
            <button type="submit">Log in</button>
          </div>
        </div>
      </form>
      <div ref="csrf" id="test" style="display:none;" v-html="data"></div>
    </div>
  </div>
</template>

<script>
import { router } from '../routes';
import { userService } from '../services';
import Menu from './Menu.vue'

export default {
  components: {
    'app-menu': Menu
  },
  data () {
    return {
      error: false,
      user: {
        username: '',
        password: ''
      },
      returnUrl: '',
      submitted: false,
      data: '',
      csrf_token: '',
      csrfmiddlewaretoken: ''
    }
  },
   created () {
      userService.logout();
      this.returnUrl = this.$route.query.returnUrl || '/signin';
    },

    methods: {
      login: function(){
        const LOGIN_PAGE_URL = 'http://0.0.0.0:8000/login/'
        const formData = new FormData();
        formData.append('username', this.user.username);
        formData.append('password', this.user.password);

        this.$http.post(LOGIN_PAGE_URL, formData)
          .then(response => this.loginSuccessful(response))
          .catch(() => this.loginFailed())
      },

      loginSuccessful (req) {
        const RESPONSE = '<!DOCTYPEhtml><html><head><metacharset="utf-8"><title>Home</title></head><body><main><p>Youarenotloggedin</p><ahref="/login/">login</a></main></body></html>';  

        const REQ = req.bodyText.replace(/\s/g,"");

        if(REQ === RESPONSE) {
          localStorage.username = this.user.username;
          this.$router.replace(this.$route.query.redirect || '/online')
        } else {
          this.loginFailed();
        }
      },

      loginFailed () {
       alert('Login failed');
      },
  }
};
</script>

<style>
</style>
