<template>
    <div class="line_chart"></div>
</template>

<script>
// 引入d3
import * as d3 from 'd3'
export default {
    data () {
        return {
            data: {
                y: 'xxx',
                series: [{ name: 'n1', values: [2.3, 2.4, 2.5, 2.6, 2.7] }, { name: 'n2', values: [0.6, 2.4, 2.5, 2.6, 2.3] }, { name: 'n3', values: [2.1, 2.3, 2.7, 2.6, 2.1] }],
                dates: [new Date('2000-01-01'), new Date('2000-02-01'), new Date('2000-03-01'), new Date('2000-04-01'), new Date('2000-05-01')]
            },
            width: 600,
            height: 400,
            margin: { top: 20, right: 20, bottom: 30, left: 30 }
        }
    },
    methods: {
        draw () {
            const svg = d3.select('div.line_chart').append('svg')
                .attr('viewBox', [0, 0, this.width, this.height])
                .style('overflow', 'visible')

            // 定义 X 轴比例尺
            let scaleX = d3.scaleUtc()
                .domain(d3.extent(this.data.dates))
                .range([this.margin.left, this.width - this.margin.right])

            // 定义 y 轴比例尺
            let scaleY = d3.scaleLinear()
                .domain([0, d3.max(this.data.series, d => d3.max(d.values))]).nice()
                .range([this.height - this.margin.bottom, this.margin.top])

            let line = d3.line()
                .defined(d => !isNaN(d))
                .x((d, i) => scaleX(this.data.dates[i]))
                .y(d => scaleY(d))

            // 绘制 x y 轴
            let xAxis = g => g
                .attr('transform', `translate(0,${this.height - this.margin.bottom})`)
                .call(d3.axisBottom(scaleX).ticks(this.width / 80).tickSizeOuter(0))
            let yAxis = g => g
                .attr('transform', `translate(${this.margin.left},0)`)
                .call(d3.axisLeft(scaleY))
                .call(g => g.select('.domain').remove())
                .call(g => g.select('.tick:last-of-type text').clone()
                    .attr('x', 3)
                    .attr('text-anchor', 'start')
                    .attr('font-weight', 'bold')
                    .text(this.data.y))
            svg.append('g').append('g')
                .call(xAxis)
            svg.append('g').append('g')
                .call(yAxis)

            const path = svg.append('g')
                .attr('fill', 'none')
                .attr('stroke', 'steelblue')
                .attr('stroke-width', 1.5)
                .attr('stroke-linejoin', 'round')
                .attr('stroke-linecap', 'round')
                .selectAll('path')
                .data(this.data.series)
                .join('path')
                .style('mix-blend-mode', 'multiply')
                .attr('d', d => line(d.values))

            this.hover(svg, path, scaleX, scaleY)
        },
        hover (svg, path, scaleX, scaleY) {
            let that = this
            if ('ontouchstart' in document) {
                svg
                    .style('-webkit-tap-highlight-color', 'transparent')
                    .on('touchmove', moved)
                    .on('touchstart', entered)
                    .on('touchend', left)
            } else {
                svg
                    .on('mousemove', moved)
                    .on('mouseenter', entered)
                    .on('mouseleave', left)
            }

            const dot = svg.append('g')
                .attr('display', 'none')

            dot.append('circle')
                .attr('r', 2.5)

            dot.append('text')
                .attr('font-family', 'sans-serif')
                .attr('font-size', 10)
                .attr('text-anchor', 'middle')
                .attr('y', -8)

            function moved (event) {
                event.preventDefault()
                const pointer = d3.pointer(event, this)
                const xm = scaleX.invert(pointer[0])
                const ym = scaleY.invert(pointer[1])
                const i = d3.bisectCenter(that.data.dates, xm)
                const s = d3.least(that.data.series, d => Math.abs(d.values[i] - ym))
                path.attr('stroke', d => d === s ? null : '#ddd').filter(d => d === s).raise()
                dot.attr('transform', `translate(${scaleX(that.data.dates[i])},${scaleY(s.values[i])})`)
                dot.select('text').text(s.name)
            }

            function entered () {
                path.style('mix-blend-mode', null).attr('stroke', '#ddd')
                dot.attr('display', null)
            }

            function left () {
                path.style('mix-blend-mode', 'multiply').attr('stroke', null)
                dot.attr('display', 'none')
            }
        }
    },
    mounted () {
        this.draw()
    }
}
</script>
