#!/bin/bash

SCRIPTS_PATH="$(dirname "$(readlink -f "$0")")"
echo "cwd: ${SCRIPTS_PATH}"

set -e
set -v

npx prettier --write .

python -m ruff --fix .
python -m ruff format .

bash ${SCRIPTS_PATH}/lint.ba.sh

set +v
set +e
