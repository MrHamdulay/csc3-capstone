var fs = require('fs')
  , Promise = require('promise')
  , request = require('request')
  , cheerio = require('cheerio');

// Use Promises along with Generators
// for asynchronous code that looks
// as clean as synchronous code but also
// identifiable as a asynchronous code.

function async(makeGenerator){
  return function () {
    var generator = makeGenerator.apply(this, arguments);

    function handle(result){
      // result => { done: [Boolean], value: [Object] }
      if (result.done) return Promise.resolve(result.value);

      return Promise.resolve(result.value).then(function (res){
        return handle(generator.next(res));
      }, function (err){
        return handle(generator.throw(err));
      });
    }

    try {
      return handle(generator.next());
    } catch (ex) {
      return Promise.reject(ex);
    }
  }
}

// Turn request objects into promises so
// they may also be used with the generator
// pattern.
function req_html(url) {
    return new Promise(function(fulfill, reject) {
        request(url, function(err, resp, html) {
            if (err) return reject(err);
            if (resp.statusCode !== 200 && resp.statusCode !== 201) {
                var err = new Error('Unexpected status code ' + resp.statusCode);
                err.res = resp;
                return reject(err);
            }
            fulfill(html);
        });
    });
}

//

var year = '2014';
var course = '1015';
var url = 'http://mufasa.cs.uct.ac.za/~hussein/2014/1015_plagiarism_reports/';
var assignments = {};

var get_results_page = async(function* (name) {
    var assignment_url = yield get_assignment_url(name);
    var assignment_html = yield req_html(assignment_url);
    return assignment_html;
});

//

var write_output = function (output) {
    return fs.writeFile('public/data/' + year + '_' + course + '_plagiarism_reports.json', JSON.stringify(output, null, 4));
}

var extract_diff_data = async(function* (url) {
    var html = yield req_html(url)
      , $ = cheerio.load(html);
    // get student id's
    var path_0 = $('table th:nth-child(1)').text();
    var path_1 = $('table th:nth-child(3)').text();
    //
    var file_0  = path_0.split('/')[2].split(' ')[0];
    var file_1  = path_1.split('/')[2].split(' ')[0];
    var stdnt_0 = path_0.split('/')[2].split('.')[0].toUpperCase();
    var stdnt_1 = path_1.split('/')[2].split('.')[0].toUpperCase();
    var cfdnc_0 = path_0.split('(')[1].split('%')[0];
    var cfdnc_1 = path_1.split('(')[1].split('%')[0];
    //
    var line_rows = $('table tr:not(:first-child)');
    var stdnt_0_lines = [];
    var stdnt_1_lines = [];
    var row;
    for (var i = 0; i < line_rows.length; i++) {
        $row = $(line_rows[i]);
        var stdnt_0_line = $row.find('a[target=0]').text();
        var stdnt_1_line = $row.find('a[target=1]').text();
        var start_0 = parseInt(stdnt_0_line.split('-')[0]);
        var end_0   = parseInt(stdnt_0_line.split('-')[1]);
        var start_1 = parseInt(stdnt_1_line.split('-')[0]);
        var end_1   = parseInt(stdnt_1_line.split('-')[1]);
        stdnt_0_lines.push([start_0, end_0]);
        stdnt_1_lines.push([start_1, end_1]);
    }
    var stdnt_0_data = {
        student: stdnt_0,
        confidence: cfdnc_0,
        file: file_0,
        matched_lines: stdnt_0_lines
    }
    var stdnt_1_data = {
        student: stdnt_1,
        confidence: cfdnc_1,
        file: file_1,
        matched_lines: stdnt_1_lines
    }
    var other_0 = clone(stdnt_0_data);
    var other_1 = clone(stdnt_1_data);
    stdnt_0_data.other = other_1;
    stdnt_1_data.other = other_0;
    return [stdnt_0_data, stdnt_1_data];
});

var get_diff_url = function* (html, url) {
    var $ = cheerio.load(html)
      , rows = $('table tr').length - 1;
    for (var i = 0; i < rows; i++) {
        yield url + '/match' + i + '-top.html';
    }
}

var get_result_url = async(function* (name) {
    var sub_url = url + name + '/moss.stanford.edu/results/';
    var refid = yield req_html(sub_url).then(function(html) {
        var $ = cheerio.load(html)
        return $('table tr:nth-child(4) td:nth-child(2) a').text().replace('/', '');
    });
    return sub_url + refid;
});

function extract_assignment_names(html) {
    var names = []
      , $ = cheerio.load(html)
      , $names = $('table tr td:nth-child(2) a');
    for (var i = 1; i < $names.length; i++) {
        names.push($names[i].attribs.href.replace('/', ''));
    }
    return names;
}

function fetch_assignments() {
    return req_html(url).then(extract_assignment_names);
}

var run = async(function* () {
    var output = {};
    console.log('fetching assignments');
    var assignments = yield fetch_assignments();
    var assgnmnt, refid, result_page, num_results;
    for(var i = 0; i < assignments.length; i++) {
        assgnmnt = assignments[i];
        console.log('fetching assignment ', (i + 1));
        output[assgnmnt] = {};
        result_url  = yield get_result_url(assgnmnt);
        result_html = yield req_html(result_url);
        console.log('requesting result html')
        for (var url of get_diff_url(result_html, result_url)) {
            var result = yield extract_diff_data(url);
            output[assgnmnt][result[0].student] = result[0];
            output[assgnmnt][result[1].student] = result[1];
        }
    }
    return output
});

run().then(function(output) {
    write_output(output);
    console.log('output written.');
}, function(err) {
    console.log(err);
});





//

function clone(obj) {
    var copy;

    // Handle the 3 simple types, and null or undefined
    if (null == obj || "object" != typeof obj) return obj;

    // Handle Date
    if (obj instanceof Date) {
        copy = new Date();
        copy.setTime(obj.getTime());
        return copy;
    }

    // Handle Array
    if (obj instanceof Array) {
        copy = [];
        for (var i = 0, len = obj.length; i < len; i++) {
            copy[i] = clone(obj[i]);
        }
        return copy;
    }

    // Handle Object
    if (obj instanceof Object) {
        copy = {};
        for (var attr in obj) {
            if (obj.hasOwnProperty(attr)) copy[attr] = clone(obj[attr]);
        }
        return copy;
    }

    throw new Error("Unable to copy obj! Its type isn't supported.");
}
