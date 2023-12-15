#!/bin/bash

set -e
set -v

python -m pip install --upgrade -v -r requirements.upgrade.txt
python -m pip install -v -r requirements.txt

set +v
set +e
