#!/usr/bin/env bash

virtualenv env
source env/bin/activate
pip install django
pip install Markdown
pip install beautifulsoup4
pip install Pygments
pip install django-pipeline
pip install django-widget-tweaks
pip install South

sudo apt-get install libjpeg-dev
pip install Pillow

pip install six
pip install pytz
pip install django-comments-xtd

python3 manage.py collectstatic
