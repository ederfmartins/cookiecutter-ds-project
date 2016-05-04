#!/usr/bin/env bash

echo "configure virtualenv"
source "/usr/local/bin/virtualenvwrapper.sh"
WORKON_HOME=$HOME/.virtualenvs
#mkvirtualenv --python=python{{ cookiecutter.python_version }} {{ cookiecutter.repo_name }}
mkvirtualenv {{ cookiecutter.repo_name }}
echo "install requirements"
set -e
pip install -r test_requirements.txt
pip install -r prod_requirements.txt
echo "install project as a python module"
make install
echo "test"
make test
