<template>
    <div data-smooth-scroll-offset="77">
        <div class="nav-container">
            <div>
                <nav class="bar bar-toggle">
                    <div class="container">
                        <div class="row align-items-center">
                            <div class="col-6">
                                <div class="bar__module">
                                    <router-link :to="{ name: 'Index' }">
                                        <img
                                            class="logo logo-dark"
                                            alt="logo"
                                            src="img/logo-dark.png"
                                        />
                                        <img
                                            class="logo logo-light"
                                            alt="logo"
                                            src="img/logo-light.png"
                                        />
                                    </router-link>
                                </div>
                            </div>
                            <div class="col-6 d-flex justify-content-end">
                                <div class="bar__module">
                                    <div
                                        class="menu-toggle pull-right"
                                        @click="showSideMenu(true)"
                                    >
                                        <i
                                            class="stack-interface stack-menu"
                                        ></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>
                <div
                    class="mask"
                    v-show="isSideMenuShowing"
                    @click.self.stop="showSideMenu(false)"
                ></div>
                <transition name="from-right">
                    <div
                        class="
                            notification
                            pos-right pos-top
                            side-menu
                            bg--white
                        "
                        v-if="isSideMenuShowing"
                        v-on:click.stop="clickWrapper($event)"
                    >
                        <div
                            class="
                                side-menu__module
                                pos-vertical-center
                                text-right
                            "
                        >
                            <ul class="menu-vertical">
                                <li class="h4">{{ username }}</li>
                                <li>
                                    <input
                                        type="button"
                                        class="btn"
                                        @click="signout"
                                        value="Signout"
                                    />
                                </li>
                            </ul>
                        </div>
                    </div>
                </transition>
            </div>
        </div>
        <div class="main-container">
            <section>
                <div class="container">
                    <div class="masonry">
                        <div
                            class="
                                masonry-filter-container
                                text-center
                                row
                                justify-content-center
                                align-items-center
                            "
                        >
                            <span>City: </span>
                            <div class="masonry-filter-holder">
                                <div
                                    class="masonry__filters"
                                    data-filter-all-text="All Categories"
                                >
                                    <ul>
                                        <li
                                            class="active"
                                            data-masonry-filter="*"
                                        >
                                            All Categories
                                        </li>
                                        <li data-masonry-filter="filter-1">
                                            Filter 1
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="masonry__container row masonry--active">
                            <div
                                class="
                                    masonry__item
                                    col-md-6 col-12
                                    filter-filter-1
                                "
                            >
                                <my-line-chart></my-line-chart>
                                <span class="h4 inline-block">Video Title</span>
                                <span>Detailed Description</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <my-footer></my-footer>
        </div>
    </div>
</template>

<script>
import MyFooter from '@/components/Footer'
import MyLineChart from '@/components/MultiLineChart'

export default {
    data: function () {
        return {
            isSideMenuShowing: false,
            username: 'username'
        }
    },
    methods: {
        showSideMenu (flag) {
            this.isSideMenuShowing = flag
        },
        clickWrapper (event) {
            event.stopPropagation()
        },
        signout () {
            // signout logic
            // send message to server
            sessionStorage.removeItem('token')
            this.$router.push({ name: 'Login' })
        }
    },
    components: {
        MyFooter,
        MyLineChart
    }
}
</script>

<style scoped>
.from-right-enter-active {
    animation: from-right 0.3s linear 0s forwards;
}
.from-right-leave-active {
    animation: from-right 0.3s linear 0s reverse;
}
@keyframes from-right {
    from {
        transform: translate3d(100%, 0, 0);
        -webkit-transform: translate3d(100%, 0, 0);
        opacity: 1;
    }
    to {
        transform: translate3d(0, 0, 0);
        -webkit-transform: translate3d(0, 0, 0);
        opacity: 1;
    }
}

.mask {
    position: fixed;
    width: 100%;
    left: 0;
    top: 0;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 10;
    transition: all 0.2s ease-in;
}
</style>
