// import { authHeader } from "../../../../../../AIiR/Fractals App/vuejs-fractals-app/src/auth-header";
import Vue from 'vue'
import VueResource from "vue-resource"
Vue.use(VueResource);

export const userService = {
    login,
    logout
  };

  function login(username, password) {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password, grant_type: "password"})
    };
    Vue.http.post('http://localhost:8082/oauth/token', requestOptions)
    .then(handleResponse)
    .then(user => {
      if (user) {
        user.authdata = window.btoa(username + ":" + password);
        localStorage.setItem("user", JSON.stringify(user));
      }

      return user;
    }
    )
    .catch(err => {
        localStorage.removeItem('user-token') // if the request fails, remove any possible user token if possible
      });
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('username');
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}

// function getAll() {
//   const requestOptions = {
//       method: 'GET',
//       headers: authHeader()
//   };

//   // return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
// }