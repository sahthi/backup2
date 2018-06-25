#!/usr/bin/python
def prime_num(inp):
	for val in range(2,(inp/2)+1):
		if (inp%val==0):
			print "%d is not a prime number"%inp
			break
	else:
		print "%d is prime number"%inp

inp=input("enter the input number:")
prime_num(inp)
