# cookiecutter_simple_docker


- based on https://github.com/cookiecutter/cookiecutter-django
- https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html
- including DRF, excluding celery

Requirements:
- python3 -m pip freeze > requirements.txt 

# Getting started local default:
- python3.9 -m venv <virtual env path>
- source <virtual env path>/bin/activate
- cookiecutter gh:cookiecutter/cookiecutter-django
- cd <what you have entered as the project_slug at setup stage>
- python3 -m pip install -r requirements/local.txt
- git init # A git repo is required for pre-commit to install
- pre-commit install
  
# Getting started docker local:
- docker-compose -f local.yml build
