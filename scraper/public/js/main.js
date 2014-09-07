$.get('data/2014_1015_plagiarism_reports.json')
 .done(function(json) {

    var ctx = document.getElementById("duplicate_lines_per_assignment").getContext("2d");
    //
    var contexts = [
        document.getElementById("confidence_1").getContext("2d"),
        document.getElementById("confidence_2").getContext("2d"),
        document.getElementById("confidence_3").getContext("2d"),
        document.getElementById("confidence_4").getContext("2d"),
        document.getElementById("confidence_5").getContext("2d"),
        document.getElementById("confidence_6").getContext("2d"),
        document.getElementById("confidence_7").getContext("2d"),
        document.getElementById("confidence_8").getContext("2d"),
        document.getElementById("confidence_9").getContext("2d")
    ];
    //
    var options = {
        scaleBeginAtZero : true,
        scaleShowGridLines : true,
        scaleGridLineColor : "rgba(0,0,0,.05)",
        scaleGridLineWidth : 1,
        barShowStroke : true,
        barStrokeWidth : 2,
        barValueSpacing : 5,
        barDatasetSpacing : 1,
        legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
    }
    //
    var assignments = get_assignments(json);
    var copied_lines = get_copied_lines(json);
    var labels = get_assignments(json);
    //
    var copied_lines_data = {
        labels: labels,
        datasets: [{
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: copied_lines
        }]
    }

    var conf_labels = new Array(100);
    var conf_data_1 = new Array(100)
      , conf_data_2 = new Array(100)
      , conf_data_3 = new Array(100)
      , conf_data_4 = new Array(100)
      , conf_data_5 = new Array(100)
      , conf_data_6 = new Array(100)
      , conf_data_7 = new Array(100)
      , conf_data_8 = new Array(100)
      , conf_data_9 = new Array(100);
    var conf_datas  = [];
    for (var i = 0; i < contexts.length; i++) {
        conf_datas.push([]);
    }
    for (var i = 0; i < conf_labels.length; i++) {
        conf_labels[i] = i + 1;
        for (var j = 0; j < 9; j++) {
            conf_datas[j][i] = 0;
        }
    }

    var i = 0;
    for (var key in json) {
        count_occurrences_of_confidence(json, key, conf_datas[i++]);
    }

    function get_graph_data(data) {
        return {
            labels: conf_labels,
            datasets: [
                {
                    label: "My First dataset",
                    fillColor: "rgba(220,220,220,0.2)",
                    strokeColor: "rgba(220,220,220,1)",
                    pointColor: "rgba(220,220,220,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(220,220,220,1)",
                    data: data
                }
            ]
        }
    }
    //
    for (var i = 0; i < conf_datas.length; i++) {
        var data = get_graph_data(conf_datas[i]);
        new Chart(contexts[i]).Line(data, options);
    }
    //
    new Chart(ctx).Bar(copied_lines_data, options);

 });

function get_assignments(json) {
    var assignments = [];
    for (var key in json) {
        assignments.push(key);
    }
    return assignments
}

function get_copied_lines (json) {
    var copied_lines = [];
    for (var key in json) {
        var total = 0;
        var student, lines;
        var assignment = json[key];
        for (var key in assignment) {
            total += get_lines_by_student(assignment[key]);
        }
        copied_lines.push(total / 2);
    }
    return copied_lines;
}

function count_occurrences_of_confidence(json, assignment, data) {
    var assignment = json[assignment];
    var total;
    for (var key in assignment) {
        data[assignment[key].confidence]++;
    }
}

function get_lines_by_student(student) {
    var total = 0;
    lines = student.matched_lines;
    for (var i = 0; i < lines.length; i++) {
        total += lines[i][1] - lines[i][0];
    }
    return total;
}
