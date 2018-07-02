print('try ,finally')
try:
	x=open('exp1.txt','r')
finally:
	y=open('exp1.txt','w')
	y.write("wassup")
	print('finally')
	y.close()