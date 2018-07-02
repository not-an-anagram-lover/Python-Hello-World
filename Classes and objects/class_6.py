class marks:
	
	def input_marks(self):

		a=[]	
		z=int(input('enter number of subjects'))
		print('enter marks of ',z,' no of subjects')
		for i in range(0,z):
			j=int(input())

			a.append(j)
		return(a)
	def mdis(self):
			a=marks.input_marks(0)
			l=len(a)
			print(l)
			for i in range(0,l):
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
		marks.mdis(0)
		library.ldis(0)

s1=student()

s1.sdis()