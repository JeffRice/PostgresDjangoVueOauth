<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
      <h1>IsInit: {{ Vue3GoogleOauth.isInit }}</h1>
      <h1>IsAuthorized: {{ Vue3GoogleOauth.isAuthorized }}</h1>
      <h2 v-if="user">signed user: {{user}}</h2>
      <button @click="handleClickSignIn" :disabled="!Vue3GoogleOauth.isInit || Vue3GoogleOauth.isAuthorized">sign in</button>
      <button @click="handleClickGetAuthCode" :disabled="!Vue3GoogleOauth.isInit">get authCode</button>
      <button @click="handleClickSignOut" :disabled="!Vue3GoogleOauth.isAuthorized">sign out</button>
      <button @click="handleClickDisconnect" :disabled="!Vue3GoogleOauth.isAuthorized">disconnect</button>
    </div>
  </div>
      <button @click="testAxios">Get Github Repos</button>
        <div @click="handleClick" id="repos"></div>
   </template>
<script>


import { inject, toRefs } from "vue";
const axios = require('axios').default;

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
 mounted() {

   const gitLogin = this.gitLogin = JSON.parse(document.getElementById('git-name').textContent);
   const djangoLogin = this.djangoLogin = JSON.parse(document.getElementById('django-name').textContent);
   const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  console.log(gitLogin);
  console.log(djangoLogin);
  console.log(csrftoken);
  },





  data(){
    return {
      user: '',  eventname: 'click',
    }
  },
  methods: {
    async handleClickSignIn(){
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        console.log("googleUser", googleUser);
        this.user = googleUser.getBasicProfile().getEmail();
        console.log("getId", this.user);
        console.log("getBasicProfile", googleUser.getBasicProfile());
        console.log("getAuthResponse", googleUser.getAuthResponse());
        console.log(
          "getAuthResponse",
          this.$gAuth.instance.currentUser.get().getAuthResponse()
        );
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },
    async handleClickGetAuthCode(){
      try {
        const authCode = await this.$gAuth.getAuthCode();
        console.log("authCode", authCode);
      } catch(error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },
    async handleClickSignOut() {
      try {
        await this.$gAuth.signOut();
        console.log("isAuthorized", this.Vue3GoogleOauth.isAuthorized);
        this.user = "";
      } catch (error) {
        console.error(error);
      }
    },
    handleClickDisconnect() {
      window.location.href = `https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=${window.location.href}`;
    },
    testAxios() {    
      axios.get('https://api.github.com/users/' + this.gitLogin + '/repos')
  .then(function (response) {
    // handle success
    console.log(response);

    var Data = response.data;
    console.log(Data);

    const reposDiv = document.getElementById('repos');

    for (let i = 0; i < Data.length; i++) {
    reposDiv.innerHTML += "<li><button @click='handleClick' class='repoItem'>" + Data[i].name + "</button></li>";
     }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed

  });
    },
handleClick(e) {
      const elt = e.target.closest(".repoItem");
      if (elt) {
        console.log("this:", this)
        console.log("elt:", elt)
        console.log(elt.innerText)
        const clickedRepo = elt.innerText
        this.saveRepo(clickedRepo);
      }

    },
saveRepo(clickedRepo) {
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(csrftoken)
      axios.get('http://localhost:8000/api/usernotes?username='  + this.djangoLogin)

  .then(function (response) {
    // handle success

    console.log(response);
    console.log(response.data);
    console.log('previously chosen repo: ', response.data[0].selectedRepo);
    console.log(clickedRepo);
    console.log(response.data[0].id);


    const userID = response.data[0].id;
    let newRecord = response.data[0];
    newRecord.selectedRepo = clickedRepo;


    console.log(newRecord)


let apiresponse = fetch("http://localhost:8000/api/usernotes/" + userID + "/", {
    method: 'put',
    body: JSON.stringify(newRecord),
    headers: { "X-CSRFToken": csrftoken, 'Content-Type': 'application/json', },
})

console.log(apiresponse)



  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {

    // always executed

  });
},

    
  },
  setup(props) {
    const { isSignIn } = toRefs(props);
    const Vue3GoogleOauth = inject("Vue3GoogleOauth");
    const handleClickLogin = () => {};
    return {
      Vue3GoogleOauth,
      handleClickLogin,
      isSignIn,
    };
  },
};




</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: 0;
  margin: 0;
  -webkit-transition: 0.1s;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
  margin-right: 1em;
}
button:disabled {
  background: #fff;
  color: #ddd;
  cursor: not-allowed;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
