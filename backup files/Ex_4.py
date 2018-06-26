class A:
	# pass
	def abc(self):
		print("class A")

class B(A):
	pass
	# def abc(self):
	# 	print("class B")

class C(B):
	# pass
	def abc(self):
		print("class C")

class D(C):
	# pass
	def abc(self):
		print("class D")

a1 = D()
a1.abc()

