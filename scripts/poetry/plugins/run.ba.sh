#!/bin/bash

cwd=$(pwd)
echo "[C]urrent [W]orking [D]irectory: ${cwd}"

set -e
set -v

poetry sort

POETRY_EXPORT_CLI_ARGS='--no-interaction --format requirements.txt'
poetry export ${POETRY_EXPORT_CLI_ARGS} --output ${cwd}/requirements.prd.txt
poetry export ${POETRY_EXPORT_CLI_ARGS} --output ${cwd}/requirements.dev.txt --with dev

set +v
set +e
