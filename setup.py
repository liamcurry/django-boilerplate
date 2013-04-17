from setuptools import setup
import sys


extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
    extra['convert_2to3_doctests'] = ['src/your/module/README.txt']
    extra['use_2to3_fixers'] = ['your.fixers']


setup(
    name='{{ project_name }}',
    author='Your name',
    author_email='your.email@gmail.com',
    license='MIT',
    description='An awesome module.',
    url='https://github.com/username/{{ project_name }}',
    install_requires=[
        'django',
        'django-extensions',
        'psycopg2',
        'south',
        'jinja2',
        'jingo',
        'django-assets',
        'yuicompressor',
        'ipython',
        'Werkzeug',
    ],
    dependency_links=[
        'https://github.com/miracle2k/webassets/archive/master.tar.gz#egg=webassets',
    ],
    classifiers=[

    ],
    **extra
)
