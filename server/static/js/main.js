/**
 * main.js
 * Author: Jarred de Beer
 * Date: 22 September 2014
 *
 * Description: This file is used in the cheaters_review.html template
 * to enhance the page with responsive UI functionality. It is responsible
 * for initializing all the data needed for interaction, which it obtains by
 * sending asynchronous HTTP requests to the server on page load (see the
 * run() function which is the point of execution).
 *
 * It is responsible for registering click events to the buttons on the page:
 * The "Pairs of Students", "Groups of Students" and "Code view" navigation
 * tabs; Transitions between tab views when clicking a pair in the list;
 * rendering the diagrams (Histogram and Graph) on click; maintaining the state
 * of the system to allow the 'Back' button to transition to the previous view;
 * rendering and enhancing the code in the 'Code view'; Reporting students
 * as having cheated from the 'Report Student' buttons on the 'Code view'
 *
 * Dependencies:
 * - jQuery.js
 * - D3.js
 * - Prism.js
 * - Graph.js
 *
 **/

// self executing anonymous function, creating a closure
// that protects the global scope.

(function() {

// selectors for indexing DOM elements.
// all DOM selections made in the code
// are listed and can be adjusted here.

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
    student_A_pre_selector   = code_selector + ' .A pre',
    student_A_code_selector  = code_selector + ' .A code',
    student_B_id_selector    = code_selector + ' .B .id',
    student_B_lines_selector = code_selector + ' .B .lines',
    student_B_pre_selector  = code_selector + ' .B pre',
    student_B_code_selector = code_selector + ' .B code',
    mark_button_selector = code_selector + ' ' + action_bar_selector + ' .mark';

// local variables to store system data

var code = {},
    confidence_values = [];

// begin methods

// Promise which fetches data used by the UI.
// - Gets student pairs,
// - Generates groups from student pairs,
// - Populate data for Histogram,
// - Fullfill promise with pairs, groups, histogram data.
//
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
                    line_numbers: []
                });
                // histogram
                histogram.push(json.matches[i].confidence);
            }
            groups = graph.get_groups();

            fulfill({
                pairs: json.matches,
                groups: groups,
                histogram: histogram
            });

        });

    });

}

// Promise to fetch all the code submissions for the current assignment
// Fulfilled by an Object Hash with student numbers as keys and code String as value
//
var fetch_code = function() {
    return new Promise(function(fulfill, reject) {
        d3.json(get_api_url('code'), function(error, json) {
            if (error) reject(error);
            fulfill(json);
        });
    });
}

// Enhances the Prism Code blocks with line numbers
//
var set_line_numbers = function(lines) {
    var pre_A = d3.select(student_A_pre_selector),
        pre_B = d3.select(student_B_pre_selector);

    var data_line_l = lines.source,
        data_line_r = lines.target,
        start, end;

    // set line number data attributes
    pre_A.attr('data-line', lines.source);
    pre_B.attr('data-line', lines.target);

    var code_A_w = $(student_A_code_selector).width() + 50,
        code_B_w = $(student_B_code_selector).width() + 50;

    // make line highlight blocks full width of horizontal scrollable area
    setTimeout(function() {
        $(student_A_pre_selector + ' .line-highlight').css('width', code_A_w);
        $(student_B_pre_selector + ' .line-highlight').css('width', code_B_w);
    }, 1);

}

// Enable mirroring of scrolling of the left code block by the right code block
// The right code block scrolls independently in order to match offsets where
// line number matches are not one-to-one between both sources of code.
//
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

// Set a row of students from a Pair into either the:
// - 'Pairs of students' table
// - 'Groups of students' table
//
var set_pair_row = function(tr) {
    tr.append('td').text(function(d, i) { return i + 1 });
    tr.append('td').text(function(d, i) { return d.source });
    tr.append('td').text(function(d, i) { return d.target });
    tr.append('td').text(function(d, i) { return d.confidence });
}

// Draw the graph of a student group in the diagram to the right of
// the 'Groups of students' list. Enable clicking of an edge to
// transition to the 'Code View'.
//
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
    // side effect: sets name to [object]. need to set it back to string at end of function.
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

    // graph edges
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

    // graph nodes
    var circle = svg.append("g").selectAll("circle")
        .data(force.nodes())
      .enter().append("circle")
        .attr("r", 10)
        .call(force.drag);

    // graph node student numbers
    var text = svg.append("g").selectAll("text")
        .data(force.nodes())
      .enter().append("text")
        .attr("x", 10)
        .attr("y", 5)
        .text(function(d) { return d.name; });

    // bind click event to graph edge
    path.on('click', function(d) {
        populate_code_view({
            source: d.source.name,
            target: d.target.name,
            source_id: d.source_id,
            target_id: d.target_id,
            confidence: d.confidence
        });
        transition_view('code');
    });

    // helper functions provided by d3 template
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

// resets the name attribute of the d object used by d3
// to allow for the graph to be rendered properly more than once.
// This occurs due to a side effect from the d3 graph drawing code
// that happens from a mutation on the d object after first time the graph is rendered.
var reset_d_name = function(links) {
    links.forEach(function(link) {
        if (typeof link.source == 'object') {
            link.source = link.source.name;
            link.target = link.target.name;
        }
    });
}

// Draw the histogram which appears to the right of the 'Pairs of students' list.
// This is run on page load by initialize_data() in the run() function.
//
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

// Set the table which lists Student pairs in the 'Pairs of students' view.
//
var set_pairs_table = function(pairs) {
    var tr = d3.select(pairs_tbody_selector).selectAll('tr')
        .data(pairs)
        .enter().append('tr')

    set_pair_row(tr);
    tr.on('click', function(d) {
        $(subgroups_selector + ' tr.selected').removeClass('selected');
        $(this).addClass('selected');
        populate_code_view(d);
        transition_view('code');
    });
}

// Set the table which lists Group pairs in the 'Groups of students' view.
// This differs from the 'Pairs of students' table in that it is a table
// containing multiple tbody elements for each group where each tbody lists the
// pairs. Wheras the 'Pairs of students' table has just one tbody listing all pairs.
//
var set_groups_table = function(list) {

    var tbody = d3.select(groups_table_selector).selectAll('tbody')
        .data(list)
        .enter()
        .append('tbody');

    // highlight selected group and draw the corresponding graph
    tbody.on('click', function(d) {
        $(subgroups_selector + ' tr.selected').removeClass('selected');
        $(this).find('tr').addClass('selected');
        reset_d_name(d);
        draw_graph_diagram(d);
    });

    var tr = tbody.selectAll('tr')
        .data(function(d) { return d })
        .enter()
        .append('tr');

    set_pair_row(tr);

    // set the first cell of the first row in each tbody with the number of pairs in the group
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

// Dynamically render buttons in the action toolbar of the 'Code view' which
// scrolls the code to the appropriate line number when clicked.
// lines is a comma separated list of number ranges, i.e. "1-5,10-13,54-75"
//
var set_action_line_buttons = function(lines) {

    // extract line ranges
    var ranges = lines.split(','),
        line_height = parseFloat($(student_A_pre_selector).css('line-height'));

    // generate button elements for each line range
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

    // set click event to scroll code to the top line
    $(shared_lines_selector + ' .btn').on('click', function(e) {
        e.preventDefault();
        var scroll_top = parseFloat($(e.target).data('top'));
        $(student_A_pre_selector).scrollTop(scroll_top);
    });
}

// Promise to either insert or delete an entry for a student in the Report table
// If the 'del' param is true it sends a DELETE request to delete a student, otherwise
// it sends a POST request to insert a student
//
var send_report = function(student, del) {
    var type = (del) ? 'DELETE' : 'POST';
    return new Promise(function(fulfill, reject) {
        $.ajax({
            url: get_api_url('mark'),
            type: type,
            data: {
                student: student,
                assignment_number: assignment_number
            },
            success: function(res) { fulfill(res) },
            error: function(err) { reject(err) }
        });
    });
}

// Populates the 'Code view' with code from the student pairs,
// re-initializes the view by clearing any existing
// line number information and re-establishing the state of the 'Report student' buttons
var populate_code_view = function(d) {

    // clean view
    $('.line-highlight').remove();
    $(shared_lines_selector).empty();

    // reset scroll on code
    $(student_A_pre_selector).scrollTop(0);
    $(student_B_pre_selector).scrollTop(0);
    $(student_A_pre_selector).scrollLeft(0);
    $(student_B_pre_selector).scrollLeft(0);

    if (!$(code_panel_body_selector).hasClass('rendered'))
        $(code_panel_body_selector).addClass('rendered');

    if (!$(code_panel_body_selector).hasClass('fetching'))
        $(code_panel_body_selector).addClass('fetching');

    $(mark_button_selector).each(function() {
        $(this).text($(this).data('text'));
        $(this).removeClass('btn-default')
            .addClass('btn-danger')
            .removeAttr('disabled');
    });

    // set Student A and Student B
    d3.select(student_A_id_selector).text(d.source);
    d3.select(student_B_id_selector).text(d.target);

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

// Promise to retrieve matching line numbers between a Pair of students
//
var retrieve_matches = function(id) {
    return new Promise(function(fulfill, reject) {
        d3.json(get_api_url('lines', id), function(error, json) {
            if (error) reject(error);
            fulfill(json);
        });
    });
}

// Helper function to return the appropriate url for API http requests.
// These URLS are needed in multiple places and thus only need to be updated here
// if the change.
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
        case 'mark':
            url = '/api/reports';
            break;
    }
    return url;
}

// Sets the vertical layout of elements on the page to fit the vertical
// height of the browser. Horizontal width is handled by CSS rules and are responsive
// to any reasonable page width. However, vertical height is nearly impossible to do with CSS
// and needs to be handled by javascript on page load.
//
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

// Helper function used by set_vertical_layout to get the css integer value
// of a specified CSS rule for a DOM element.
//
var get_css_val = function(rule, selector) {
    return parseInt($(selector).css(rule).replace('px', ''));
}

// Transitions the view between 'Pair of students', 'Groups of students' and 'Code view'
//
var transition_view = function(name) {
    // set the back button to the current view
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

// Mark a student as having Cheated or Undo a student which was marked as cheated.
// Triggered by click event on the 'Report Student A/B' buttons in the 'Code view'
//
var mark_student = function(btn) {
    var student, selector, orig_text;
    var choice = $(btn).attr('id');
    if (choice.indexOf('A') >= 0) {
        selector = student_A_id_selector;
    } else {
        selector = student_B_id_selector;
    }
    student = $(selector).text();
    // add student to report
    if ($(btn).text() == $(btn).data('text')) {
        $(btn).text('Reporting...');
        send_report(student).then(function() {
            $(btn).text('Undo');
            $(btn).removeClass('btn-danger')
                .addClass('btn-default');
        });
    // remove student from report
    } else {
        $(btn).text('Undoing...');
        send_report(student, true).then(function() {
            $(btn).text($(btn).data('text'));
            $(btn).removeClass('btn-default')
                .addClass('btn-danger');
        });
    }
}

// run method which is called on page load and is the initial entry point for main.js
//
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
        transition_view(view);
    })

    $(navtabs_li_a_selector).on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var view = $(e.target).closest('li').data('view');
        transition_view(view);
    });

    $(mark_button_selector).on('click', function(e) {
        e.preventDefault();
        btn = this;
        mark_student(this);
    });

    set_vertical_layout();
    mirror_code_scrolling();

    fetch_code().then(function(json) {
        code = json;
    });

}

// execute the run method. Main entry point.
run();


})();
