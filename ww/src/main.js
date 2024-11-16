import './assets/nullstyle.css'
import './assets/main.css'
import axios from "axios";
axios.defaults.baseURL = 'http://localhost:8000';


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
