person={
'name':"glory",
'age':"24",
'gender':"female",
'location':["kiambu",518,'thika'],
'address':{'street':'muthaiga',
           'city':'nairobi',
           'country':'kenya'}
}
print(type(person))
print(person)
#display name
print(person['name'])
#display age and gender
print(person['age'])
print(person['gender'])
#display 518
print(person['location'][1])
print(person['location'][2])

print(person['address']['street'])
print(person['address']['city'])
print(person['address']['country'])
#to update value
person['age']=40
person['location']='kasarani'
print(person)
#add new key and a value
person['occupation']='doctor'
print(person)

#dictionaries methods

#1.keys  - returns all the keys
print(person.keys()) 

#2.values  -returns all the values in the dictionaries
print(person.values())

#3.items -returns a list containing a key and a value
print(person.items())

#4.pop -removes the value with the specified key
person.pop('name')
#remove occupation
person.pop('occupation')
print(person)

#.get()-returns the value value with a specified key
print(person.get('address')) 