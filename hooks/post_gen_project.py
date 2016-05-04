#!/usr/bin/env python

import os
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def add_github():
    subprocess.call('git init', shell=True)
    subprocess.call('git add .', shell=True)
    subprocess.call('git commit -m "First commit"', shell=True)
    subprocess.call(
        'git remote add origin "{{  cookiecutter.repo_url }}"',
        shell=True
    )
    subprocess.call('git remote -v', shell=True)
    subprocess.call('git push origin master', shell=True)


def add_werker():
    subprocess.call('wercker create', shell=True)

if __name__ == '__main__':
    script = "deploy/local/configure_local_dev_env.sh"
    print (PROJECT_DIRECTORY)
    return_code = subprocess.call(script, shell=True)
    if return_code != 0:
        sys.exit(return_code)
    add_github()
    # add_werker()
