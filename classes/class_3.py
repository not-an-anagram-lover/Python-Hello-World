x=0
y=0
z=0
m=[None]*100
w=[None]*100
c=[None]*100
class Ppp:
	
	x=0
	def tp(m,w,c):
		sum1=0
		for i in range(0,x):
			sum1=sum1+m[i]+w[i]+c[i]
			
		print(sum1,'is the total population overall')
	def tmp(m):
		sum2=0
		for i in range(0,x):
			sum2=sum2+m[i]
			
		print(sum2,'is the total population men')
	def hmp(m):
		max=m[0]
		for i in range(0,x):
			if(max<m[i]):
				max=m[i]
		print(max,'is the highest population men')
	def lwp(w):
		low=w[0]
		for i in range(0,x):
			if(low>w[i]):
				low=w[i]
		print(low,'is the lowest women population')
	def lcp(c):
		low=c[0]
		for i in range(0,x):
			if(low>c[i]):
				low=c[i]
		print(low,'is the lowest children population')
	def main(self):
		x=int(input('enter no of districts'))
		print('enter men population')
		for i in range(0,x):
			m[i]=int(input())
		print('enter women population')
		for i in range(0,x):
			w[i]=int(input())
		print('enter children population')
		for i in range(0,x):
			c[i]=int(input())
		


		print('main menu')
		print('1.total population')		
		print('2.total men population')
		print('3.highest men population')
		print('4.lowest women population')
		print('5.lowest children population')

		ch=int(input('enter choice'))
		s=ch
		while((s>0)&(s<6)):
			if(s==1):
				Ppp.tp(m,w,c)
			elif(s==2):
				Ppp.tmp(m)
			elif(s==3):
				Ppp.hmp(m)
			elif(s==4):
				Ppp.lwp(w)
			elif(s==5):
				Ppp.lcp(c)
			s=int(input('enter 6 or more to exit otherwise continue'))
	

a=Ppp()
a.main()

