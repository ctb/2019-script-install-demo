from __future__ import print_function
from setuptools import setup

VERSION="0.1"

SETUP_METADATA = \
               {
    "name": "fizbar",
    "version": VERSION,
    "description": "a quick demo of something",
    "author": "C. Titus Brown",
    "author_email": "titus@idyll.org",
    "license": "BSD 3-clause",
    "entry_points": {'console_scripts': [
        'fizbar = fizbar.__main__:main'
        ]
    },
    "include_package_data": True,
    "packages": ['fizbar'],
    "package_data": {
        "fizbar": ['*.dat']
    }
}
    
setup(**SETUP_METADATA)
