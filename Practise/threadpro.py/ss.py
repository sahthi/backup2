#!usr/bin/python
import re
f0=open("employee.txt")
f1=f0.readlines()
print (f1)

inp=raw_input("Enter the name :")
for i in f1:
	if inp in i:
		print i.split(":")[1]

