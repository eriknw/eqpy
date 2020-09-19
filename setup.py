#!/usr/bin/env python
from os.path import exists
from setuptools import setup

setup(
    name="eqpy",
    version="0.0.2",
    description="Solve systems of equations and assumptions, linear and "
    "non-linear, numerically and symbolically.",
    url="http://github.com/eriknw/eqpy/",
    author="https://raw.github.com/eriknw/eqpy/master/AUTHORS.md",
    maintainer="Erik Welch",
    maintainer_email="erik.n.welch@gmail.com",
    license="BSD",
    keywords="math CAS equations symbolic sympy",
    packages=[
        "eqpy",
    ],
    install_requires=["sympy"],
    tests_require=["pytest", "numpy"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    long_description=open("README.md").read() if exists("README.md") else "",
    zip_safe=False,
)
