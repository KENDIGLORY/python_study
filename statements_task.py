   
#slide 55 NESTED IF TASK
# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."

trancsaction_amount=float(input('enter amount: '))
account_type=(input('enter acount type standard/premium')).lower().strip()
if  account_type=='standard':
    if trancsaction_amount>500:
        print('transaction exceeds the limit for standard accounts')
    else:
        print('transaction approved')
elif account_type=='premium':
    if trancsaction_amount>1000:
        print('Transaction exceeds the limit for Premium accounts')
    else:
        print('transaction approved')
else:
    print('invalid account type')


#slide 54 IF STATEMENT TASK
#Take three inputs from a user, separately. Print the largest of the numbers.print the largest of numbers
#Hint: Determine what type of data is taken in as input.
num1=float(input('enter num1: '))
num2=float(input('enter num2: ')) 
num3=float(input('enter num3: '))

#Determine the largest
#print the largest
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
else:
    largest=num3
print(f'{largest} is the largest')

#1 max function gives us the largest of the numbers given
#2 formated string used to pass variables inside strings
#eg name=glory
#   age=24
#   print(f'my name is{name} and my age is{age}')
#max function
#largest=max(num1,num2.num3)
#print(f'the largest number is{kargest}')


# 2.Take as input from a user the temperature
# if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=float(input('enter temp: '))
if temp>30:
    print('temp is too high')
elif temp>15:
    print('Normal temperature')
else:
    print('Cold temperature')

# 3Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met",
#  otherwise print "Conditions not met"
marks=float(input('enter marks: '))
score=float(input('enter score: '))
if marks>10 and marks<=20 and score>100:
    print('Conditions met')
else:
    print('conditions not met')

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input('enter password: ')
correct_password='glo1234'
if password==correct_password: 
    print('access granted')
else:
    print('access denied')

# 5. Write a Python program that checks if a variable student_score is greater than 90.
# If true, check if the attendance is greater than 80. \
# If both conditions are true, print "Excellent student", 
# otherwise print "Good score, but attendance needs improvement"
student_score=float(input('enter score: '))
attendance=int(input('enter attendance: '))
if student_score>90 and attendance>80:
    print('Excellent student')
else:
    print("Good score, but attendance needs improvement")
