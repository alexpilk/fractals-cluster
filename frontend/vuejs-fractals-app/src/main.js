import Vue from 'vue'
import App from './App.vue'
import { router } from './routes.js'
import VueResource from 'vue-resource';
import VueCsrf from 'vue-csrf';
import VueCookies from 'vue-cookies';
// var VueResource = require('vue-resource');

Vue.use(VueResource);
Vue.use(VueCsrf);
Vue.use(VueCookies);

// const router = new VueRouter({
//   routes: Routes
// });

new Vue({
  el: '#app',
  render: h => h(App),
  router
})
// }).$mount('#app')
