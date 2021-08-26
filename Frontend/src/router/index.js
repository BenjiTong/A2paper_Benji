import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import TestD3 from '@/components/TestD3'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Index',
            component: Index,
            meta: { // 加一个自定义obj
                requireAuth: true // 这个参数 true 代表需要登录才能进入A
            }
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/test_d3',
            name: 'TestD3',
            component: TestD3
        }
    ]
})
