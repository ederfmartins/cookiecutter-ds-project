# coding: utf-8
import os
import re

import pip

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()

# grep {{ cookiecutter.source }}/__init__.py since python 3.x cannot import it
file_text = read(fpath('{{ cookiecutter.source }}/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


links = []
requires = []
requiriments_file_name = 'prod_requirements.txt'

try:
    requirements = pip.req.parse_requirements(requiriments_file_name)
    requirements = [r for r in requirements]
except:
    # new versions of pip requires a session
    requirements = pip.req.parse_requirements(
        requiriments_file_name, session=pip.download.PipSession())

for item in requirements:
    if item.req:
        requires.append(str(item.req))
    # older pip has url but newer versions have link
    if getattr(item, 'url', None):
        links.append(str(item.url))
    if getattr(item, 'link', None):
        links.append(str(item.link))

setup(
    name='{{ cookiecutter.source }}',
    version=grep('__version__'),
    url='{{ cookiecutter.repo_url }}',
    license='MIT',
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author }}@gmail.com",
    description='{{ cookiecutter.project_short_description }}',
    long_description="{{ cookiecutter.project_short_description }}",
    packages=["{{ cookiecutter.source }}"],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    dependency_links=links
)
