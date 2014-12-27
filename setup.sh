#!/usr/bin/env bash

virtualenv env
source env/bin/activate

pip install Django==1.6.6
pip install Markdown==2.4.1
pip install beautifulsoup4==4.3.2
pip install Pygments==1.6
pip install django-pipeline==1.3.25
pip install django-widget-tweaks==1.3
pip install South==1.0.2

sudo apt-get install libjpeg-dev
pip install Pillow==2.5.3

pip install six==1.7.3
pip install pytz==2014.4
pip install django-comments-xtd==1.3a1

python3 manage.py collectstatic
