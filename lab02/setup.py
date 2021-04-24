from setuptools import setup
from os.path import join, dirname


setup(
    name = 'custom_serialiser',
    long_description = open(join(dirname(__file__),"README.txt")).read(),
    py_modules = [
        'console_app',
        'arguments',
        'classes',
        'decoder',
        'encoder',
        'fabric_cls',
        'my_json',
        'my_pickle',
        'my_toml',
        'my_yaml',
        'pickler'
        ],
    entry_points = {
        'console_scripts': ['custom_serialiser = console_app:main',
         ], 
    }

)