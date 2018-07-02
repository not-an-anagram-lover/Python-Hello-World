z=[None]*100
print("taking input now")
for i in range(0,4):
	z[i]=int(input())
print("you printed")
for i in range(0,4):
	print(z[i])
print("even numbers are")
for i in range(0,4):
	if(z[i]%2==0):
		print(z[i])

print("sum of numbers in inserted list")
sum=0
for i in range(0,4):
	sum=sum+z[i]
print(sum)