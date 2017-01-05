#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='labeler',
    version='1.0',
    description='Creates printable labels',
    author='Luke Shiner',
    install_requires=['reportlab', 'pylabels'],
    packages=find_packages(),
    )
