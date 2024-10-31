#TASK 1: Write a program that prompts the user to enter the base and height of a 
# triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
b=float(input('enter base: '))
h=float(input('enter height: '))
a=b*h
print(a)
# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
number=float(input('enter number: '))
if number%2==0:
    print('number is even')
    if number%4==0:
      print('number divisible by 4')
else:
    print('number is odd')

# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates 
# the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or
#   1.. Convert the number to start with +254… 

phone_number=(input('enter phone number: '))
if phone_number.startswith (('07','01')):
   phone_number=phone_number[1:]
   phone_number='+254' + phone_number
   print(phone_number)
elif phone_number.startswith(('7', '1')):
   phone_number='+254' + phone_number
   print(phone_number)
   


# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email
#  by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.
email=input('enter your email: ')
if '@' in email and '.' in email:
   print('valid email')
else:
   print('invalid email')  

# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser,
#  and stores them in three variables. Return the largest of the three.
#  Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
num1=float(input('enter num1: '))
num2=float(input('enter num2: '))
num3=float(input('enter num3: '))
if num1>num2 and num1>num3:
   largest=num1
elif num2>num1 and num2>num3:
   largest=num2
else:
   largest=num3
print(f"{largest}is the largest")

# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check
#  the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.
attempts=4
correct_password="admin@123"
for i in range(attempts):
   password=input('enter your password: ')
   print(password)
# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
marks=float(input('enter marks: '))

# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.


# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
# Once you learn functions,revisit this and write this code inside a function.





# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.



