p=int(input("enter a number"))
a=p
rem=0
rev=0

while(p!=0):
	rem=p%10
	rem=int(rem)
	rev=rev*10+rem
	rev=int(rev)
	p=p/10
	p=int(p)
print(rev)
if(rev==a):
	print ("pallindrome")
else:
	print("not a palindrome")