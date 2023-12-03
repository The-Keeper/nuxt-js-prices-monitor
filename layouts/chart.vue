<template>
  <highstock :options="chartOpts" />
</template>

<script>
export default {
  data () {
    return {
      series: []
    }
  },
  computed: {
    chartOpts () {
      return {
        rangeSelector: {
          selected: 4
        },


        tooltip: {
          valueDecimals: 2,
          split: true
        },

        series: this.series
      }
    }
  },
  mounted () {
    const symbols = ['BTC']
    symbols.forEach(s => this.fetchData(s))
  },
  methods: {
    async fetchData (symbol) {
      const data = await fetch(`/api/prices`).then(r => r.json())
      this.series.push({
        name: symbol,
        data
      })
    }
  }
}
</script>