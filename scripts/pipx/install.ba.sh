#!/bin/bash

cwd=$(pwd)
echo "[C]urrent [W]orking [D]irectory: ${cwd}"

set -e
set -v

cat ${cwd}/requirements.pipx.txt | xargs -n 1 pipx install

set +v
set +e
