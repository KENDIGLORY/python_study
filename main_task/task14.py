# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only 
# or otherwise display an error “invalid character entered” 
# and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.
while True:
    try:
        input1=float(input('enter the first number: '))
        input2=float(input('enter the second number: '))
        result=input1+input2
        print(result)
        break
    except:
        print("invavid character entered") 
        