var gulp = require('gulp')
  , watch = require('gulp-watch')
  , livereload = require('gulp-livereload')
  , connect = require('connect')
  , serveStatic = require('serve-static');

gulp.task('server', function(next) {
    var server = connect();
    server.use(serveStatic('public')).listen(6007, next);
});

gulp.task('watch', ['server'], function() {
    var server = livereload();
    gulp.watch('public/**').on('change', function(file) {
        server.changed(file.path);
    });
});

gulp.task('default', ['server', 'watch']);
