class shape:
     def __init__(self,n):
         self.n=n
     def print_sides(self):
         print('There are'+str(self.n)+'sides')
class Square(shape):
     def __init__(self,length):
         self.length=length
     def getarea(self):
         return self.length*self.length
class Rectangle(Square):
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def area(self):
         return self.length*self.breadth
t=Rectangle(5,3)
print t.getarea()
print t.area()

     
