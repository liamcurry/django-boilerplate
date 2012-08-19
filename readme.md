# Django Boilerplate

This is a baseline for my Django projects, and so it makes some assumptions for
some of my personal preferences and directory structure.

You can use it yourself by running this command (if using Django 1.4+):

```
django-admin.py startproject --template https://github.com/liamcurry/django-boilerplate/zipball/master project_name
```

## Features

* `make` will create a virtual environment, install requirements, and compile
  assets.
* `make assets` will compile [LESS](http://lesscss.org/), [SASS](http://sass-lang.com/),
  [Stylus](http://learnboost.github.com/stylus/), and
  [CoffeeScript](http://coffeescript.org/) automatically. It will also minify and
  gzip all generated CSS and JS files. Use
  [watch](https://github.com/visionmedia/watch) (`watch make`) to have this all done
  automatically when there are changes made.
* `make clean` will remove common trash files, along with generated and minified
  CSS/JS files.

## TODO

* Better documentation.
* Structure for project testing and documentation
