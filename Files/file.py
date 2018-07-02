#file object = open(file_name [, access_mode][, buffering])


x=open("file.txt","w")
x.write("wassup")
x.close()

x=open("file.txt","r")
s=x.read()
print(s)
x.close()

y=open("C:/Users/lenovo/Downloads/goal setting/neckdeep.jpg","rb")
s=y.read()
print(s)
y.close()