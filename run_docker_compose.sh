#!/bin/bash

set -e

for directory in "$PWD"/*; do
  if [ -d "$directory" ]; then
    pushd "$directory" || return
    echo "Running docker-compose in $directory"
    docker-compose up -d
    popd || return
  fi
done
