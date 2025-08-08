import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PriceView from '@/views/PriceView.vue'
import FaqView from '@/views/FaqView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/price',
      name: 'price',
      component: PriceView,
    },
    {
      path: '/faq',
      name: 'faq',
      component: FaqView,
    }
  ],
})

export default router
