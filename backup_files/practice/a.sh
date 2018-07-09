#!/bin/bash
nums="1 2 3 4 5"
for num in $nums
do
	q=`expr$num % 2`
	if[ $q -eq 0 ]
	then
		echo"number is even"
		continue
	else
		echo"number is odd"
done
