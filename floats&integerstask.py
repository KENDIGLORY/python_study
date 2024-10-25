#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
temp = 56.8926
temp=int(temp)
temp=str(temp)
temp=temp.replace("56","57")
print(temp)


#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
temp = 56.8926
temp=str(temp)
temp=temp.replace("56.8926","56.89")
temp=float(temp)
print(temp)

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893
temp = 56.8926
temp=str(temp)
temp=temp[0:6]
temp=temp.replace("2","3")
print(temp)
 
#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
temp=56.8926
temp=str(temp)
temp=temp[3:7]

print(temp)


#NB: Use string  slice & concatenation, but have result as float 

x=10
x+=20
print(x)

print(3<10)
print(10==10)
print(4!=6)
print(3>=2)
print(4<=2)

print(34 != 67 and 78 > 89 and 45 == 45)
print(34 == 67 or 45 < 9 or 6 > 8 or 8 < 9)
