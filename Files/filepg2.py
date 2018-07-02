f=open("filepg2.txt","w+")
n=int(input('how many numbers do you want?'))
for i in range(0,n):
	s=input()
	f.write(s)
	f.write(",")
print("")	
f.seek(0)
c=f.read()
d=c.split(",")
print(d)

max=d[0]
max=int(max)
for i in range(0,n):
	a=d[i]
	a=int(a)
	if(max<a):
		max=a

print("printing max " ,max)

f.close()
max=str(max)
f=open("filepg2-2.txt","w")
f.write(max)

