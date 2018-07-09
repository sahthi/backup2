class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def showName(self):
         print (self.name)
     def showAge(self):
         print (self.age)
class Student:
     def __init__(self,Id):
         self.StudentId=Id
     def getId(self):
         print(self.Id)
class Resident(Person,Student):
     def __init__(self,name,age,Id):
         Person.__init__(self,name,age)
         Student.__init__(self,Id)
r=Resident('john',30,102)
r.showName()
print (r.getId())

         


