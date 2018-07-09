#!/bin/bash
sum()
{
	return ` expr $1 + $2`
}
sum 17 6
echo sum is $?
