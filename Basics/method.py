"""def star():
	print('*')
	print('*',end='')
	print('*',end='')

star()"""







def sum(x):
	sum1=0
	for i in range(0,n):
		sum1+=x[i]
	return(sum1)

z=[None]*100

x=0
n=int (input('enter size'))
print("taking input now")
for i in range(0,n):
	z[i]=int(input())
print("you printed")
for i in range(0,n):
	print(z[i])

print('')
a=sum(z)
print(a)


