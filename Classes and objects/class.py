class A:
	def x(self,a,b):
		self.a=a
		self.b=b
		print(self.a,self.b)
		print(a,b)
	

o1=A()
o1.x(2,3)
o2=A()
o2.x(4,64)