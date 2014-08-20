'use strict';

var exec = require('child_process').exec;
var path = require('path');

var del = require('del');
var merge = require('merge-stream');
var source = require('vinyl-source-stream');
var es = require('event-stream');
var request = require('request');
var Sequence = require('sequence').Sequence;
var runSequence = require('run-sequence');

var gulp = require('gulp');
var plugins = require('gulp-load-plugins')();

/**
 * Delete files created by this script.
 */
gulp.task('clean', function() {
  return del([
    'SocialSharePrivacy-master/',
    'hydra/static/css/hydra.min.css',
    'hydra/static/js/hydra.blog.min.js',
    'hydra/static/js/hydra.min.js',
    'hydra/static/socialshareprivacy/',
  ], function(err) {
    if (err !== undefined) {
      console.log(err)
    }
  });
});

/**
 * Build Bootstrap's JS and CSS.
 */
gulp.task('buildBootstrap', function() {
  var sequence = Sequence.create();

  return sequence
    // Delete unwanted Bootstrap JavaScript files
    .then(function(next) {
      del([
        'node_modules/bootstrap/js/*.js',
        '!node_modules/bootstrap/js/{transition,collapse}.js'
      ], function() {
        next();
      });
    })
    // Replace Bootstrap's main LESS file
    .then(function(next) {
      gulp.src('assetsrc/bootstrap.less')
        .pipe(gulp.dest('node_modules/bootstrap/less/'))
        .on('end', function() {
          next();
        });
    })
    // Compile Bootstrap
    .then(function(next) {
      exec(
        "cd node_modules/bootstrap/ && node -e \"require('grunt').tasks(['dist']);\"",
        function() {
          next();
        }
      );
    });
});

/**
 * Build JS that's used on the whole site.
 */
gulp.task('siteJs', function() {
  return gulp.src([
    'assetsrc/scroll-to-top.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js'
  ])
    .pipe(plugins.uglify())
    .pipe(plugins.concat('hydra.min.js'))
    .pipe(gulp.dest('hydra/static/js/'))
});

/**
 * Download and build Social Share Privacy.
 */
gulp.task('buildSocialSharePrivacy', function() {
  var sequence = Sequence.create();

  return sequence
    // Download SocialSharePrivacy
    .then(function(next) {
      request('https://github.com/panzi/SocialSharePrivacy/archive/master.tar.gz')
        .pipe(source('SocialSharePrivacy.tar.gz'))
        .pipe(plugins.gunzip())
        .pipe(plugins.untar())
        .pipe(gulp.dest('.')).on('end', function() {
          next();
        })
    })
    // Get and update the PATH
    .then(function(next) {
      var envPath = process.env.PATH;
      process.env.PATH = process.env.PATH +
        ':' + path.join(__dirname, '/node_modules/uglify-js/bin') +
        ':' + path.join(__dirname, '/node_modules/uglifycss');
      next(envPath);
    })
    // Build SocialSharePrivacy
    .then(function(next, envPath) {
      exec(
        'cd SocialSharePrivacy-master/ && ./build.sh -m tumblr,twitter,facebook -l none'
      ,
        function(error, stdout, stderr) {
          if (error === null) {
            console.log(stdout);
          } else {
            console.log(stderr);
          }
          process.env.PATH = envPath;
          next();
        }
      );
    });
});

/**
 * Build JS that's only used on the blog.
 */
gulp.task('blogJs', ['buildSocialSharePrivacy'], function() {
  // Copy Social Share Privacy images
  gulp.src('SocialSharePrivacy-master/build/images/*')
    .pipe(gulp.dest('hydra/static/socialshareprivacy/images/'));

  // Copy Social Share Privacy CSS
  gulp.src('SocialSharePrivacy-master/build/stylesheets/*')
    .pipe(gulp.dest('hydra/static/socialshareprivacy/stylesheets/'));

  return merge(
    // Download one JS file
    request('http://panzi.github.io/SocialSharePrivacy/javascripts/jquery.cookies.js')
    .pipe(source('jquery.cookies.js'))
  ,
    gulp.src([
      'SocialSharePrivacy-master/build/javascripts/jquery.socialshareprivacy.min.autoload.js',
    ])
  )
    .pipe(plugins.order([
      'jquery.cookies.js',
      'jquery.socialshareprivacy.min.autoload.js'
    ]))
    .pipe(plugins.streamify(plugins.uglify()))
    .pipe(plugins.streamify(plugins.concat('hydra.blog.min.js')))
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
gulp.task('build', function() {
  runSequence(
    'buildBootstrap',
    ['siteJs', 'siteCss']
  );
  runSequence('blogJs');
});
