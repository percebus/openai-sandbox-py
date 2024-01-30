#!/bin/bash

SCRIPTS_PATH="$(dirname "$(readlink -f "$0")")"
echo "script path: ${SCRIPTS_PATH}"

cwd=$(pwd)
echo "[C]urrent [W]orking [D]irectory: ${cwd}"
