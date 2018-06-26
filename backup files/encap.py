class A:
	def __init__(self, name, age):
		self.__name = name
		self._age = age

	def get_name(self):
		print(self.__name)

	def get_age(self):
		print(self._age)

	def __hell(self):
		print("Welcome vt")

a1 = A("Moshe", 22)
a1.get_name()
# a1.name = "jdklafj"
a1._A__name = "fasjfkl"
a1.get_name()
print(a1._age)
a1._age = 76
print(a1._age)

print(a1._A__name)

a1._A__hell()

def greet(name = None):
    if name:
        return "Hello {}".format(name)
    return "Hello"
    
    
print(greet())
print(greet("vinay"))