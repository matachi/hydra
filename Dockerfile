FROM debian:latest

# Set locale to UTF-8
# RUN locale-gen en_US.UTF-8
# RUN update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
# ENV LANG en_US.UTF-8
# ENV LC_ALL en_US.UTF-8

RUN apt-get update

RUN mkdir /root/.pycharm_helpers

# Install and set up SSH
RUN apt-get install -y openssh-server
RUN echo "root:pass" | chpasswd
RUN mkdir /var/run/sshd

RUN apt-get install -y python3 python3-pip sqlite3
RUN pip-3.2 install django

CMD /usr/sbin/sshd && bash
