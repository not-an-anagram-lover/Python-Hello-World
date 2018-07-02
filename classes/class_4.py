class A:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		print(a,b)
	def x(self):
		print('in x')

	y=10

obj=A(33,4)

print(A.y)
A.y=A.y+1
print(A.y)
A.x(0)