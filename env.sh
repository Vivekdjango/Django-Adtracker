#!/bin/bash

set -e

/opt/inmobi/commons/mustache-util/render-template \
  --addenvvars True \
  --template techtop/techstop/tech_template/settings.py.template \
  --output techstop/techstop/settings.py
  
/opt/inmobi/commons/mustache-util/render-template \
  --addenvvars True \
  --template techtop/techstop/tech_template/views.py.template \
  --output techstop/tech/views.py
  
  
/etc/init.d/apache2 start
