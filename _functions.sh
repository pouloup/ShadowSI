#!/bin/bash

# Using which is not recommended as it requires launching an external process and might give you incorrect output.
is_installed () {
    command -v "$1" > /dev/null 2>&1; res=$?
    if [ "$res" != 0 ]; then
        echo "$1 is not installed, please fix."
        exit 1
    fi
}
