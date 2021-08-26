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
                                        @click="submit"
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
            ]
        }
    },
    methods: {
        submit: function () {
            // Http request here

            // Temp create fake token
            sessionStorage.setItem('token', '123')
            this.$router.push({ name: 'Index' })
        }
    },
    components: {
        MyFooter
    }
}
</script>
