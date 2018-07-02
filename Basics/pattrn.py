print(1)
for i in range(0,5):
	print("")
	for j in range(0,5):
		print("* ",end='')
print("")
print(2)
for i in range(0,5):
	print("")
	for j in range(0,i+1):
		print("*",end=' ')
print("")
print(3)
for i in range (0,5):
	print("")
	for j in range (5,i,-1):
		print("* ",end='')

print("")
print(4)

for i in range (5,0,-1):
	print("")#for next line
	for j in range(0,i):
		print(" ",end=' ')
	for k in range(0,5-i+1):
		print("*",end='   ')

print("")
print(5.1)


for i in range (5,0,-1):
	
	for j in range(0,i):
		print(" ",end=' ')#for decreasing spaces
	print("*")
	print("")#for next line

print("")
print(5.2)


for i in range (0,5):
	
	for j in range(0,i):
		print(" ",end=' ')#for decreasing spaces
	print("*")
	print("")#for next line
	
print("")
print(5.3)

for i in range(5,0,-1):
	for j in range(0,i):
		print(" ",end='')
	for k in range(0,5):
		if(k==3):
			print("*"*4)
		else:
			for l in range(0,5-i):
				print("",end='')
	print("")#for next line


print("")
print(6)
for a in range(0,8):
	print("",end=' ')
print("*")

for i in range(3,1,-1):
	for j in range(0,i):
		print(" ",end=' ')
	print("*",end='')
	for k in range(0,4-i):
		print("  ",end='  ')
	print("*")
	
print("  ",end='')
for b in range(0,4):
	print("*  ",end=' ')
print("")
print("*",end='')
for b in range(0,7):
	print(" ",end=' ')
print(" *")













print("")
print(7)
for i in range(0,4):
	print(' ',end='')
print('*')
for i in range(0,2):
	print(' ',end='')
print('*',end='')
for i in range(0,3):
	print(' ',end='')
print('*')


print(' ',end='')

for i in range(0,3):
	print('* ',end=' ')
print("")
for j in range(0,2):
	for i in range(0,4):
		print(' ',end='')
	print("*")
	
print(' ',end='')

for i in range(0,3):
	print('* ',end=' ')
for i in range(0,2):
	print(' ',end='')

















