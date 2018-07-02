class A:
	
	def x(self):
		print('in x')

	y=10
class B(A):
	
	def z(self):
		A.x(0)

obj=B()
B.z(0)
