<template>
  <div class="contentContainer">
    <h1>Sign in</h1>
    <form class="login" @submit.prevent="getCsrf">
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
</template>

<script>
import { router } from '../routes';
import { userService } from '../services';

export default {
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
        // reset login status
      // this.getCsrf();
      userService.logout();

        // get return url from route parameters
      this.returnUrl = this.$route.query.returnUrl || '/signin';
    },
    methods: {
      // handleSubmit (e) {
      //   this.submitted = true;
      //   const { username, password } = this;


      // if (!(username && password)) {
      //           return;
      //       }

      //   userService.login(username, password)
      //   .then(
      //       user => router.push(this.returnUrl),
      //       error => {
      //       this.error = error;
      //      }
      //    );

      // },
      login: function(){
        const LOGIN_PAGE_URL = 'http://35.238.239.157:8000/login/';
        this.$cookies.set('csrftoken', this.csrf_token);
        let csrf = this.$cookies.get('csrftoken');

        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          data: JSON.stringify({'csrfmiddlewaretoken': this.csrfmiddlewaretoken, 'username': this.user.username, 'password': this.user.password}),
          cookies: {
            'csrftoken': this.csrf_token
          }
        };
        
        // this.csrf_token = this.$cookies.get('csrftoken');
        // const requestOptions = {
        //   method: "POST",
        //   data: JSON.stringify({'csrfmiddlewaretoken': csrf, 'username': this.user.username, 'password': this.user.password}), 
        //   headers: {'X_CSRFTOKEN': csrf }
        // }
        this.$http.post(LOGIN_PAGE_URL, requestOptions)
          .then(request => this.loginSuccessful(request))
          .catch(() => this.loginFailed())
      },
      loginSuccessful (req) {
        if(!req.data.token) {
          this.loginFailed();
          return;
        }
        localStorage.token = req.data.token;
        this.error = false;
        this.authorization = true;
        this.$router.replace(this.$route.query.redirect || '/online')
      },
      loginFailed () {
        this.error = 'Login failed!';
        delete localStorage.token;
      },

      getCsrf: function() {
        const LOGIN_PAGE_URL = 'http://35.238.239.157:8000/login/';
        this.$http.get(LOGIN_PAGE_URL)
          .then(function(request) {
          this.data = request.bodyText;

          let t = this;
          setTimeout(function(){
            let inputs = document.getElementsByTagName('input');
            t.csrf_token = inputs.item(2).value;
            t.csrfmiddlewaretoken = t.csrf_token;
            t.login();
          }, 1000);
      });
     }
  }
};
</script>

<style>
</style>
