(function() {

var csv_download_selector = '#csv-download';

var set_csv_download_link = function(report) {

    var csv_content = "data:text/csv;charset=utf-8,Assignment " + assignment_number + "\n" + report.join('\n'),
        encoded_uri  = encodeURI(csv_content);

    $(csv_download_selector).attr('href', encoded_uri);
    $(csv_download_selector).attr('download', 'cheatah_report_assignment_' + assignment_number + '.csv');

}

set_csv_download_link(report);

})()
