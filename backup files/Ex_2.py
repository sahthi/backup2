class Parent:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		print(self.name)

h = Parent('ram', 14)

# h.get_name()

class Parent_2:
	def __init__(self, job):
		self.job = job

	def get_job(self):
		print(self.job)

class Child(Parent):
	pass
b = Child("Hari", 34)

# b.get_name()

class Child_2(Parent):
	def __init__(self, name, age, gender):
		self.gender = gender
		super(Child_2, self).__init__(name, age)

	def get_gender(self):
		print(self.gender)
		super(Child_2, self).get_name()

c1 = Child_2("Ravi", 34, "M")

# c1.get_name()
# c1.get_gender()
class Child_3(Parent, Parent_2):
	def __init__(self, name, age, job, place):
		self.place = place
		# super(Child_3, self).__init__(name, age, job)
		# super(Child_3, self).__init__(job)
		Parent.__init__(self, name, age)
		Parent_2.__init__(self, job)

c3 = Child_3("Harsha", 12, "eat", "plvd")

c3.get_job()
c3.get_name()
