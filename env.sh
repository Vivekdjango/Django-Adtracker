#!/bin/bash

set -e

/opt/inmobi/commons/mustache-util/render-template \
  --addenvvars True \
  --template /var/www/techstop/techstop/tech_template/settings.py.template \
  --output /var/www/techstop/techstop/settings.py

/opt/inmobi/commons/mustache-util/render-template \
  --addenvvars True \
  --template /var/www/techstop/techstop/tech_template/views.py.template \
  --output /var/www/techstop/tech/views.py


source /etc/apache2/envvars; /usr/sbin/apache2 -DFOREGROUND


