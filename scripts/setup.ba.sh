#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x


# Upgrades top-level dependencies, like pipx
bash ${scripts_path}/pip/upgrade.ba.sh

# pipx installs CLI executables, like poetry
bash ${scripts_path}/pipx/install.ba.sh

# poetry has its own plugins
bash ${scripts_path}/poetry/plugin/add.ba.sh

set +x
set +e
