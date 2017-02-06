#!/bin/bash

set -e

render-template \
  --addenvvars True \
  --template pass.template \
  --output techstop/techstop/settings.py
  
render-template \
  --addenvvars True \
  --template pass.template \
  --output techstop/tech/views.py
  
