#!/usr/bin/python
class myname():
	def __init__(self,end,n):
		self.end=end
		self.n=n
	def Numbers(self):
		for i in range(1,self.end):
	        	if i%self.n==0:
	        	    yield i 

if __name__=='__main__':
	end=input("Enter the range of  number :")
	n=input("Enter the divisible number :")
	c=myname(end,n)
	result=c.Numbers()
	for number in result:
		print number


