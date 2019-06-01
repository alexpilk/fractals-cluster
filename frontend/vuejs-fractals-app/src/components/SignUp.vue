<template>
    <div class="container">
        <app-menu></app-menu>
        <div class="contentContainer">
            <h1>Sign up</h1>
            <form v-on:submit.prevent="register">
                <div class="inputBox">
                    <input type="text" required="" v-model="user.username">
                    <label>username</label>
                </div>
                <div class="inputBox">
                    <input type="password" required="" v-model="user.password">
                    <label>password</label>
                </div>
                <div class="inputBox">
                    <input type="password" required="" v-model="user.confirmPassword">
                    <label>confirm password</label>
                </div>
                <div class="buttonContainer">
                    <button type="submit">Sign up</button>
                </div>
            </form>
            
        </div>
    </div>
</template>

<script>
import Menu from './Menu.vue'

export default {
    components: {
        'app-menu': Menu
    },
    data() {
        return {
          user: {
              username: '',
              password: '',
              confirmPassword: '',
          }
        }
    },
     methods: {
        register: function(){
            const REGISTER_PAGE_URL = 'http://35.238.239.157:8000/signup/';
            const formData = new FormData();
            formData.append('username', this.user.username);
            formData.append('password1', this.user.password);
            formData.append('password2', this.user.confirmPassword);

            this.$http.post(REGISTER_PAGE_URL, formData)
            .then(response => this.registerSuccessful(response))
            .catch(() => this.registerFailed())
            },

            registerSuccessful (req) {
                const RESPONSE = '<title>Login</title>';

                const REQ = req.bodyText.search(RESPONSE);
                if(REQ !== -1){
                    this.$router.replace(this.$route.query.redirect || '/signin')
                } else {
                    this.registerFailed();
                }
            },
            registerFailed () {
                alert('Registration failed');
            },
        }
}
</script>
