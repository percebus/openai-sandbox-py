#!/bin/bash

set -e
set -v

# pip upgrades pip
poetry run pip install --verbose --upgrade pip

# pip upgrades pipx
poetry run pip install --verbose --upgrade --requirement requirements.upgrade.txt

set +v
set +e
