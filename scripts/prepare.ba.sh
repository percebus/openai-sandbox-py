#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

# Upgrades top-level dependencies, like gil
bash ${scripts_path}/pip/upgrade.ba.sh
gil clone
bash repositories/commons/scripts/prepare.ba.sh

set +x
set +e
