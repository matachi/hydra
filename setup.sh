#!/usr/bin/env bash

virtualenv env
source env/bin/activate

pip install Django==1.7.1
pip install Markdown==2.5.2
pip install beautifulsoup4==4.3.2
pip install django-pipeline==1.4.2
pip install django-widget-tweaks==1.3

sudo apt-get install libjpeg-dev
pip install Pillow==2.6.1

pip install six==1.8.0
pip install pytz==2014.10
pip install django-comments-xtd==1.3a1

python3 create_secret_key.py
python3 manage.py collectstatic
python3 manage.py syncdb
