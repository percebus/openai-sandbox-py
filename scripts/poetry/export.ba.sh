#!/bin/bash

set -e
set -v

POETRY_EXPORT_CLI_ARGS='--no-interaction --format requirements.txt'
poetry export ${POETRY_EXPORT_CLI_ARGS} --output requirements.prd.txt
poetry export ${POETRY_EXPORT_CLI_ARGS} --output requirements.dev.txt --with dev

set +v
set +e
