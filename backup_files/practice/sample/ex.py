#!/usr/bin/python
class Numbers:
     multiplier = 5

     def __init__(self,v1,v2):
          self.v1=v1
          self.v2=v2

     def add(self):
          return self.v1+self.v2

     def multiply(self,val):
	  return Numbers.multiplier*val

     @staticmethod
     def substract(v1,v2):
	  return v1-v2

     @property
     def value(self):
         return self.v1, self.v2

     @value.setter
     def value(self,v1, v2):
	  self.v1=v1
	  self.v2 = v2
	
ob = Numbers(2,3)
print ob.multiply(4)
print ob.add()
print Numbers.substract(6,3)
print ob.value
print ob.v1
ob.value = 6
print ob.v1
