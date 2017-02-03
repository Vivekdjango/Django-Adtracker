FROM dockerhub.corp.inmobi.com/idp/docker-ubuntu-14.04-phat:20161010_7

MAINTAINER vivek.sinha@inmobi.com

RUN apt-get -y install apache2

RUN apt-get -y install python-pip

#To install Apache WSGI module
RUN apt-get -y  install libapache2-mod-wsgi 

#Install dependencies
RUN apt-get -y install libldap2-dev

RUN apt-get -y install libsasl2-dev

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
#Upgrade pip
RUN pip install --upgrade pip
#Install ldap
RUN pip install python-ldap
#Install jira
RUN pip install jira
#Install django
RUN pip install django

RUN mkdir -p /django/first/

RUN chmod -R 777 /django/first/

COPY techstop/  /django/techstop/

COPY 000-default.conf /etc/apache2/sites-available/

COPY apache2.conf /etc/apache2/

CMD ["/etc/init.d/apache2","start"]
