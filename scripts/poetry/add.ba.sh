#!/bin/bash

set -e
set -v

poetry self add poetry-plugin-export
poetry self add poetry-plugin-sort

set +v
set +e
