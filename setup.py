#!/usr/bin/env python
#from setuptools import setup, find_packages
from distutils.core import setup
from os import path
import sys

from CSSOnDiet import cod

try:
  from pypandoc import convert
  read_md = lambda f: convert(f, 'rst')
except ImportError:
  #print("warning: pypandoc module not found, could not convert Markdown to RST")
  read_md = lambda f: open(f, 'r').read()

try:
  long_description=read_md('README.md')
except OSError:
  print "Pypandoc probably not istalled (just python module)"
  sys.exit(1)
except:
  long_description=read_md(path.join('CSSOnDiet','README.md'))

setup(
  name="CSSOnDiet",
  version=cod.VERSION,
  description="Easy and fast CSS preprocessor",
  long_description=long_description,
  
  packages = ["CSSOnDiet"],
  scripts = ["cod"],

  data_files=[
    ('share/doc/CSSOnDiet', ['changelog','LICENSE','README.md'])
  ],

  url='http://cssondiet.com',
  author='Tomasz Wyderka',
  author_email='wyderkat@cofoh.com',

  license='GPL3',

 # https://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Topic :: Software Development :: Pre-processors',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
  ],
 
  # What does your project relate to?
  keywords='CSS preprocessor',
#
#    # To provide executable scripts, use entry points in preference to the
#    # "scripts" keyword. Entry points provide cross-platform support and allow
#    # pip to create the appropriate form of executable for the target platform.
#    entry_points={
#        'console_scripts': [
#            'CSS-On-Diet=code',
#        ],
#    },
)
