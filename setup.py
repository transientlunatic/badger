#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    "Click"
]

test_requirements = [
    # TODO: put package test requirements here
]


setup(
    name='badger',
    version='0.1.0',
    description="Badger is the research notebook for distributed research workflows.",
    long_description=readme + '\n\n' + history,
    author="Daniel Williams",
    author_email='d.williams.2@research.gla.ac.uk',
    url='https://github.com/transientlunatic/badger',
    packages=[
        'badger',
    ],
    package_dir={'badger':
                 'badger'},
    include_package_data=True,
    entry_points='''
        [console_scripts]
        badger=badger.badger:cli
    ''',
    license="ISCL",
    zip_safe=False,
    keywords='badger',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
