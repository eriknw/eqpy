#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import eqpy

setup(
    name='eqpy',
    version=eqpy.__version__,
    description='Solve systems of equations and assumptions, linear and '
                'non-linear, numerically and symbolically.',
    url='http://github.com/eriknw/eqpy/',
    author='https://raw.github.com/eriknw/eqpy/master/AUTHORS.md',
    maintainer='Erik Welch',
    maintainer_email='erik.n.welch@gmail.com',
    license='BSD',
    keywords='math CAS equations symbolic sympy',
    packages=[
        'eqpy',
    ],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    long_description=open('README.md').read() if exists("README.md") else "",
    zip_safe=False,
)
