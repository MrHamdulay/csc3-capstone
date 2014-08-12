// Initialize the dashboard chart

Chart.defaults.global.responsive = true;
Chart.defaults.global.maintainAspectRatio = false;

var data = {
    labels: ["Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4"],
    datasets: [{
        label: "Cheaters",
        fillColor: "rgba(220,220,220,0.2)",
        strokeColor: "rgba(220,220,220,1)",
        pointColor: "rgba(220,220,220,1)",
        pointStrokeColor: "#fff",
        pointHighlightFill: "#fff",
        pointHighlightStroke: "rgba(220,220,220,1)",
        data: [3, 6, 7, 2, 4, 9, 2]
    }]
}

var options = {
    bezierCurveTension: 0.2,
    legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
}
var dsh = document.getElementById('overall').getContext('2d')
  , dsh_chart = new Chart(dsh).Line(data, options);

var legend = dsh_chart.generateLegend();
document.getElementById('legend').innerHTML = legend;
