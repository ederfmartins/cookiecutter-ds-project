# Cookiecutter-ds-project
Cookiecutter-ds-project is a cookiecutter template that contains some boilerplate you need to create a ready to deploy (on AWS) artificial inteligence project.

**Warning: This template is not ready to use yet. At this moment this template only configures a local virtualenv and commit some files to github.**

# What this template do for you

    - It creates the bare bones of your new project.
    - It provides some usefull scripts to configure your project in a new machine.
    - It configures a basic CI env to you, using werker (in the future Travis CI and Coveralls too).
    - It configures ansible to deploy your project to AWS EC2 instances (not implemented yet).

# Get start

    - Create a new repository on GitHub. To avoid errors, do not initialize the new repository with README, license, or gitignore files.
    - Install cookiecutter
    ```bash
    pip install cookiecutter
    ```
    - Create the project skeleton
    ```bash
    cookiecutter cookiecutter-ds-project/
    ```
    - Start coding :)

# Some usefull scritpts

    - Use deploy/local/configure_local_dev_env.sh to initialize your local env.
    

# TODO:

    - add docker to deploy/local/
    - add ansible to deploy/prod/
    - add a github hook to avoid merges if travis fail
    - automate wercker Application creation
        - http://old-devcenter.wercker.com/articles/gettingstarted/cli.html
