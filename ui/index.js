var express = require('express');
var app = express();

app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res) {
    console.log('received request');
    res.sendfile(__dirname + '/public/index.html');
});

app.listen(6006);
