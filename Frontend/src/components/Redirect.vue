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
        /*
        console.log(url)
        console.log(this.txtReg)
        console.log(url.match(this.txtReg))
        console.log(this.txtReg.test(url))
        */
        // if url match regular expression, or redirect to index
        if (this.txtReg.test(url)) {
            let afterQuestion = url.split('?')[1]
            let paramPairs = afterQuestion.split('&')
            let code = paramPairs[0].split('=')[1]
            console.log(code)
            // temporarily enter index
            // Temp create fake token
            sessionStorage.setItem('token', '123')
            this.$router.push({ name: 'Index', query: { username: 'xxx' } })
        } else {
            this.$router.push({ name: 'Login' })
        }
    }
}
</script>
