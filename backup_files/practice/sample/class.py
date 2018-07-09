class employee:
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
     def displaycount(self):
         print "total employee %d" %employee.empcount
     def displayemployee(self):
         print ("name:",self.name, "salary:",self.salary) 
emp1=employee("zara",2000)
emp2=employee("mani",5000)
emp1.displayemployee()
emp2.displayemployee()

 
