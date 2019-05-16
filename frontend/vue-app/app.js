// -----------------  home component ------------------------------
var home = {
    template: `
    <div class = contentContainer> 
        <h1>The Online<br>Fractal<br>Generator</h1>
    </div>`
};
// ----------------- sign-in component ----------------------------
var signin = {
    props: ['authorization'],
    template: `
    <div class="contentContainer">
    <h1>Sign in</h1>
    <form action="#"> 
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
     <button type="submit" v-on:click.prevent="login">Log in</button>
    </div>
  </div>`,
  data() {
      return {
        error: false,
        user: {
            username: '',
            password: ''
        }
      }
  },
  methods: {
    login: function(){
        this.$http.post('http://35.238.239.157:8000/login/' ,{
            username: this.user.username,
            password: this.user.password})
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
            }
  }
};
// ---------------- sign-up component ------------------------------
var signup = {
    template: `
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
    `,
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
    // <div class="inputBox">
            //     <input type="password" required="">
            //     <label>confirm password</label>
            // </div></div>
};
// ---------------- About component -------------------------------
var about = {
    template: `
    <div class="contentContainer">
        <h1>About</h1>
    </div>
    `
};
// ---------------------- Online ----------------------------------
var online = {
    template: `
    <div class="fractalContainer">
            <div class="imgContainer">
                <img v-bind:src="imgSrc" alt="">
            </div>
            <div class="formContainer">
                <h1>Data to generate fractal</h1>
                <form >
                    <div class="inputBox">
                        <label for="">Name:</label>
                        <select v-model="fractal.selectedName">
                            <option v-for="fractalName in fractalsName":value="fractalName">{{ fractalName }}</option>
                        </select>
                    </div>
                    <div class="inputBox">
                        <label for="">Max iterations:</label>
                        <input type="text" v-model="fractal.maxIt">
                    </div>
                    <div class="inputBox">
                        <label for="">re:</label>
                        <input type="text" v-model="fractal.re">
                    </div>
                    <div class="inputBox">
                        <label for="">im:</label>
                        <input type="text" v-model="fractal.im">
                    </div>
                    <div class="inputBox">
                        <label for="">h:</label>
                        <input type="text" v-model="fractal.h">
                    </div>
                    <div class="inputBox">
                        <label for="">w:</label>
                        <input type="text" v-model="fractal.w">
                    </div>
                    <div class="inputBox">
                        <label for="">p1:</label>
                        <input type="text" v-model="fractal.p1">
                    </div>
                    <div class="inputBox">
                        <label for="">k1:</label>
                        <input type="text" v-model="fractal.k1">
                    </div>
                    <div class="inputBox">
                        <label for="">p2:</label>
                        <input type="text" v-model="fractal.p2">
                    </div>
                    <div class="inputBox">
                        <label for="">k2:</label>
                        <input type="text" v-model="fractal.k2">
                    </div>
                </form>
                <div class="buttonContainer">
                    <button v-on:submit.prevent="sendFractal">send</button>
                </div>
            </div>
        </div>
    `,
    data(){
        return{
            imgSrc: '',
            fractalsName: [
                "mandelbrot",
                "julia"
            ],
            fractal: {
                selectedName: '',
                maxIt: '',
                re: '',
                im: '',
                h: '',
                w: '',
                p1: '',
                k1: '',
                p2: '',
                k2: ''
            }
        }
    },
    methods: {
        sendFractal: function(){
            axios.post('http://35.238.239.157:8000/fractal/', { 
                name: this.fractal.selectedName,
                maxIt: this.fractal.maxIt,
                re: this.fractal.re,
                im: this.fractal.im,
                h: this.fractal.h,
                w: this.fractal.w,
                p1: this.fractal.p1,
                k1: this.fractal.k1,
                p2: this.fractal.p2,
                k2: this.fractal.k2
            }).then(function(data){
                
            });
        },
        getFractal: function(){
            this.$http.get('http://35.238.239.157:8000/fractal/').then(function(data, status, reques) {
                if(status == 200){          // czt na pewno?? 
                    this.imgSrc = data;
                }
            })
        }
    },
};
//------------------- routes --------------------------------------
var routes = [
    {path: '/', component: home},
    {path: '/signin', component: signin},
    {path: '/signup', component: signup},
    {path: '/abuot', component: about},
    {path: '/online', component: online}
];

var router = new VueRouter({
    routes: routes
});

// --------------------- vue app -----------------------------------
const app = new Vue({
    el: '#app',
    router: router,
    data: {
        authorization: false
    },
    methods: {    
    }
});