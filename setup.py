# -*- coding: utf-8 -*-


import os
from distutils.core import setup


# Specify the file of station codes, available from:
# http://www.nationalrail.co.uk/stations_destinations/48541.aspx
station_codes = 'station_codes.csv'

# Write station codes to package before installing package
with open(station_codes, 'rt') as f:
    table = f.read().splitlines()[1:]
table = [r.split(',')[0:2] for r in table]
lookup = dict(zip(
    [r[0] for r in table],
    [r[1] for r in table]))
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
for_release = False

VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)
if not for_release:
    VERSION += '.dev'

# Write package version.py
with open(os.path.join('nationalrail', 'version.py'), 'wt') as f:
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
    scripts=[
        'scripts/national-rail.py',
        ],
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
        ],
    platforms=['Any'],
    )
