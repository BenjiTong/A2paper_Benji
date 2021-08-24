// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import '@/assets/css/socicon.css'
import '@/assets/css/bootstrap.css'
import '@/assets/css/stack-interface.css'
import '@/assets/css/theme-serpent.css'
import '@/assets/css/custom.css'

Vue.config.productionTip = false

/* eslint-disable no-new */

function fakeAuth () {
    if (sessionStorage['token'] != null) {
        return true
    } else {
        return false
    }
}

router.beforeEach((to, from, next) => {
    if (to.meta.requireAuth && !fakeAuth) {
        // Check login state
        next({ path: '/login' })
    } else {
        next()
    }
})

new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
