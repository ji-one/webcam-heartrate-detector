import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Analysis from '../views/Analysis.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: Analysis
  },
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
