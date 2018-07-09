#!/usr/bin/python
class rectangle:
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def area(self):
         return self.breadth*self.length
a=input("enter the length of rectangle:")
b=input("enter the breadth of rectangle:")
obj=rectangle(a,b)
print("area of rectangle:",obj.area())

 
         

