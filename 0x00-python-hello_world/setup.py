#!/usr/bin/python3
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1}},
    #windows = [{'script': "hello.py"}],
  console = [{'script': "hello.py"}],
    zipfile = None,
)
