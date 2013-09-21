#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement, division, absolute_import
from setuptools import setup, find_packages


def main():
    setup(
        name='''package_template''',
        long_description='''This is very simple package template only''',
        version='''0.0.1''',
        url='''https://github.com/truszkowski/python-template''',
        author='''truszkowski''',
        author_email='''truszkowski@gmail.com''',
        platforms=['unix', 'linux', 'osx'],
        classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Topic :: Software Development :: Libraries',
            'Topic :: System :: Distributed Computing',
            'Topic :: System :: Networking',
            'Programming Language :: Python'],
        packages=find_packages(),
        install_requires=[p.strip() for p in open('requirements.txt')],
        entry_points={
            'console_scripts': [ 
                'package_template_main = package_template.main:main' 
            ]
        },
        zip_safe=False,
        include_package_data=True
    )

    
if __name__ == '__main__':
    main()
