==================
Django Boilerplate
==================

This is a baseline for my Django projects, and so it makes some assumptions for
some of my personal preferences and directory structure.

You can use it yourself by running this command (if using Django 1.4+)::

    django-admin.py startproject --template https://github.com/liamcurry/django-boilerplate/zipball/master project_name

Features
--------

- Automatic Stylus, SASS, Compass, and LESS compliation via `webassets`_.
- Automatic combining and minifying of CSS/JS assets via `webassets`_.
- Jinja2 templates via `jingo`_.

TODO
----

- Better documentation.
- Structure for project testing and documentation
- Sample git hooks for deployment, style checking, etc.


.. _webassets: https://github.com/miracle2k/webassets
.. _jingo: https://github.com/jbalogh/jingo
