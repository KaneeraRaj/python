my__dict={}

my__dict={1:'apple',2:'ball'}

my__dict={'name':'John',1:[2,4,3,7]}

my__dict={'name':'Jack','age':26}

print(my__dict['name'])
print(my__dict.get('age'))

my__dict['age']=27
print(my__dict)

my__dict['address']='Downtown'
print(my__dict)

my__dict.pop('age')
print(my__dict)

print("Address:",my__dict.get('address'))

my__dict.clear()
print(my__dict)