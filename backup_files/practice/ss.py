#!/usr/bin/python 
import sys 
def my_list(start=1,stop=100): 
	l1=[] 
	for num in range(start,stop): 
		hf=num/2 
		for i in range(2,hf): 
			if num%i==0:	 
				break; 
		else: 
			l1.append(num)		 
	return l1 

vals=(sys.argv[1:]) 

if len(vals)<2: 
	print my_list() 

else: 
	start=int(vals[0]) 
	stop=int(vals[1]) 
	print my_list(start,stop)


