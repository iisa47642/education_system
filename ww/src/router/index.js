import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "../views/HomeView.vue"
import InfoView from "../views/InfoView.vue"
import ProfileView from "../views/ProfileView.vue"
import LoginView from "../views/LoginView.vue"
import CoursesView from "../views/CoursesView.vue"
import SheduleView from "../views/SheduleView.vue"

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
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/profile/:id/courses',
      name: 'courses',
      component: CoursesView
    },
    {
      path: '/profile/:id/shedule',
      name: 'shedule',
      component: SheduleView
    }
  ]
})

export default router
