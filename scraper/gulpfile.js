var gulp = require('gulp')
  , connect = require('connect')
  , watch = require('gulp-watch')
  , serveStatic = require('serve-static')
  , liveReload = require('gulp-livereload');

gulp.task('server', function(next) {
    var server = connect();
    server.use(serveStatic('public')).listen(8008, next);
});

gulp.task('watch', ['server'], function() {
    var server = liveReload();
    gulp.watch('public/**').on('change', function(file) {
        server.changed(file.path);
    });
});

gulp.task('default', ['server', 'watch']);
