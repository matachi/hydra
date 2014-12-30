# Hydra

Personal website and blog.

Author: Daniel Jonsson  
License: [MIT License](LICENSE)

## Run with Docker

Build the Docker image:

    $ sudo docker build -t matachi/hydra .

Run the image:

    $ sudo docker run -i -t -v `pwd`:/home/hydra/app:rw -p 8000:8000 -p 1337:22 matachi/hydra

Then start the Django development web server:

    $ python3 /home/hydra/app/manage.py runserver 0.0.0.0:8000

Finally open [127.0.0.1:8000](http://127.0.0.1:8000) in the web browser.

## Configure PyCharm

To work with the project in PyCharm and still run it in Docker, read the
following text.

Set your project Python interpreter to a remote interpreter. Configure it with
the following settings:

    Host: 127.0.0.1
    Port: 1337
    Username: root
    Auth type: Password
    Password: pass
    Python interpreter path: /usr/bin/python3

And before starting a *Django server*, make the following configurations:

    Host: 0.0.0.0
    Port: 8000
    Path mappings: /path/to/hydra/on/host=/home/hydra/app

Where `/path/to/hydra/on/host` is the directory on the host where this project
directory is located.

## Build JS and CSS

### Prerequisites

Install Node.js, npm, gulp and virtualenv.

#### Debian and Ubuntu

Instructions to install the prerequisites on a Debian based system (Ubuntu for
example):

    $ sudo apt-get install nodejs python-virtualenv
    $ sudo npm install -g gulp
    $ sudo chown -R `whoami`:`whoami` ~/.npm ~/tmp

#### Fedora

Instructions for Fedora:

    $ sudo dnf install nodejs npm python-virtualenv
    $ sudo npm install -g gulp

Note, use `yum` instead of `dnf` if `dnf` isn't available.

### Setup

Install build tools and dependencies:

    $ npm install

Note, the above command will also execute [postinstall.sh](postinstall.sh).

### Build

    $ gulp build

## Interact with a server

Copy the SQLite database file from a server over SSH:

    $ scp [hostname]:hydra/db.sqlite3 .

This is useful when the site is deployed on a remote server and you want to
retrieve the database for local testing and development.

## Manually build the syntax highlighting stylesheet

This is already done by `$ gulp build`.

    $ pygmentize -S manni -f html -a ".codehilite pre" > manni.css

## Manually build Social Share Privacy

This is already done by `$ gulp build`.

Download from <https://github.com/panzi/SocialSharePrivacy> and run:

    $ ./build.sh -m tumblr,twitter,facebook -l none
