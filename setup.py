#!/usr/bin/env python
# :WORKAROUND: http://bugs.python.org/issue15881#msg170215
import multiprocessing
from setuptools import setup

setup(
    name='shovel',
    author='Jiawei Li',
    version='0.1.0',
    description='A set of tools for scrapers - simple and batteries included.',
    keywords='scraping framework download',
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://github.com/jiaweihli/mangopi/',
    author_email='jiawei.h.li@gmail.com',
    license='MIT'
)
