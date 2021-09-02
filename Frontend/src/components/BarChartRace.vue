<template>
    <div class="bar_chart_race"></div>
</template>

<script>
// 引入d3
import * as d3 from 'd3'
export default {
    data () {
        return {
            data: [
                { date: new Date('2000-01-01'), name: 'Coca-Cola', category: 'Beverages', value: 72537 },
                { date: new Date('2000-01-01'), name: 'Microsoft', category: 'Technology', value: 70196 },
                { date: new Date('2000-01-01'), name: 'IBM', category: 'Business Services', value: 53183 },
                { date: new Date('2000-01-01'), name: 'Coca-Cola', category: 'Beverages', value: 68945 },
                { date: new Date('2000-01-01'), name: 'Microsoft', category: 'Technology', value: 70196 },
                { date: new Date('2000-01-01'), name: 'IBM', category: 'Business Services', value: 65068 },
                { date: new Date('2000-01-01'), name: 'Coca-Cola', category: 'Beverages', value: 52790 },
                { date: new Date('2000-01-01'), name: 'Microsoft', category: 'Technology', value: 60193 },
                { date: new Date('2000-01-01'), name: 'IBM', category: 'Business Services', value: 43183 },
                { date: new Date('2000-01-01'), name: 'Coca-Cola', category: 'Beverages', value: 72537 },
                { date: new Date('2000-01-01'), name: 'Microsoft', category: 'Technology', value: 30196 },
                { date: new Date('2000-01-01'), name: 'IBM', category: 'Business Services', value: 33183 },
                { date: new Date('2000-01-01'), name: 'Coca-Cola', category: 'Beverages', value: 72537 },
                { date: new Date('2000-01-01'), name: 'Microsoft', category: 'Technology', value: 50196 },
                { date: new Date('2000-01-01'), name: 'IBM', category: 'Business Services', value: 63183 }
            ],
            width: 800,
            margin: { top: 20, right: 20, bottom: 30, left: 30 },
            n: 8,
            barSize: 48
        }
    },
    methods: {
        draw () {
            /*
            const svg = d3.select('div.bar_chart_race').append('svg')
                .attr('viewBox', [0, 0, this.width, this.height])

            const updateBars = this.bars(svg)
            const updateAxis = axis(svg)
            const updateLabels = labels(svg)
            const updateTicker = ticker(svg)

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
            */
        },
        bars (svg) {
            /*
            let bar = svg.append('g')
                .attr('fill-opacity', 0.6)
                .selectAll('rect')

            return function (transition) {
                bar = bar
                    .data(this.data.slice(0, this.n), d => d.name)
                    .join(
                        enter => enter.append('rect')
                            .attr('fill', this.colorScale)
                            .attr('height', this.scaleY.bandwidth())
                            .attr('x', this.scaleX(0))
                            .attr('y', d => this.scaleY((prev.get(d) || d).rank))
                            .attr('width', d => this.scaleX((prev.get(d) || d).value) - x(0)),
                        update => update,
                        exit => exit.transition(transition).remove()
                            .attr('y', d => this.scaleY((next.get(d) || d).rank))
                            .attr('width', d => this.scaleX((next.get(d) || d).value) - x(0))
                    )
                    .call(bar => bar.transition(transition)
                        .attr('y', d => this.scaleY(d.rank))
                        .attr('width', d => this.scaleX(d.value) - this.scaleX(0)))
            }
            */
        },
        computed: {
            height: function () {
                return this.margin.top + this.barSize * this.n + this.margin.bottom
            },
            scaleX () {
                return d3.scaleLinear([0, 1], [this.margin.left, this.width - this.margin.right])
            },
            scaleY () {
                return d3.scaleBand()
                    .domain(d3.range(this.n + 1))
                    .rangeRound([this.margin.top, this.margin.top + this.barSize * (this.n + 1 + 0.1)])
                    .padding(0.1)
            },
            scaleColor () {
                const scale = d3.scaleOrdinal(d3.schemeTableau10)
                if (this.data.some(d => d.category !== undefined)) {
                    const categoryByName = new Map(this.data.map(d => [d.name, d.category]))
                    scale.domain(categoryByName.values())
                    return d => scale(categoryByName.get(d.name))
                } else {
                    return d => scale(d.name)
                }
            }
        },
        mounted () {
            this.draw()
        }
    }
}
</script>
