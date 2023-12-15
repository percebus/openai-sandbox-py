#!/bin/bash

set -e
set -v

cat requirements.pipx.txt | xargs -n 1 pipx install

pipx inject poetry poetry-plugin-export

set +v
set +e
