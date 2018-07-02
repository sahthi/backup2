class rectangle():
     def __init__(self,length,breadth):
           self.length=length
           self.breadth=breadth
     def area(self):
           return self.breadth*self.length
a=input("enter len:")
b=input("enter breadth:")
obj=rectangle(a,b)
print("area of rect:",obj.area())

