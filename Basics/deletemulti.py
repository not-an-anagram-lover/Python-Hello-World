print('bubble sort')
z=[None]*100
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
a=int(input('number whose duplicates ar to be deleted'))

for i in range(0,n):
	for j in range(0,n):
		if(z[i]==a):
			for j in range(i,n):
				z[j]=z[j+1]
			n-=1
print("you printed")
for i in range(0,n):
	print(z[i])
