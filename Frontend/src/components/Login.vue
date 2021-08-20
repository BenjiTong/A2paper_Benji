<template>
    <div class="row lyear-wrapper">
        <div class="lyear-login">
            <div class="login-center">
                <div class="form-group has-feedback feedback-left">
                    <input
                        type="text"
                        placeholder="Your email"
                        v-model="email"
                    />
                    <span
                        class="mdi mdi-account form-control-feedback"
                        aria-hidden="true"
                    ></span>
                </div>
                <div class="form-group has-feedback feedback-left">
                    <input
                        type="password"
                        placeholder="Password"
                        v-model="password"
                    />
                    <span
                        class="mdi mdi-lock form-control-feedback"
                        aria-hidden="true"
                    ></span>
                </div>
                <div class="form-group">
                    <input
                        class="btn btn-block btn-primary"
                        type="button"
                        @click="submit"
                        value="Login"
                    />
                </div>
                <hr />
                <footer class="col-sm-12 text-center">
                    <p class="m-b-0">{{ copyright }}</p>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            email: '',
            password: '',
            copyright: 'Copyright © 2021 A2Inc. All right reserved'
        }
    },
    methods: {
        submit: function () {
            // Http request here
        }
    }
}
</script>

<style scoped>
.lyear-wrapper {
    position: relative;
}
.lyear-login {
    display: flex !important;
    min-height: 100vh;
    align-items: center !important;
    justify-content: center !important;
}
.login-center {
    /* background: #fff; */
    background: rgba(255, 255, 255, 0.5);
    min-width: 38.25rem;
    padding: 2.14286em 3.57143em;
    border-radius: 5px;
    margin: 2.85714em 0;
}
.login-header {
    margin-bottom: 1.5rem !important;
}
.login-center .has-feedback.feedback-left .form-control {
    padding-left: 38px;
    padding-right: 12px;
}
.login-center .has-feedback.feedback-left .form-control-feedback {
    left: 0;
    right: auto;
    width: 38px;
    height: 38px;
    line-height: 38px;
    z-index: 4;
    color: #dcdcdc;
}
.login-center .has-feedback.feedback-left.row .form-control-feedback {
    left: 15px;
}
</style>
