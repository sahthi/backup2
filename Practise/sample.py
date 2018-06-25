class Rectangle:
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def area(self):
         return self.length*self.breadth
s=Rectangle(10,20)
print s.area()

