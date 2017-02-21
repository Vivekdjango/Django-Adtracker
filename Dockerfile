FROM dockerhub.corp.inmobi.com/idp/docker-ubuntu-14.04-phat:20161010_7

MAINTAINER vivek.sinha@inmobi.com

RUN mkdir -p /opt/inmobi/usr/deployment/validate

RUN apt-get -y install apache2

RUN apt-get -y install python-pip

ENV INMOBI_DEPLOY /opt/inmobi/usr/deployment

#To install Apache WSGI module
RUN apt-get -y  install libapache2-mod-wsgi 

#Install dependencies
RUN apt-get -y install libldap2-dev

RUN apt-get -y install libsasl2-dev

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

RUN apt-get -y install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev gcc

#Upgrade pip
RUN pip install --upgrade pip
#Install ldap
RUN pip install python-ldap
#Install jira
RUN pip install jira
#Install django
RUN pip install django

RUN pip install PyJWT

RUN easy_install gevent

RUN pip install cryptography

RUN mkdir  /var/www/techstop/

RUN chmod -R 777 /var/www/techstop/

COPY techstop/  /var/www/techstop/

COPY 000-default.conf /etc/apache2/sites-available/

COPY techstop/conf/validate.sh  ${INMOBI_DEPLOY}/validate

COPY env.sh /var/www/techstop/

COPY apache2.conf /etc/apache2/

COPY techstop/conf/command.conf /etc/supervisor/conf.d/
