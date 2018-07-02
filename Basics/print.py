print("5"*3)
print("x","y","z")
print("it is a beautiful day")
print("love",43,98.08)
print("love",43,98.08,sep=',',end='--\n')
print("love",43,98.08,end=':')


print("")

for y in "python":
  
  print(y)
  print(y,end=':')


print("")
for y in "python":
	print(y,end=':')
print("")
print("About assignment")
string={"she":"has issues","he":"has his too"}
print(string)


arg=23
print("")
print("example calculation 23*54=",arg*54)




#doubt in this->https://stackoverflow.com/questions/16417986/function-range-in-python-language-does-not-give-the-expected-result/16418143?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""In python 3, range() returns a generator, that's why it shows you the object rather than the values:

>>> print(range(10))
range(0, 10)
If you were expecting a list, you will need to convert it to one before printing it:

>>> print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Generators only create one value at a time in order to save memory. You can read up on them here, which includes an example suited to your test case."""


print("")
print("About range")
print(range(3))

print('and that is why')
print(list(range(10)))
#

a,b,c=range(3)
print(a)
print(b)
print(c)

#using isinstance() and type()

