'use strict';

var exec = require('child_process').exec;

var del = require('del');
var merge = require('merge-stream');
var source = require('vinyl-source-stream');
var es = require('event-stream');

var gulp = require('gulp');
var plugins = require('gulp-load-plugins')();

/**
 * Build Bootstrap's JS and CSS.
 */
gulp.task('buildBootstrap', function() {
  // Delete unwanted Bootstrap JavaScript files
  del([
    'node_modules/bootstrap/js/*.js',
    '!node_modules/bootstrap/js/{transition,collapse}.js'
  ], function() {});

  // Replace Bootstrap's main LESS file
  gulp.src('assetsrc/bootstrap.less')
    .pipe(gulp.dest('node_modules/bootstrap/less/'));

  // Compile Bootstrap
  exec(
    "cd node_modules/bootstrap/ && node -e \"require('grunt').tasks(['dist']);\""
  );
});

/**
 * Build JS that's used on the whole site.
 */
gulp.task('siteJs', ['buildBootstrap'], function() {
  return gulp.src([
    'assetsrc/scroll-to-top.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js'
  ])
    .pipe(plugins.uglify())
    .pipe(plugins.concat('hydra.min.js'))
    .pipe(gulp.dest('hydra/static/js/'))
});

/**
 * Build JS that's only used on the blog.
 */
gulp.task('blogJs', function() {
  return gulp.src([
    'assetsrc/blog/jquery.cookies.js',
    'assetsrc/blog/socialshareprivacy.js',
    'assetsrc/blog/jquery.socialshareprivacy.min.autoload.js',
  ])
    .pipe(plugins.uglify())
    .pipe(plugins.concat('hydra.blog.min.js'))
    .pipe(gulp.dest('hydra/static/js/'))
});

/**
 * Build the site's CSS.
 */
gulp.task('siteCss', function() {
  return merge(
    gulp.src('node_modules/bootstrap/dist/css/bootstrap.min.css')
  ,
    es.child(exec('./env/bin/pygmentize -S manni -f html -a ".codehilite pre"'))
    .pipe(source('manni.css'))
  )
    .pipe(plugins.order(['bootstrap.min.css', 'manni.css']))
    .pipe(plugins.minifyCss({keepSpecialComments: 0}))
    .pipe(plugins.streamify(plugins.concat('hydra.min.css')))
    .pipe(gulp.dest('hydra/static/css/'))
});

/**
 * Build the site's JS and CSS.
 */
gulp.task('build', [
  'siteJs',
  'blogJs',
  'siteCss',
]);
