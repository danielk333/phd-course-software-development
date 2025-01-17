gulp.task('serve', () => {

    connect.server({
        root: root,
        port: port,
        host: host,
        livereload: true
    })

    gulp.watch(['*.html', '*.md', '*.css'], gulp.series('reload'))
    gulp.watch(['dist/theme/my*.css', 'css/*.css', '*.css'], gulp.series('reload'))
    gulp.watch(['presentations/**/*.html', 'presentations/**/*.md'], gulp.series('reload'))
    gulp.watch(['plugin/**/plugin.js', 'plugin/**/*.html'], gulp.series('plugins', 'reload'))
    gulp.watch(['js/**'], gulp.series('js', 'reload'))
})