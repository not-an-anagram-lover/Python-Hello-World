
"""z=[None]*100
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
x=0

print('for single digit only')

for i in range(0,n):
	r=z[i]
	x=x*10+r

print(x)


z=[None]*100
print('for double only')
x=0
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])



for i in range(0,n):
	r=z[i]
	x=x*100+r

print(x)"""




































z=[None]*100
print('for double only')
x=0
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
y=0
for i in range(0,n):
	y=0
	r=z[i]
	a=z[i]
	while(a!=0):
		y+=1
		a=a/10
		a=int(a)
	print(y)
	for i in range(0,y):
		x=x*10
	x=x+r
	
	
print(x)


