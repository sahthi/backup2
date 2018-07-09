#!/usr/bin/python
f0=open("Test_fiel.txt","a+")
inp=input("Enter the text ")
while inp!="end":	
	
	f0.write(inp)
	inp=input("Enter the text :")
	

else:
	f0.close()
	f1=open("Test_fiel.txt","r")
	f1=f1.read()
	print f1

f0.close()
