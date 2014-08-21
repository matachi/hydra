#!/usr/bin/env bash

virtualenv env
source env/bin/activate
pip install django
pip install Markdown
pip install beautifulsoup4
pip install Pygments
pip install django-pipeline
pip install django-widget-tweaks
pip install Pillow

sudo apt-get install libjpeg-dev
pip install South

# See comment in `Dockerfile`
pip install https://bitbucket.org/andrewgodwin/south/get/e2c9102ee033.zip#egg=South

pip install six
pip install pytz
pip install django-comments-xtd

python3 manage.py collectstatic
