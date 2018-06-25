#!/bin/bash
if [-e $HOME]
then
	echo "OK on the directory,now lets check the file"
	if [-e $HOME/Dockerfile]
	then
		echo"file exists"
	else
		echo "file doesn't exist"
	fi
else
	echo "sorry,you dont have a home directory"
fi
