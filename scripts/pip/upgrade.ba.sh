#!/bin/bash

set -e
set -v

# pip upgrades pip
python -m pip install --verbose --upgrade pip

# pip upgrades pipx
python -m pip install --verbose --upgrade --requirement requirements.upgrade.txt

set +v
set +e
