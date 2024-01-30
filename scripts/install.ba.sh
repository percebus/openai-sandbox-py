#!/bin/bash

parent_dir="$(dirname "$(readlink -f "$0")")"
echo "Parent directory: ${parent_dir}"

set -e
set -v

bash ${parent_dir}/pip/install.ba.sh
bash ${parent_dir}/pipx/install.ba.sh

set +v
set +e
