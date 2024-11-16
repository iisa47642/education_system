import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "../views/HomeView.vue"
import InfoView from "../views/InfoView.vue"
import ProfileView from "../views/ProfileView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/#about',
      name: 'about',
      component: HomeView
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/info',
      name: 'info',
      component: InfoView
    }
  ]
})

export default router
