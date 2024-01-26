#!/bin/bash

set -e
set -v

cat requirements.pipx.txt | xargs -n 1 pipx install

set +v
set +e
