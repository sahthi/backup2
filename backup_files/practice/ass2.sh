#!/usr/bin/bash
if [ -d "$@" ]
then
find "$@" type -f | ls -l "$@" | wc -l | echo "number of files is: $@"
find "$@" type -d | ls -l "$@" | wc -l | echo"number of directories is : $@"
fi
