import { Bar } from "vue-chartjs";
export default {
  extends: Bar,
  data: () => ({
    chartdata: {
      labels: [...Array(24).keys()].map((e) => `${e}h`),
      datasets: [
        {
          label: "Average BPM",
          backgroundColor: "#f87979",
          data: [],
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  }),

  mounted() {
    this.axios.get("hr/avg").then((res) => {
      this.chartdata.datasets[0].data = Array.from({ length: 24 }, () => 0);
      res.data.forEach((e) => {
        this.chartdata.datasets[0].data[e.fields.hour] = e.fields.avg_bpm;
      });
      this.renderChart(this.chartdata, this.options);
    });
  },
};
