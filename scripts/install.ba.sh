#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

bash ${scripts_path}/prepare.ba.sh
bash _scripts/setup.ba.sh

poetry install
python -m pip install -e .

set +x
set +e
