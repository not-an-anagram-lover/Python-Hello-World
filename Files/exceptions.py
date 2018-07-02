print('try ,except, finally')
print('')
try:
	x=open('exp.txt','r')
except:
	print("file doesn't exsist")
else:
	s=x.read()
	print(s)
	x.close()
print('')
