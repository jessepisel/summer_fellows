"""
Build and install the project.
"""
from setuptools import setup, find_packages

import versioneer


NAME = "aliaser"
FULLNAME = "Aliaser"
AUTHOR = "The Aliaser Developers"
AUTHOR_EMAIL = "destinydong@utexas.edu"
MAINTAINER = "Destiny Dong"
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = "MIT License"
URL = "https://github.com/jessepisel/summer_fellows/tree/master/Well%20Log%20Mnemonics/mnem-pointer-generator"
DESCRIPTION = (
    "Automated well log mnemonics parser"
)
KEYWORDS = "geophysics, geodesy"
with open("README.md") as f:
    LONG_DESCRIPTION = "".join(f.readlines())
VERSION = '0.0'
CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: {}".format(LICENSE),
]
PLATFORMS = "Any"
PACKAGES = find_packages(exclude=["doc"])
SCRIPTS = []
PACKAGE_DATA = {}
with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.readlines()
PYTHON_REQUIRES = ">=3.6"

if __name__ == "__main__":
    setup(
        name=NAME,
        fullname=FULLNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        platforms=PLATFORMS,
        scripts=SCRIPTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES
    )