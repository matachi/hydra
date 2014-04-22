#!/usr/bin/env bash

virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install django
python3 manage.py collectstatic