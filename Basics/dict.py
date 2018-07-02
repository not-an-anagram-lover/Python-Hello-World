alphabets={1:'a'}
print(alphabets.get(1))

#get() lets you set a default value

print(alphabets.get(2,'default'))

#print(alphabets[2])-> gives a  error

person={'city':'ooti','name':'avi','food':'pizza'}
print(person)

# del 
del person['name']
print(person)

#pop

print(person.pop('food',None))

print(person)

#has_key

#alphabets.has_key(2)-> gives error, can try in python shell

person['foo']='junk'

person['o']='ju'
print(person)