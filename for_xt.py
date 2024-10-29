fruits=['apple','banana','mangoes']
for fruit in fruits:
 if fruit=='banana':
    print(fruit)
    
   # functions
   #1 range () used to create a list of numbers
numbers=list(range(0,101))
print(numbers)

#iterate through numbers from 10 to 40
x=list(range(10,41))
for num in x:
  print(num)

  #iterate through numbers from 10 to 50 and only display even numbers
  even_num=[]
  x=list(range(10,51))
  for num in x:
    if num%2==0:
      even_num.append(num)
      print(even_num)
  