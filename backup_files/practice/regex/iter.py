#!/usr/bin/python 
l1=[1,2,3,4] 
l2=[] 
# l2=[i*2 for i in l1] 
# index=iter(l1) 
itr=iter(l1) 
while True: 
	try : 
		temp= itr.next() 
		value=temp*2 
		l2.append(value) 
	except: 
		StopIteration 
		break; 
print l2

