print('bubble sort')
z=[None]*100
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
print('now sorting')

for i in range(0,n):
	for j in range(i+1,n):
		if(z[j]<z[i]):
			temp=z[j]
			z[j]=z[i]
			z[i]=temp


for i in range(0,n):
	print(z[i])


print('selection sort')
z=[None]*100
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
print('now sorting')

for i in range(0,n):
	s=i
	for j in range(i+1,n):
		if(z[j]<z[s]):
			s=j
	if(s!=i):
		temp=z[s]
		z[s]=z[i]
		z[i]=temp

for i in range(0,n):
	print(z[i])