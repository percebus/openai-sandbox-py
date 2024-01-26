#!/bin/bash

npx prettier --check .

python -m ruff .

python -m pyright src
python -m pylint src
