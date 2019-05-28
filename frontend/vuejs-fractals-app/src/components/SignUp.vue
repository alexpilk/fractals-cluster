<template>
    <div class="contentContainer">
        <h1>Sign up</h1>
        <form v-on:submit.prevent="register">
            <div class="inputBox">
                <input type="text" required="" v-model="user.email">
                <label>email</label>
            </div>
            <div class="inputBox">
                <input type="text" required="" v-model="user.username">
                <label>username</label>
            </div>
            <div class="inputBox">
                <input type="password" required="" v-model="user.password">
                <label>password</label>
            </div>
        </form>
        <div class="buttonContainer">
            <button type="submit">Sign up</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
          user: {
              email: '',
              username: '',
              password: ''
          }
        }
    },
     methods: {
        register: function(){
            this.$http.post('http://35.238.239.157:8000/signup/' ,{
                email: this.user.email,
                username: this.user.username,
                password: this.user.password})
            .then(request => this.registerSuccessful(request))
            .catch(() => this.registerFailed())
            },
            registerSuccessful (req) {
                if(!req.data.token) {
                    this.registerFailed();
                    return;
                }
                localStorage.token = req.data.token;
                this.error = false;
                this.$router.replace(this.$route.query.redirect || '/signin')
            },
            registerFailed () {
                this.error = 'Registration failed!';
                delete localStorage.token;
            },
        }
}
</script>
