#!/bin/bash

set -e

render-template \
  --addenvvars True \
  --template techtop/techstop/tech_template/settings.py.template \
  --output techstop/techstop/settings.py
  
render-template \
  --addenvvars True \
  --template techtop/techstop/tech_template/views.py.template \
  --output techstop/tech/views.py
  
  
/etc/init.d/apache2 start
