#!/usr/bin/python

var1 = int(input("Enter a number to find out num is both a prime and a fibonacci number: "))

a = 1
b = 1
lst = []

for val in range(2, var1):
	if var1 % val == 0:
		print("Number {} is not Fibonacci-Prime".format(var1))
		break
else:
	while a <= var1:
		lst.append(a)
		a, b = b, a + b

	if var1 in lst:
		print("Number {} is Fibonacci-Prime".format(var1))

