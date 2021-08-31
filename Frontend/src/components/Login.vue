<template>
    <div data-smooth-scroll-offset="77">
        <div class="nav-container"></div>
        <div class="main-container">
            <section class="height-100 text-center">
                <div class="container pos-vertical-center">
                    <div class="row">
                        <div class="col-md-7 col-lg-5">
                            <h2>Sign in with</h2>

                            <ul>
                                <li
                                    v-for="way in signInWays"
                                    v-bind:key="way.id"
                                >
                                    <input
                                        class="btn btn--primary type--uppercase"
                                        type="button"
                                        @click="submit(way.id)"
                                        v-bind:value="way.label"
                                    />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
            <my-footer />
        </div>
    </div>
</template>

<script>
import MyFooter from '@/components/Footer'

export default {
    data: function () {
        return {
            signInWays: [
                { id: 0, label: 'Github' }
            ],
            wayDetails: [
                {
                    client_id: '42a45d2fefb71837398e',
                    scope: 'read:user',
                    state: 'A2Inc', // An unguessable random string. It is used to protect against cross-site request forgery attacks.
                    getCodeURL: 'https://github.com/login/oauth/authorize',
                    redirectURL: 'http://localhost:8888/oauth/redirect'
                }
            ]
        }
    },
    methods: {
        submit: function (index) {
            // check if log in

            // if not
            if (index === 0) {
                // console.info(this.formatGitHubCodeURL)
                // window.open(this.formatGitHubCodeURL)
                window.location.href = this.formatGitHubCodeURL
            }
            /*
            this.$http.jsonp(
                'github/login/oauth/authorize',
                {
                    'params': this.wayDetails[index]
                })
                .then((response) => {
                    console.info(response.body)
                }, (response) => {
                    console.error(response)
                })
*/
            // Temp create fake token
            // sessionStorage.setItem('token', '123')
            // this.$router.push({ name: 'Index' })
        }
    },
    computed: {
        formatGitHubCodeURL: function () {
            let detail = this.wayDetails[0]
            return detail.getCodeURL + ('?' + this.$querystring.stringify({
                client_id: detail.client_id,
                scope: detail.scope,
                state: detail.state,
                redirect_uri: detail.redirectURL
            }))
        }
    },
    components: {
        MyFooter
    }
}
</script>
