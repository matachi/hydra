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
RUN pip3 install Django==1.7.1
RUN pip3 install Markdown==2.5.2
RUN pip3 install beautifulsoup4==4.3.2
RUN pip3 install django-pipeline==1.4.2
RUN pip3 install django-widget-tweaks==1.3

RUN apt-get install -y libjpeg-dev
RUN pip3 install Pillow==2.6.1

RUN pip3 install six==1.8.0
RUN pip3 install pytz==2014.10
RUN pip3 install django-comments-xtd==1.3a1

# Comment out a line from /etc/pam.d/sshd to not get `Connection to 127.0.0.1
# closed. Exit status 254.` when connection to the container over ssh.
RUN sed -i 's/^\(session    required     pam\_loginuid\.so\)/\#\1/' /etc/pam.d/sshd

RUN sed -i 's/^\(PermitRootLogin\) without-password/\1 yes/' /etc/ssh/sshd_config

CMD /usr/sbin/sshd && bash
