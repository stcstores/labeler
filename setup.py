#!/usr/bin/env python
"""Setup for labeler."""

import os

import setuptools

NAME = 'labeler'

with open("README.rst", "r") as readme:
    long_description = readme.read()

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, NAME, '__version__.py'), 'r') as f:
    exec(f.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    install_requires=['reportlab', 'pylabels'],
    packages=setuptools.find_packages(),
)
