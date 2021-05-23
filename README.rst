compredict_interview_task
=========================

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Overview
--------
This project containes small API written with Django Rest Framework.

API has only one endpoint: api/v1/standardize which takes json containing three sensor lists containing decimal numbers.

Json is getting validated with help of Serializer. In case of unequal lists being provided in json, ValidationError is thrown.

Data is then passed to Transformer class, which takes care of standardization.

Quote: "The standardization technique is simply removing the mean and dividing by standard divation for each column"

Endpoint returns standardized data.

Source Code
---------------
API dir in the project is called: standardizing_api

Basic Commands
--------------
1. Install requirements with: pip -r requirements/local.txt
2. Run the standardizing_api with: python3 manage.py runserver
3. Now you can use the endpoint. Address: http://127.0.0.1:8000/api/v1/standardize

Docker:
1. Run: docker-compose up
2. Use containarized api: http://127.0.0.1:8000/api/v1/standardize

Testing
-------------

In order to check test coverage of the project, from root directory run simply: pytest --cov=standardizing_api standardizing_api/tests
