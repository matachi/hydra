# Hydra

Podcast site built with Django.

## Run with Docker

Build the Docker image:

    sudo docker build -t matachi/hydra .

Run the image:

    sudo docker run -i -t -v `pwd`:`pwd`:rw -p 127.0.0.1:8000:8000 -p 127.0.0.1:1337:22 matachi/hydra

In the container, `cd` into the project folder, which is located at the same
path as on the host. Then start the Django development web server with:

    python3 manage.py runserver 0.0.0.0:8000

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
    PyCharm helpers path: /root/.pycharm_helpers

And before starting a *Django server*, configure the host IP to `0.0.0.0:8000`.

## Compile SocialSharePrivacy

Source: <https://github.com/panzi/SocialSharePrivacy>

    ./build.sh -m tumblr,twitter,facebook,pinterest -l none

## Compile Bootstrap files

Source: <http://getbootstrap.com/getting-started/>
Instructions: <https://github.com/twbs/bootstrap#compiling-css-and-javascript>

### Specify Bootstrap JS source files

Change `concat.bootstrap` in Gruntfile.js to:

    bootstrap: {
      src: [
        'js/transition.js',
        'js/collapse.js'
      ],
      dest: 'dist/js/<%= pkg.name %>.js'
    }

### Compile

    grunt dist

### Copy files

    cp less/bootstrap.less ~/PycharmProjects/hydra/assetsrc/.
    cp dist/css/bootstrap.min.css ~/PycharmProjects/hydra/hydra/static/css/.
    cp dist/js/bootstrap.min.js ~/PycharmProjects/hydra/hydra/static/js/.
