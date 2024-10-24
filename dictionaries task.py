my_ds=[23,"jane",(560),["lesson","math",{"currency":"KES"}],987,(76,"john")]
#print KES
print(my_ds[3][2]['currency'])
print(my_ds[2])
print(my_ds[3][1])

#add key 'amount with value 90
my_ds[3][2]['amount']=90
print(my_ds)
#reverse 987 to 789 without using method or assigning 789 manually
#first identify its index then convert to string
my_ds[4]=str(my_ds[4]) 
#reverse it
my_ds[4]=my_ds[4][::-1]
#convert back to an integer
my_ds[4]=int(my_ds[4])
print(my_ds)
#change john to jane
my_ds[5]=list(my_ds[5])
my_ds[5][1]='jane'
my_ds[5]=tuple(my_ds[5]) 
print(my_ds)



