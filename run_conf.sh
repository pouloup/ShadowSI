#!/bin/bash

set -e

if [ -f _functions.sh ]; then
    source _functions.sh
fi

is_installed python3
is_installed docker
is_installed docker-compose

python3 apply_conf.py
