FROM centos:6

MAINTAINER Alvaro Vega <alvaro.vegagarcia@telefonica.com>

ENV ORCHESTRATOR_USER orchestrator
ENV GIT_REV_ORCHESTRATOR develop
ENV CLEAN_DEV_TOOLS 1

ENV KEYSTONE_HOST localhost
ENV KEYSTONE_PORT 5001
ENV KEYSTONE_PROTOCOL http

ENV KEYPASS_HOST localhost
ENV KEYPASS_PORT 17070
ENV KEYPASS_PROTOCOL http

ENV ORION_HOST localhost
ENV ORION_PORT 1026
ENV ORION_PROTOCOL http

ENV IOTA_HOST localhost
ENV IOTA_PORT 4052
ENV IOTA_PROTOCOL http

ENV STH_HOST localhost
ENV STH_PORT 18666
ENV STH_PROTOCOL http

ENV PERSEO_HOST localhost
ENV PERSEO_PORT 19090
ENV PERSEO_PROTOCOL http


RUN adduser --comment "${ORCHESTRATOR_USER}" ${ORCHESTRATOR_USER}


RUN \
    # Install dependencies
    yum update -y && yum install -y wget && \
    wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && \
    yum localinstall -y --nogpgcheck epel-release-6-8.noarch.rpm && \
    yum install -y python git python-pip python-devel python-virtualenv gcc ssh && \
    # Install orchestrator from source
    git clone https://github.com/telefonicaid/orchestrator && \
    cd orchestrator && \
    git checkout ${GIT_REV_ORCHESTRATOR} && \
    pip install -r requirements.txt && \
    pip install repoze.lru

ENV python_lib /var/env-orchestrator/lib/python2.6/site-packages

RUN mkdir -p $python_lib/iotp-orchestrator
COPY ./src/ $python_lib/iotp-orchestrator
RUN find $python_lib/iotp-orchestrator -name "*.pyc" -delete
COPY ./bin/orchestrator-daemon.sh /etc/init.d/orchestrator
COPY ./bin/orchestrator-daemon /etc/default/orchestrator-daemon
RUN ln -s $python_lib/iotp-orchestrator /opt/orchestrator
RUN mkdir -p $python_lib/iotp-orchestrator/bin
COPY ./bin/orchestrator-entrypoint.sh /opt/orchestrator/bin
RUN ln -s /opt/orchestrator/orchestrator/commands /opt/orchestrator/bin/
RUN mkdir -p /var/log/orchestrator


# Set IOTP EndPoints in orchestrator config
RUN sed -i ':a;N;$!ba;s/KEYSTONE = {[A-Za-z0-9,\"\n: ]*}/KEYSTONE = { \
             \"host\": \"'$KEYSTONE_HOST'\", \
             \"port\": \"'$KEYSTONE_PORT'\", \
             \"protocol\": \"'$KEYSTONE_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

RUN sed -i ':a;N;$!ba;s/KEYPASS = {[A-Za-z0-9,\"\n: ]*}/KEYPASS = { \
             \"host\": \"'$KEYPASS_HOST'\", \
             \"port\": \"'$KEYPASS_PORT'\", \
             \"protocol\": \"'$KEYPASS_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

RUN sed -i ':a;N;$!ba;s/ORION = {[A-Za-z0-9,\"\n: ]*}/ORION = { \
             \"host\": \"'$ORION_HOST'\", \
             \"port\": \"'$ORION_PORT'\", \
             \"protocol\": \"'$ORION_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

RUN sed -i ':a;N;$!ba;s/ORION = {[A-Za-z0-9,\"\n: ]*}/IOTA = { \
             \"host\": \"'$IOTA_HOST'\", \
             \"port\": \"'$IOTA_PORT'\", \
             \"protocol\": \"'$IOTA_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

RUN sed -i ':a;N;$!ba;s/STH = {[A-Za-z0-9,\"\n: ]*}/STH = { \
             \"host\": \"'$STH_HOST'\", \
             \"port\": \"'$STH_PORT'\", \
             \"protocol\": \"'$STH_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

RUN sed -i ':a;N;$!ba;s/PERSEO = {[A-Za-z0-9,\"\n: ]*}/PERSEO = { \
             \"host\": \"'$PERSEO_HOST'\", \
             \"port\": \"'$PERSEO_PORT'\", \
             \"protocol\": \"'$PERSEO_PROTOCOL'\" \
}/g' /opt/orchestrator/settings/dev.py

# TODO: put IOT endpoints conf into ochestrator-entrypoint.sh
RUN sed -i 's/KEYSTONE_PORT=5001/KEYSTONE_PORT='$KEYSTONE_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/KEYSTONE_PROTOCOL=http/KEYSTONE_PROTOCOL='$KEYSTONE_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/KEYPASS_PORT=17070/KEYPASS_PORT='$KEYPASS_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/KEYPASS_PROTOCOL=http/KEYPASS_PROTOCOL='$KEYPASS_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/ORION_PORT=1026/ORION_PORT='$ORION_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/ORION_PROTOCOL=http/ORION_PROTOCOL='$ORION_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/IOTA_PORT=4052/IOTA_PORT='$IOTA_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/IOTA_PROTOCOL=http/IOTA_PROTOCOL='$IOTA_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/STH_PORT=18666/STH_PORT='$STH_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/STH_PROTOCOL=http/STH_PROTOCOL='$STH_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/PERSEO_PORT=19090/PERSEO_PORT='$PERSEO_PORT'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN sed -i 's/PERSEO_PROTOCOL=http/PERSEO_PROTOCOL='$PERSEO_PROTOCOL'/g' /opt/orchestrator/bin/orchestrator-entrypoint.sh

# just for debugging
RUN cat  /opt/orchestrator/bin/orchestrator-entrypoint.sh
RUN cat /opt/orchestrator/settings/dev.py

WORKDIR /

# Define the entry point
ENTRYPOINT ["/opt/orchestrator/bin/orchestrator-entrypoint.sh"]

EXPOSE 8084
