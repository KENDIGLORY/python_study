my_set={10,20,30,40,50}
print(type(my_set))
print(my_set)
#set methods
#.add-add elements
my_set.add(60)
print(my_set)
#.remove- to remove an existing element in a set
my_set.remove(40)
print(my_set)

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
#Remove friday and sunday from the set using methods.
days.remove("friday")
days.remove("sunday")
print(days)
#Add them back to the set
days.add("friday")
days.add("sunday")
print(days)

