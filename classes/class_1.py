class A:
	def x(self):
		print('in x')

	y=10


print(A.y)
A.y=A.y+1
print(A.y)
A.x(0)