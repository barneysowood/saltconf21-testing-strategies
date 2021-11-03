ARG OS_VER=20.04
FROM ubuntu:$OS_VER

ARG SALT_VER=3003.3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y python3-pip git virtualenv

COPY etc/requirements.txt /tmp
RUN sed -i  "s/^salt==.*//" /tmp/requirements.txt
RUN virtualenv --python=python3 /opt/virtualenv
RUN /opt/virtualenv/bin/pip3 install salt==$SALT_VER
RUN /opt/virtualenv/bin/pip3 install -r /tmp/requirements.txt
COPY bin/runlevel /usr/sbin
