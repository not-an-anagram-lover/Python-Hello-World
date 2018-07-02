#https://stackoverflow.com/questions/699866/python-int-to-binary?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


"""a=int(input('enter a number'))
print(a)
a=bin(a)
print(a)"""



b=int(input('enter another'))
x=format(b,'b')#not working
print(x)
x=int(x)
g=x
sum=0
while(x!=0):
	r=x%10
	r=int(r)
	sum+=r
	x=x/10
	x=int(x)

print(sum)
flag=0
print('now checking if prime or not')
k=sum/2
k=int(k)
for i in range(2,k+1 ):
	if(sum%i==0):
		print('not pernicious')
		flag=1
if(flag==0):
	print('pernicious')