#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from setuptools import setup
import nose
import io

import scraper


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('readme.md')


setup(name='scraper',
      version=scraper.__version__,
      url='',
      license='?',
      author='Fernando Cezar',
      cmdclass={'test': nose},
      author_email='netcriptus@gmail.com',
      description='Simple web scraper backend',
      long_description=long_description,
      packages=['scraper'],
      include_package_data=True,
      platforms='any',
      zip_safe=False,
      classifiers=['Programming Language :: Python',
                   'Development Status :: 4 - Beta',
                   'Natural Language :: English',
                   'Environment :: Web Environment',
                   'License :: ?',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content'])
