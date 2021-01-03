from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "pypsu: python drivers for electronic programable PSU"
# Long description will go up on the pypi page
long_description = """
This is a collection of Python scripts for controlling several workbench programable PSU.
For comunication requires pySerial.
"""

NAME = "pypsu"
MAINTAINER = "diozener"
MAINTAINER_EMAIL = "diozener@hotmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/diozener/pypsu"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "diozener"
AUTHOR_EMAIL = "diozener@hotmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGES = ['pypsu',
            'pypsu.tenma72',
            'pypsu.hanmatek']
PACKAGE_DATA = {'pypsu': [pjoin('data', '*')]}
REQUIRES = ["pyserial"]