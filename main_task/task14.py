# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only 
# or otherwise display an error “invalid character entered” 
# and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.

value_a=input("enter first number: ")
value_b=input("enter second number: ")
sum=(value_a) + (value_b)
if value_a==int() or float() and value_b==float() or int():
    print("acccept input")
else:
    print("invalid character entered")
    
print(sum)