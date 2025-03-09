#!/bin/bash

set -e

scripts_path="$(dirname "$(readlink -f "$0")")"
echo "Script directory: ${scripts_path}"

set -x

# pipx installs CLI executables, like poetry
bash ${scripts_path}/pipx/install.ba.sh

# poetry has its own plugins
bash ${scripts_path}/poetry/plugin/add.ba.sh

set +x
set +e
