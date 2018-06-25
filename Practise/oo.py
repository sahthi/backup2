class Employee:

    def __init__(self,first,last,sal):
          self.fname=first
          self.lname=last
          self.sal=sal
          self.email=first+'.'+last+'@company.com'

    def fullname(self):
          return '{}{}'.format(self.fname,self.lname)

emp1=Employee("pinky","chohari",10000)
emp2=Employee("dinky","bihari",5000000)
print emp1.fname
print emp2.lname
	
