(function() {

// selectors for indexing DOM elements

var container_selector    = '.container',
    navbar_selector       = container_selector  + ' > nav.navbar',
    navtabs_selector      = container_selector  + ' ul.nav-tabs',
    row_selector          = container_selector  + ' > .row',
    navtabs_li_selector   = navtabs_selector    + ' li',
    navtabs_li_a_selector = navtabs_li_selector + ' a';

var subgroups_selector    = '#subgroups',
    pairs_selector        = '#pairs',
    groups_selector       = '#groups',
    code_selector         = '#code',
    pairs_tbody_selector  = pairs_selector + ' .scrollable table tbody',
    pairs_panel_selector  = pairs_selector + ' .panel',
    pairs_diagram_selector = pairs_selector + ' .diagram',
    groups_table_selector = groups_selector + ' .scrollable table',
    groups_panel_selector = groups_selector + ' .panel',
    groups_diagram_selector = groups_selector + ' .diagram';

var code_selector = '#code',
    action_bar_selector = '.action-bar',
    action_bar_back_selector = action_bar_selector + ' .back',
    shared_lines_selector = '#shared-lines',
    code_panel_heading_selector = code_selector + ' .panel-heading',
    code_panel_body_selector = code_selector + ' .panel-body',
    student_A_id_selector    = code_selector + ' .A .id',
    student_A_lines_selector = code_selector + ' .A .lines',
    student_A_pre_selector  = code_selector + ' .A pre',
    student_A_code_selector  = code_selector + ' .A code',
    student_B_id_selector    = code_selector + ' .B .id',
    student_B_lines_selector = code_selector + ' .B .lines',
    student_B_pre_selector  = code_selector + ' .B pre',
    student_B_code_selector  = code_selector + ' .B code';

var code = {},
    confidence_values = [];

// initialization methods

var initialize_data = function(callback) {

    return new Promise(function(fulfill, reject) {
        d3.json(get_api_url('pairs'), function(error, json) {

            if (error) reject(error);

            // remove comparisons to self
            json.matches = $.grep(json.matches, function(m) {
                return m.source != m.target
            });

            // create graph for groups,
            // create confidence list for histogram
            var graph = new Graph(),
                histogram = [];
            for (var i = 0; i < json.matches.length; i++) {
                // graph
                graph.add_edge(json.matches[i].source, {
                    source_id: json.matches[i].source_id,
                    target_id: json.matches[i].target_id,
                    target: json.matches[i].target,
                    confidence: json.matches[i].confidence,
                    line_numbers: [ {source: {start: 10, end: 15}, target: {start: 17, end: 22}} ]
                });
                // histogram
                histogram.push(json.matches[i].confidence / 10);
                histogram.push(json.matches[i].confidence / 10);
            }
            groups = graph.get_groups();

            fulfill({
                pairs: json.matches,
                groups: graph.get_groups(),
                histogram: histogram
            });

        });

    });

}

var fetch_code = function() {
    return new Promise(function(fulfill, reject) {
        d3.json(get_api_url('code'), function(error, json) {
            if (error) reject(error);
            fulfill(json);
        });
    });
}

var set_line_numbers = function(lines) {
    var pre_A = d3.select(student_A_pre_selector),
        pre_B = d3.select(student_B_pre_selector);

    var data_line_l = lines.source,
        data_line_r = lines.target,
        start, end;

    pre_A.attr('data-line', lines.source);
    pre_B.attr('data-line', lines.target);

    var code_A_w = $(student_A_code_selector).width() + 50,
        code_B_w = $(student_B_code_selector).width() + 50;

    setTimeout(function() {
        $(student_A_pre_selector + ' .line-highlight').css('width', code_A_w);
        $(student_B_pre_selector + ' .line-highlight').css('width', code_B_w);
    }, 1);

}

var mirror_code_scrolling = function() {
    var $pre_A = $(student_A_pre_selector),
        $pre_B = $(student_B_pre_selector);

    $pre_A.scroll(function() {
        var from_scrollTop_perc = $pre_A.scrollTop() / ( $pre_A.prop('scrollHeight') - $pre_A.height() ),
            to_scrollTop_px = from_scrollTop_perc * ( $pre_B.prop('scrollHeight') - $pre_B.height() );

        var from_scrollLeft_perc = $pre_A.scrollLeft() / ( $pre_A.prop('scrollWidth') - $pre_A.width() ),
            to_scrollLeft_px = from_scrollLeft_perc * ( $pre_B.prop('scrollWidth') - $pre_B.width() );

        $pre_B.prop('scrollTop', to_scrollTop_px);
        $pre_B.prop('scrollLeft', to_scrollLeft_px);
    });
}

var set_group_row = function(tr) {
    tr.append('td').text(function(d, i) { return i + 1 });
    tr.append('td').text(function(d, i) { return d.source });
    tr.append('td').text(function(d, i) { return d.target });
    tr.append('td').text(function(d, i) { return d.confidence });
    tr.append('td').text(function(d, i) { return d.confidence });
    tr.append('td').text(function(d, i) { return d.confidence });
}

var draw_graph_diagram = function(d) {

    var links = d,
        nodes = {};

    var width = $(groups_diagram_selector).width(),
        height = $(groups_diagram_selector).innerHeight();

    if (!$(groups_diagram_selector).hasClass('rendered')) {
        $(groups_diagram_selector).addClass('rendered');
    }

    d3.select(groups_diagram_selector).selectAll('*').remove();

    var svg = d3.select(groups_diagram_selector).append("svg")
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
        .linkDistance(150)
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
        .attr("r", 10)
        .call(force.drag);

    var text = svg.append("g").selectAll("text")
        .data(force.nodes())
      .enter().append("text")
        .attr("x", 10)
        .attr("y", 5)
        .text(function(d) { return d.name; });

    path.on('click', function(d) {
        populate_code_view({
            source: d.source.name,
            target: d.target.name,
            source_id: d.source_id,
            target_id: d.target_id,
            confidence: d.confidence
        });
        toggle_view('code');
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

var draw_histogram_diagram = function(values) {

    // A formatter for counts.
    var formatCount = d3.format(",.0f");

    var margin = {top: 15, right: 30, bottom: 30, left: 30},
        width = $(pairs_diagram_selector).width() - margin.left - margin.right,
        height = $(pairs_diagram_selector).innerHeight() - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .domain([0, 100])
        .range([0, width]);

    // Generate a histogram using twenty uniformly-spaced bins.
    var data = d3.layout.histogram()
        .bins(x.ticks(20))
        (values);

    var y = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d.y; })])
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var svg = d3.select(pairs_diagram_selector).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var bar = svg.selectAll(".bar")
        .data(data)
      .enter().append("g")
        .attr("class", "bar")
        .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

    bar.append("rect")
        .attr("x", 1)
        .attr("width", x(data[0].dx) - 1)
        .attr("height", function(d) { return height - y(d.y); });

    bar.append("text")
        .attr("dy", ".75em")
        .attr("y", 6)
        .attr("x", x(data[0].dx) / 2)
        .attr("text-anchor", "middle")
        .text(function(d) { return formatCount(d.y); });

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
}

var set_pairs_table = function(pairs) {
    var tr = d3.select(pairs_tbody_selector).selectAll('tr')
        .data(pairs)
        .enter().append('tr')

    set_group_row(tr);
    tr.on('click', function(d) {
        $(subgroups_selector + ' tr.selected').removeClass('selected');
        $(this).addClass('selected');
        populate_code_view(d);
        toggle_view('code');
    });
}

var set_groups_table = function(list) {

    var tbody = d3.select(groups_table_selector).selectAll('tbody')
        .data(list)
        .enter()
        .append('tbody');

    tbody.on('click', function(d) {
        $(subgroups_selector + ' tr.selected').removeClass('selected');
        $(this).find('tr').addClass('selected');
        draw_graph_diagram(d);
    });

    var tr = tbody.selectAll('tr')
        .data(function(d) { return d })
        .enter()
        .append('tr');

    set_group_row(tr);

    $(groups_table_selector + ' tbody').each(function(i, tbody) {
        var len = $(tbody).children().length;
        $(tbody).find('tr:first-child td:first-child').each(function(i, td) {
            $(td).text(len);
        });
        $(tbody).find('tr:not(:first-child) td:first-child').each(function(i, td) {
            $(td).text('');
        });
    });

}

var set_action_line_buttons = function(lines) {

    var ranges = lines.split(','),
        line_height = parseFloat($(student_A_pre_selector).css('line-height'));

    for (var i = 0, range; range = ranges[i++];) {
        var $button = $('<button type="button" class="btn btn-default"><span class="glyphicon glyphicon-align-justify"></span></button>'),
            text = range;
        range = range.split('-');
        var start = +range[0],
            top = (start - 1) * line_height;
        $button.attr('data-top', top);
        $button.append(text);
        $(shared_lines_selector).append($button);
    }

    $(shared_lines_selector + ' .btn').on('click', function(e) {
        e.preventDefault();
        var scroll_top = parseFloat($(e.target).data('top'));
        $(student_A_pre_selector).scrollTop(scroll_top);
    });
}

var populate_code_view = function(d) {

    // clean view
    $('.line-highlight').remove();
    $(shared_lines_selector).empty();

    if (!$(code_panel_body_selector).hasClass('rendered'))
        $(code_panel_body_selector).addClass('rendered');

    if (!$(code_panel_body_selector).hasClass('fetching'))
        $(code_panel_body_selector).addClass('fetching');

    // set Student A and Student B
    d3.select(student_A_id_selector).text(d.source);
    d3.select(student_B_id_selector).text(d.target);
    d3.select(student_A_lines_selector).text(parseInt(d.confidence) + '%');
    d3.select(student_B_lines_selector).text(parseInt(d.confidence) + '%');

    // set code
    d3.select(student_A_code_selector).text(code[d.source]);
    d3.select(student_B_code_selector).text(code[d.target]);

    retrieve_matches(d.source_id).then(function(json) {

        $(code_panel_body_selector).removeClass('fetching');

        // enhance code view
        set_line_numbers(json);
        Prism.highlightAll();

        // line number buttons
        set_action_line_buttons(json.source);

    });

}

var retrieve_matches = function(id) {
    return new Promise(function(fulfill, reject) {
        d3.json(get_api_url('lines', id), function(error, json) {
            if (error) reject(error);
            fulfill(json);
        });
    });
}

var get_api_url = function(key, id) {
    var url = '/api/' + assignment_number;
    switch (key) {
        case 'code':
            url += '/code';
            break;
        case 'pairs':
            url += '/matches';
            break;
        case 'lines':
            url += '/' + id;
            break;
    }
    return url;
}

var set_vertical_layout = function() {

    // .container height

    var window_h = window.innerHeight,
        container_top = get_css_val('margin-top', container_selector),
        container_h = window_h - (container_top * 2);

    $(container_selector).height(container_h);

    // #subgroups height

    var navbar_h = $(navbar_selector).innerHeight(),
        navbar_bot = get_css_val('margin-bottom', navbar_selector),
        navtabs_h = $(navtabs_selector).innerHeight() + get_css_val('margin-bottom', navtabs_selector),
        subgroups_h = container_h - navbar_h - navbar_bot - navtabs_h;

    $(subgroups_selector).height(subgroups_h);

    // #pairs .panel and #groups .panel height

    var panel_h = subgroups_h - get_css_val('margin-top', pairs_panel_selector),
        panel_header_h = $(pairs_panel_selector + ' .panel-heading').innerHeight() + 10; // border height is 2
        panel_body_h = panel_h - panel_header_h;

    $(pairs_panel_selector + ' .panel-body').height(panel_body_h);
    $(groups_panel_selector + ' .panel-body').height(panel_body_h);
    $(pairs_panel_selector + ' .scrollable').height(panel_body_h - 37);
    $(groups_panel_selector + ' .scrollable').height(panel_body_h - 37);

    // code panel height

    var actionbar_h = $(action_bar_selector).innerHeight(),
        actionbar_top = get_css_val('margin-top', action_bar_selector),
        code_panel_heading_h = $(code_panel_heading_selector).innerHeight() + 10, // 3px in borders
        code_panel_body_h = subgroups_h - actionbar_h - actionbar_top*2 - code_panel_heading_h;

    $(code_panel_body_selector).height(code_panel_body_h);

}


var get_css_val = function(rule, selector) {
    return parseInt($(selector).css(rule).replace('px', ''));
}

var toggle_view = function(name) {
    var back = $(navtabs_li_selector + '.active').data('view');
    $(navtabs_li_selector).removeClass('active');
    var $li = $(navtabs_li_selector + '[data-view="' + name + '"]').closest('li');
    $li.addClass('active');
    $(subgroups_selector + ' > div.active').removeClass('active');
    switch(name) {
        case 'pairs':
            $(pairs_selector).addClass('active');
            break;
        case 'groups':
            $(groups_selector).addClass('active');
            break;
        case 'code':
            $(action_bar_back_selector).data('view', back)
            $(code_selector).addClass('active');
            break;
    }
}

var run = function() {

    initialize_data().then(function(json) {
        set_pairs_table(json.pairs);
        draw_histogram_diagram(json.histogram);
        set_groups_table(json.groups);
        $(subgroups_selector).removeClass('initializing');
    });

    $(action_bar_back_selector).on('click', function(e) {
        e.preventDefault();
        var view = $(e.target).data('view');
        toggle_view(view);
    })

    $(navtabs_li_a_selector).on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var view = $(e.target).closest('li').data('view');
        toggle_view(view);
    });

    set_vertical_layout();
    mirror_code_scrolling();

    fetch_code().then(function(json) {
        code = json;
    });

}

run();

var easing, e, pos;
$(function(){
  // Get the click event
});

/*


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
    d3.json('/api/' + assignment_number + '/matches', function(error, json) {

        json.matches = $.grep(json.matches, function(m) {
            return m.source != m.target
        });

        var graph = new Graph();
        for (var i = 0; i < json.matches.length; i++) {
            graph.add_edge(json.matches[i].source, {
                source_id: json.matches[i].source_id,
                target_id: json.matches[i].target_id,
                target: json.matches[i].target,
                confidence: json.matches[i].confidence,
                line_numbers: [ {source: {start: 10, end: 15}, target: {start: 17, end: 22}} ]
            });
        }

        groups = graph.get_groups();

        // list table

        // graph table

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
            $('.line-highlight').remove();
        });
    });
}


//

function run() {
    // set_vertical_layout();
    // set_groups_list();
    // bind_diff_scrolling();
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

function select_pair(d) {
    console.log(d);
    d3.select('.confidence h3').text(parseInt(d.confidence)/10 + '%');
    populate_code('left', d.source);
    populate_code('right', d.target);
    $code_l.addClass('loading');
    $code_r.addClass('loading');
    d3.json('/api/'+assignment_number+'/'+d.source_id+'/', function(error, json) {
        set_line_numbers(json);
        Prism.highlightAll();
        $code_l.removeClass('loading');
        $code_r.removeClass('loading');
    });
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
        d3.select('.confidence h3').text( parseInt(d.confidence)/10 + '%');
        populate_code('left', d.source.name);
        populate_code('right', d.target.name);
        $code_l.addClass('loading');
        $code_r.addClass('loading');
        d3.json('/api/'+assignment_number+'/'+d.source_id+'/', function(error, json) {
            set_line_numbers(json);
            Prism.highlightAll();
            $code_l.removeClass('loading');
            $code_r.removeClass('loading');
        });
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
    console.log(lines);
    var data_line_l = lines.source;
    var data_line_r = lines.target;
    var start, end;

    code_l.attr('data-line', data_line_l);
    code_r.attr('data-line', data_line_r);

    var code_l_w = $('.code-left code').width() + 50;
    var code_r_w = $('.code-right code').width() + 50;
    setTimeout(function() {
        $('.code-left .line-highlight').css('width', code_l_w);
        $('.code-right .line-highlight').css('width', code_r_w);
    }, 10);

}

d3.json('/api/' + assignment_number + '/code', function(error, json) {
    code = json;
});


// click nav tab

$nav_lis.on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    var $tgt = $(e.target).closest('li');
    var idx = $nav_lis.index($tgt);
    $nav_lis.removeClass('active');
    var selected = $nav_lis[idx];
    $(selected).addClass('active');

    // update column class
    var $l_col = $('#left-col > div');
    $l_col.removeClass('active');
    console.log($l_col[idx]);
    $($l_col[idx]).addClass('active');
});

*/


})();
