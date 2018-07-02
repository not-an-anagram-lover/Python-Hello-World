class marks:
	
	def input_marks(z):

		a=[None]*100	
		
		print('enter marks of ',z,' no of subjects')
		for i in range(0,z):
			j=int(input())

			a[i]=j
		return(a)
	def mdis(self,z):
			a=marks.input_marks(z)
			l=len(a)
			print(l)
			for i in range(0,z):
				print(a[i])
class library:
	s=0
	
	def input_library(self):
		s=int(input('enter no of books issued on this student'))
		return(s)
	def ldis(self):
		s=library.input_library(0)
		print('no of books issued on this student',s)
		


class student(marks,library):
	
	
		
	def sdis(self):
		print('student has')
		z=int(input('enter number of subjects'))
		marks.mdis(0,z)
		library.ldis(0)

s1=student()

s1.sdis()