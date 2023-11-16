const gulp = require('gulp');

const sass = require('gulp-sass')(require('sass'));

// Tarea para compilar SASS a CSS
gulp.task('sass', function () {
    return gulp.src('templates/main/static/sass/**/*.scss') // Origen de los archivos SCSS
        .pipe(sass().on('error', sass.logError)) // Compila SCSS a CSS y maneja errores
        .pipe(gulp.dest('templates/main/static/css')); // Destino de los archivos CSS compilados
});

// Tarea para observar cambios en los archivos SCSS
gulp.task('watch', function () {
    gulp.watch('templates/main/static/sass/**/*.scss', gulp.series('sass'));
});

// Tarea por defecto que ejecuta las tareas 'sass' y 'watch'
gulp.task('default', gulp.series('sass', 'watch'));
