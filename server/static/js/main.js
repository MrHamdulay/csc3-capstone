(function() {

var $flow = $('#flow');
var $diff = $('#diff');
var $graph = $('#graph');
var $cntnr = $('.container');
var $codes = $('#code-block');
var $tbody = $('#groups tbody');
var $code_l = $('#code-left');
var $code_r = $('#code-right');

function set_vertical_layout() {

    var window_h = window.innerHeight;
    var win_margin = get_css_val('margin-top', $cntnr);
    var cntnr_h = window_h - win_margin * 2;
    $cntnr.height(cntnr_h);

    var paddin_b = 20;
    var tblrow_h = 38;
    var graph_h = get_css_val('height', $graph);
    var tbody_h = window_h - win_margin - graph_h - tblrow_h - paddin_b;
    $tbody.height(tbody_h);

    var flow_h = $flow.height();
    $codes.height(flow_h);

    var codes_h = $codes.height();
    var code_header_h = 41;
    var pre_margin_top = get_css_val('padding-top', $code_l);
    var pre_margin_bot = get_css_val('padding-bottom', $code_l);
    var diff_height = codes_h - code_header_h - pre_margin_top - pre_margin_bot;
    $diff.height(diff_height);

}

// returns integer value of css rule on a provided element
// @param rule String
// @param $el jQuery DOM
function get_css_val(rule, $el) {
    return parseInt($el.css(rule).replace('px', ''));
}

function bind_diff_scrolling() {
    $code_l.scroll(function() {
        set_scroll_position($code_l, $code_r);
    });
}

// determines scroll pixel value based on the % of how var
// an element has scrolled relative to its height.
// @param $el_1 jQuery DOM
// @param $el_2 jQuery DOM
function set_scroll_position($from, $to) {
    var from_scrollTop_perc = $from.scrollTop() / ( $from.prop('scrollHeight') - $from.height() );
    var to_scrollTop_px = from_scrollTop_perc * ( $to.prop('scrollHeight') - $to.height() );
    //
    var from_scrollLeft_perc = $from.scrollLeft() / ( $from.prop('scrollWidth') - $from.width() );
    var to_scrollLeft_px = from_scrollLeft_perc * ( $to.prop('scrollWidth') - $to.width() );
    //
    $to.prop('scrollTop', to_scrollTop_px);
    $to.prop('scrollLeft', to_scrollLeft_px);
}


function set_groups_list() {
    d3.json('data/2014_1015_assignment_1_rows.json', function(error, json) {
        var graph = new Graph();
        for (var i = 0; i < json.length; i++) {
            graph.add_edge(json[i].source, {
                target: json[i].target,
                confidence: json[i].tgt_cf,
                line_numbers: [ {source: {start: 10, end: 15}, target: {start: 17, end: 22}} ]
            });
        }

        groups = graph.get_groups();

        var tr = d3.select('#flow table tbody').selectAll('tr')
            .data(groups)
            .enter().append('tr');

        tr.append('td').text(function(d) { return d.length });
        tr.append('td').text(function(d) {
            var source, target;
            var students = '';
            var has_student = {};
            for (var i = 0; i < d.length; i++) {
                source = d[i].source;
                target = d[i].target;
                if (typeof has_student[source] == 'undefined')
                    has_student[source] = true;
                if (typeof has_student[target] == 'undefined')
                    has_student[target] = true;
            }
            for (var key in has_student) {
                students += key + ', ';
            }
            return students;
        });

        tr.on('click', function(d, i) {
            refresh_graph(d);
            d3.select('#flow table tbody').selectAll('tr').classed('selected', false);
            d3.select(this).classed('selected', true);
        });
    });
}


//

function run() {
    set_vertical_layout();
    set_groups_list();
    bind_diff_scrolling();
}

run();








var groups = [];
var links  = groups[0]; // start with the first group
var graph  = d3.select('#graph');
var code_l = d3.select('#code-left');
var code_r = d3.select('#code-right');
var code   = {};

var width = $('#flow').width(),
    height = 250;

var num_students = function(d) {
    return d.length;
}

// first get the groups

var refresh_graph = function(d) {

    var links = d;
    var nodes = {};

    d3.select('#graph').selectAll('*').remove();

    var svg = d3.select("#graph").append("svg")
        .attr("width", width)
        .attr("height", height);

    // Compute the distinct nodes from the links.
    links.forEach(function(link) {
      link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
      link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
    });

    var force = d3.layout.force()
        .nodes(d3.values(nodes))
        .links(links)
        .size([width, height])
        .linkDistance(100)
        .charge(-700)
        .on("tick", tick)
        .start();

    // Per-type markers, as they don't inherit styles.
    svg.append("defs").selectAll("marker")
        .data(["suit", "licensing", "resolved"])
      .enter().append("marker")
        .attr("id", function(d) { return d; })
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", 30)
        .attr("refY", -1.5)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")
      .append("path")
        .attr("d", "M0,-5L10,0L0,5");

    var path = svg.append("g").selectAll("path")
        .data(force.links())
      .enter().append("path")
        .attr("class", function(d) {
            var type = '';
            if (d.confidence >= 85)
                type = 'strong';
            else if (d.confidence >= 50)
                type = 'medium';
            else
                type = 'weak';
            return "link " + type;
        })
        .attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

    var circle = svg.append("g").selectAll("circle")
        .data(force.nodes())
      .enter().append("circle")
        .attr("r", 6)
        .call(force.drag);

    var text = svg.append("g").selectAll("text")
        .data(force.nodes())
      .enter().append("text")
        .attr("x", 10)
        .attr("y", 5)
        .text(function(d) { return d.name; });

    path.on('click', function(d, i) {
        d3.select('h3.a').text(d.source.name);
        d3.select('h3.b').text(d.target.name);
        d3.select('.confidence h3').text(d.confidence + '%');
        populate_code('left', d.source.name);
        populate_code('right', d.target.name);
        set_line_numbers(d.line_numbers);
        Prism.highlightAll();
        set_gutter();
    });

    // Use elliptical arc path segments to doubly-encode directionality.
    function tick() {
      path.attr("d", linkArc);
      circle.attr("transform", transform);
      text.attr("transform", transform);
    }

    function linkArc(d) {
      var dx = d.target.x - d.source.x,
          dy = d.target.y - d.source.y,
          dr = Math.sqrt(dx * dx + dy * dy);
      return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
    }

    function transform(d) {
      return "translate(" + d.x + "," + d.y + ")";
    }
}

var populate_code = function(pos, student) {
    d3.select('pre.code-' + pos + ' code').text(code[student]);
}

var set_line_numbers = function(lines) {
    var code_l = d3.select('pre.code-left');
    var code_r = d3.select('pre.code-right');
    var data_line_l = '';
    var data_line_r = '';
    var start, end;

    for (var i = 0; i < lines.length; i++) {
        // source (left)
        start = lines[i].source.start;
        end = lines[i].source.end;
        if (end - start > 1)
            data_line_l += start + '-' + end + ',';
        else
            data_line_l += start + ',';
        // target (left)
        start = lines[i].target.start;
        end = lines[i].target.end;
        if (end - start > 1)
            data_line_r += start + '-' + end + ',';
        else
            data_line_r += start + ',';
    }

    code_l.attr('data-line', data_line_l);
    code_r.attr('data-line', data_line_r);

    var code_l_w = $('.code-left code').width() + 50;
    var code_r_w = $('.code-right code').width() + 50;
    setTimeout(function() {
        $('.code-left .line-highlight').css('width', code_l_w);
        $('.code-right .line-highlight').css('width', code_r_w);
    }, 10);

}

d3.json('data/2014_1015_assignment_1_code.json', function(error, json) {
    code = json;
});


})();
