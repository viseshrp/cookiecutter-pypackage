#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import io

from setuptools import setup, find_packages

# Package meta-data.
NAME = '{{ cookiecutter.project_slug }}'
VERSION = '{{ cookiecutter.version }}'
DESCRIPTION = "{{ cookiecutter.project_short_description }}"
AUTHOR = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
EMAIL = '{{ cookiecutter.email }}'
URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
REQUIRES_PYTHON = ">=2.7"
REQUIREMENTS = ['future>=0.15.2', {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %} ]
SETUP_REQUIREMENTS = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]
TEST_REQUIREMENTS = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %} ]

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

with io.open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    HISTORY = history_file.read()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README + '\n\n' + HISTORY,
    keywords='{{ cookiecutter.project_slug }}',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    include_package_data=True,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    classifiers=[
        'Development Status :: 4 - Pre-Alpha',
{%- if 'no' not in cookiecutter.command_line_interface|lower %}
        'Environment :: Console',
{%- endif %}
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
{%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main',
        ],
    },
{%- endif %}
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
)
