FROM ubuntu:trusty

RUN apt-get update
RUN apt-get dist-upgrade -y

# Set locale to UTF-8
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN mkdir /root/.pycharm_helpers

# Install and set up SSH
RUN apt-get install -y openssh-server
RUN echo "root:pass" | chpasswd
RUN mkdir /var/run/sshd

RUN apt-get install -y python3-pip sqlite3
RUN pip3 install django
RUN pip3 install Markdown
RUN pip3 install beautifulsoup4
RUN pip3 install Pygments
RUN pip3 install django-pipeline
RUN pip3 install django-widget-tweaks
# South 1.0 is broken on Python 3. As of writing this, the commit that fixes
# this issue hasn't been packaged into a release yet.
# Relevant commit: https://bitbucket.org/andrewgodwin/south/commits/e2c9102ee033cc6d2ada2c67358cbeb6ad4615c0
RUN pip3 install https://bitbucket.org/andrewgodwin/south/get/e2c9102ee033.zip#egg=South

RUN apt-get install -y libjpeg-dev
RUN pip3 install Pillow

RUN pip3 install six
RUN pip3 install pytz
RUN pip3 install django-comments-xtd

# Comment out a line from /etc/pam.d/sshd to not get `Connection to 127.0.0.1
# closed. Exit status 254.` when connection to the container over ssh.
RUN sed -i 's/^\(session    required     pam\_loginuid\.so\)/\#\1/' /etc/pam.d/sshd

RUN sed -i 's/^\(PermitRootLogin\) without-password/\1 yes/' /etc/ssh/sshd_config

CMD /usr/sbin/sshd && bash
