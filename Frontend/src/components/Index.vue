<template>
    <div>
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
        <section>
            <div class="container">
                <div
                    class="
                        masonry-filter-container
                        text-center
                        row
                        justify-content-start
                        align-items-center
                    "
                >
                    <select
                        class="col-2 my-dropdown-menu"
                        v-model="selectedArea"
                    >
                        <option
                            v-for="option in options"
                            v-bind:value="option.value"
                            v-bind:key="option.value"
                        >
                            {{ option.text }}
                        </option>
                    </select>
                    <div class="my-checkbox">
                        <input
                            type="radio"
                            id="year"
                            value="0"
                            v-model="pickedMode"
                            class="col-1"
                        />
                        <label for="year">Year</label>
                        <input
                            type="radio"
                            id="month"
                            value="1"
                            v-model="pickedMode"
                            class="col-1"
                        />
                        <label for="month">Month</label>
                        <input
                            type="radio"
                            id="day"
                            value="2"
                            v-model="pickedMode"
                            class="col-1"
                        />
                        <label for="day">Day</label>
                    </div>
                </div>
                <div class="masonry__container row masonry--active">
                    <div class="masonry__item col-md-6 col-12 filter-filter-1">
                        <my-props-line-chart
                            ref="lineChart"
                        ></my-props-line-chart>
                        <span class="h4 inline-block">Title</span>
                        <span>Detailed Description</span>
                    </div>
                </div>
            </div>
        </section>
        <my-footer></my-footer>
    </div>
</template>

<script>
import MyFooter from '@/components/Footer'
import MyPropsLineChart from '@/components/PropsMultiLineChart'

export default {
    data: function () {
        return {
            data: [{}, {}, {}],
            /*
            [
                {
                    lineChart: [
                        dayData: null,
                        monthData: null,
                        yearData: null
                    ]
                },
                {
                    lineChart: [
                        dayData: null,
                        monthData: null,
                        yearData: null
                    ]
                },
                {
                    lineChart: [
                        dayData: null,
                        monthData: null,
                        yearData: null
                    ]
                }
            ], */
            isSideMenuShowing: false,
            username: 'username',
            selectedArea: 2,
            pickedMode: -1,
            options: [
                { text: 'China', value: 0 },
                { text: 'New Zealand', value: 1 },
                { text: 'Middle East', value: 2 }
            ]
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
        },
        resolveOriginData (index, originData) {
            if (this.data[index].lineChart != null) return
            let dayMap = new Map()
            let monthMap = new Map()
            let yearMap = new Map()
            originData.forEach(function (d) {
                let strDay = d.datetime.substr(0, 10)
                let strMonth = strDay.substr(0, 8) + '01'
                let strYear = strMonth.substr(0, 5) + '01-01'
                if (dayMap.has(strDay)) {
                    dayMap.get(strDay).radiance += +d.radiance
                    dayMap.get(strDay).pixels += +d.pixels
                } else {
                    dayMap.set(strDay, { radiance: +d.radiance, pixels: +d.pixels })
                }
                if (monthMap.has(strMonth)) {
                    monthMap.get(strMonth).radiance += +d.radiance
                    monthMap.get(strMonth).pixels += +d.pixels
                } else {
                    monthMap.set(strMonth, { radiance: +d.radiance, pixels: +d.pixels })
                }
                if (yearMap.has(strYear)) {
                    yearMap.get(strYear).radiance += +d.radiance
                    yearMap.get(strYear).pixels += +d.pixels
                } else {
                    yearMap.set(strYear, { radiance: +d.radiance, pixels: +d.pixels })
                }
            })
            console.log(monthMap)
            console.log(yearMap)
            let dayData = {
                y: 'radiance / pixels',
                series: [{ name: this.options[index].text, values: [] }],
                dates: []
            }
            let monthData = {
                y: 'radiance / pixels',
                series: [{ name: this.options[index].text, values: [] }],
                dates: []
            }
            let yearData = {
                y: 'radiance / pixels',
                series: [{ name: this.options[index].text, values: [] }],
                dates: []
            }
            dayMap.forEach((value, key) => {
                dayData.dates.push(new Date(key))
                dayData.series[0].values.push(value.radiance / value.pixels)
            })
            monthMap.forEach((value, key) => {
                monthData.dates.push(new Date(key))
                monthData.series[0].values.push(value.radiance / value.pixels)
            })
            yearMap.forEach((value, key) => {
                yearData.dates.push(new Date(key))
                yearData.series[0].values.push(value.radiance / value.pixels)
            })
            this.data[index].lineChart = [yearData, monthData, dayData]
            console.log(this.data[index])
            if (this.selectedArea === index) {
                this.resetData(this.selectedArea)
            }
        },
        resetData () {
            if (this.pickedMode >= 0 && this.data[this.selectedArea].lineChart != null) {
                this.$refs.lineChart.resetData(this.data[this.selectedArea].lineChart[this.pickedMode])
            }
        }
    },
    watch: {
        selectedArea: function (val) {
            console.log('selectedArea ' + val)
            this.resetData()
        },
        pickedMode: function (val) {
            console.log('pickedMode ' + val)
            this.resetData()
        }
    },
    mounted () {
        this.$http.get('/api/city?id=2').then((response) => {
            // console.info(response.body)
            this.resolveOriginData(2, response.body)
        }, (response) => {
            console.error(response)
        })
    },
    components: {
        MyFooter,
        MyPropsLineChart
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

.my-dropdown-menu {
    display: inline-block;
    cursor: pointer;
    position: relative;
    z-index: 9;
}

.my-checkbox {
    padding-left: 1%;
}
</style>
