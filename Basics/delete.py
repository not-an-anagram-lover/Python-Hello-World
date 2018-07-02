z=[None]*100
n=int(input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])
a=int(input('enter number to be deleted'))
for i in range(0,n):
	if(z[i]==a):
		for j in range(i,n):
			z[j]=z[j+1]
		n-=1
print("after deletion")
for i in range(0,n):
	print(z[i])
