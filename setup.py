#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sena Heydari",
    author_email='sheydari@dosomething.org',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="Data Platform Code for DoSomething.org",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ironheart',
    name='ironheart',
    packages=find_packages(include=['ironheart']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DoSomething/ironheart',
    version='2019.09.12.02',
    zip_safe=False,
)
