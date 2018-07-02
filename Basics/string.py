#can type string with single double or triple quotes
"""  this should be a comment """

print("""  this shouldn't be  """)


'abcdefgh'.index('f')#different from tutorial->actually works in shell programming
#if("abcdefgh".index("f"):#still error->no idea why
	#print('yeah in if')


"jin" in "cohjinhoka"#again no output
if("jin" in "cohjinhoka"):#but this works
	print('yeah')

combined_string = " ".join(["1", "2", "3"])
print(combined_string)

print("I love %s in %s" % ("programming", "Python")) 