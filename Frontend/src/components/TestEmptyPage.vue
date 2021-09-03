<template>
    <div>
        <Button @click="draw">draw</Button>
        <Button @click="resolveOriginData">resolveOriginData</Button>
        <my-props-line-chart
            :initialData="data"
            ref="lineChart"
        ></my-props-line-chart>
    </div>
</template>

<script>
import MyPropsLineChart from '@/components/PropsMultiLineChart'

export default {
    data: function () {
        return {
            data: {
                y: 'xxx',
                series: [{ name: 'n1', values: [2.3, 2.4, 2.5, 2.6, 2.7] }, { name: 'n2', values: [0.6, 2.4, 2.5, 2.6, 2.3] }, { name: 'n3', values: [2.1, 2.3, 2.7, 2.6, 2.1] }],
                dates: [new Date('2000-01-01'), new Date('2000-02-01'), new Date('2000-03-01'), new Date('2000-04-01'), new Date('2000-05-01')]
            },
            originData: [{ 'id': 22827, 'datetime': '2012-03-31T16:20:24.000+00:00', 'radiance': '1426051.8', 'pixels': 1155144, 'cityId': 2, 'window': '[2.997916665, 28.002062535000004, 46.997951865, 54.002083335]' }, { 'id': 22828, 'datetime': '2012-04-01T12:38:03.000+00:00', 'radiance': '6753252.0', 'pixels': 3902261, 'cityId': 2, 'window': '[58.997916665, 29.002062535000004, 102.997951865, 55.002083335]' }, { 'id': 22829, 'datetime': '2012-04-01T12:43:45.000+00:00', 'radiance': '11745323.0', 'pixels': 7574962, 'cityId': 2, 'window': '[55.997916665, 10.002063335000003, 91.997945465, 35.002083335]' }, { 'id': 22830, 'datetime': '2012-04-01T14:20:29.000+00:00', 'radiance': '23600416.0', 'pixels': 11584972, 'cityId': 2, 'window': '[32.997916665, 26.002063335000003, 75.997951065, 51.002083335]' }, { 'id': 22831, 'datetime': '2012-04-01T14:26:10.000+00:00', 'radiance': '10887334.0', 'pixels': 6319400, 'cityId': 2, 'window': '[29.997916665, 7.0020633350000026, 64.997944665, 32.002083335]' }, { 'id': 22832, 'datetime': '2012-04-01T16:02:54.000+00:00', 'radiance': '2648965.8', 'pixels': 3468857, 'cityId': 2, 'window': '[6.997916665, 23.002063335000003, 47.997949465, 48.002083335]' }, { 'id': 22833, 'datetime': '2012-04-02T12:20:33.000+00:00', 'radiance': '12771220.0', 'pixels': 5336758, 'cityId': 2, 'window': '[62.997916665, 24.002063335000003, 103.997949465, 49.002083335]' }]
        }
    },
    methods: {
        resolveOriginData () {
            let dayMap = new Map()
            this.originData.forEach(function (d) {
                let strDay = d.datetime.substr(0, 10)
                if (dayMap.has(strDay)) {
                    dayMap.get(strDay).radiance += +d.radiance
                    dayMap.get(strDay).pixels += +d.pixels
                } else {
                    dayMap.set(strDay, { radiance: +d.radiance, pixels: +d.pixels })
                }
            })
            console.log(dayMap)
            let dayData = {
                y: 'radiance / pixels',
                series: [{ name: 'Middle East', values: [] }],
                dates: []
            }
            dayMap.forEach((value, key) => {
                dayData.dates.push(new Date(key))
                dayData.series[0].values.push(value.radiance / value.pixels)
            })
            console.log(dayData)
            this.$refs.lineChart.resetData(dayData)
        },
        draw () {
            this.$refs.lineChart.draw()
        }
    },
    mounted () {
    },
    components: {
        MyPropsLineChart
    }
}
</script>
