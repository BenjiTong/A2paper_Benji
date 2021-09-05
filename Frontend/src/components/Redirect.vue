<template>
    <h4>Redirecting...</h4>
</template>

<script>

export default {
    data: function () {
        return {
            txtReg: /\?\bcode\b=/
        }
    },

    mounted () {
        let url = window.location.href
        // if url match regular expression, or redirect to index
        if (this.txtReg.test(url)) {
            /*
            let afterQuestion = url.split('?')[1]
            let paramPairs = afterQuestion.split('&')
            let code = paramPairs[0].split('=')[1]
            */
            let code = this.$route.query.code
            let state = this.$route.query.state
            console.log('code: ' + code)
            console.log('state: ' + state)
            console.log('deploayMode: ' + this.$deployMode)

            this.$http.post('/awselb/oauth/token',
                {
                    code: code,
                    state: 'A2inc'
                }
            ).then((response) => {
                console.log(response.body)
                this.prototype.$usrInfo = response.body.user
                sessionStorage.setItem('token', response.body.token)
                this.$router.push({ name: 'Index', query: { id: this.$usrInfo.id } })
            }, (response) => {
                console.error(response)
                this.$router.push({ name: 'Login' })
            })

            /*
            this.$http({
                url: this.$http.adornUrl(''),
                method: 'post',
                data: this.$http.adornData({
                    code: code,
                    state: 'A2inc'
                })
            }).then((response) => {
                console.log(response.body)
            }, (response) => {
                console.error(response)
            })
            */

            // temporarily enter index
            // Temp create fake token
            // sessionStorage.setItem('token', '123')
            // this.$router.push({ name: 'Index', query: { username: 'xxx' } })
        } else {
            this.$router.push({ name: 'Login' })
        }
    }
}
</script>
