mport absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 2 - Pre-Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering :: Information Analysis"]

# Description should be a one-liner:
description = "afmMiner: an image analysis tool for discovering materials properties from atomic force microscopy" 
# Long description will go up on the pypi page
long_description = """
AfmMiner
========
AfmMiner uses **Random Forests**, a kind of non-parametric supervised learning algorithm, to discover materials properties from atomic force microscopy (AFM) images. In particular, afmMiner can predict the photoluminesence of a material given some topographical and electrical AFM data. AfmMiner addresses a fundamental question: **can we predict PL from things that are not difraction limited?**.
To get started using these components in your own software, please go to the
repository README_.
.. _README: https://github.com/wesleybeckner/afm-miner/README.md
License
=======
``afmMiner`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
All trademarks referenced herein are property of their respective holders.
Copyright (c) 2015--, Wesley Beckner, The University of Washington
eScience Institute.
"""

NAME = "AfmMiner"
MAINTAINER = "Wesley Beckner"
MAINTAINER_EMAIL = "wesleybeckner@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/wesleybeckner/afm-miner"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Wesley Beckner"
AUTHOR_EMAIL = "wesleybeckner@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'afmMiner': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
