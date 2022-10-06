#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = [req for req in requirements_file.readlines()]

setup(
    name='sopel_modules.genius-answer',
    version=__version__,
    description='Genius-answer plugin for Sopel',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author='eoli3n',
    author_email='eoli3n@runbox.com',
    url='https://github.com/eoli3n/genius-answer-sopel-plugin',
    packages=find_packages('.'),
    namespace_packages=['sopel_modules'],
    include_package_data=True,
    install_requires=requirements,
    test_suite='tests',
    license='WTFPL',
)
