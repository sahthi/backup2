#!/bin/bash

if [-d $HOME]
then
        echo "Home directory exists"
        cd $HOME
        ls -a
else
        echo "Home directory doesn't exist"
fi

