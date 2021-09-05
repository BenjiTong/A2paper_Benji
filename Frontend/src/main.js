// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import querystring from 'query-string'
import '@/assets/css/bootstrap.css'
import '@/assets/css/stack-interface.css'
import '@/assets/css/theme-serpent.css'
import '@/assets/css/custom.css'

// premise
import VueResource from 'vue-resource'
Vue.prototype.$querystring = querystring
Vue.use(VueResource)

Vue.config.productionTip = false
Vue.http.options.emulateJSON = true

// setting
Vue.prototype.$deployMode = 0 // 0 local 1 ali 2 aws

/* eslint-disable no-new */

function auth () {
    if (sessionStorage['token'] != null) {
        /*
        this.$http.post('/awselb/oauth/islogin', { token: code, state: 'A2inc' }).then((response) => {
            console.log(response.body)
        }, (response) => {
            console.error(response)
        }) */
        return true
    } else {
        return false
    }
}

router.beforeEach((to, from, next) => {
    if (to.meta.requireAuth && !auth()) {
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
