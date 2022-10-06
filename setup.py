#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
from setuptools import setup, find_packages

if __name__ == '__main__':
    print('Sopel does not correctly load plugins installed with setup.py '
          'directly. Please use "pip install .", or add {}/sopel_modules to '
          'core.extra in your config.'.format(
              os.path.dirname(os.path.abspath(__file__))),
          file=sys.stderr)

with open('requirements.txt') as requirements_file:
    requirements = [req for req in requirements_file.readlines()]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sopel_modules.genius-answer',
    version='0.0.2',
    description='Genius-answer plugin for Sopel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='eoli3n',
    author_email='eoli3n@runbox.com',
    url='https://github.com/eoli3n/genius-answer-sopel-plugin',
    packages=find_packages('.'),
    namespace_packages=['sopel_modules'],
    include_package_data=True,
    install_requires=requirements,
    license='WTFPL',
)
