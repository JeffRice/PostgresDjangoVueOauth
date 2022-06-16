import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import gAuthPlugin from './plugins/vue3-google-oauth2'










const app = createApp(App)
let gauthClientId = "";
app.use(gAuthPlugin, { clientId: gauthClientId, scope: 'email', plugin_name:'oauthtest', prompt: 'consent', fetch_basic_profile: false })

app.mount('#app')

