my__dict={}

my__dict={1:'apple',2:'ball'}

my__dict={'name':'Pranjala',1:[2,4,3,7]}

my__dict={'name':'Kaneera','age':'12','grade':'5','Roll number':'30'}

print(my__dict['name'])
print(my__dict.get('age'))

my__dict['age']=12
print(my__dict)

my__dict.pop('age')
print(my__dict)

print("name:",my__dict.get('name'))

my__dict.clear()
print(my__dict)
