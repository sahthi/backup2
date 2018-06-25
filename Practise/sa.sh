#!/bin/bash
for command in date pwd df
do 
	echo "the output of $command command"
        $command
done


