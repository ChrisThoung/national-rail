# -*- coding: utf-8 -*-

# For Python 2 compatibility
from __future__ import print_function

import csv
import os
from setuptools import setup


# Specify the file of station codes, available from:
# http://www.nationalrail.co.uk/stations_destinations/48541.aspx
station_codes = 'station_codes.csv'

# Write station codes to package before installing package
lookup = {}
with open(station_codes, 'rt') as f:
    f = csv.reader(f)
    for row in f:
        lookup[row[0]] = row[1]
with open(os.path.join('nationalrail', 'codes.py'), 'wt') as f:
    print('lookup =', lookup, file=f)


# Version numbering follows the conventions of Semantic Versioning 2.0.0:
# 1. MAJOR - changes with backwards-incompatible modifications to the API
# 2. MINOR - for backwards-compatible additions to functionality
# 3. PATCH - for backwards-compatible bug fixes
# Source: http://semver.org/spec/v2.0.0.html
MAJOR = 0
MINOR = 1
PATCH = 0
for_release = True

VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)
if not for_release:
    VERSION += '.dev'

# Write package version.py
with open(os.path.join('nationalrail', 'version.py'), 'w') as f:
    version_to_write = """\
MAJOR = '%d'
MINOR = '%d'
PATCH = '%d'
VERSION = '%d.%d.%d"""
    if not for_release:
        version_to_write += '.dev'
    version_to_write += '\''
    f.write(version_to_write % (MAJOR, MINOR, PATCH, MAJOR, MINOR, PATCH))

# Call setup()
setup(
    name='nationalrail',
    version=VERSION,
    description='Command-line tools for UK national rail queries',
    license='BSD',
    author='Chris Thoung',
    author_email='chris.thoung@gmail.com',
    url='https://github.com/cthoung/national-rail',
    packages=[
        'nationalrail',
    ],
    entry_points = {
        'console_scripts': ['nationalrail=nationalrail.__main__:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    platforms=['Any'],
)
