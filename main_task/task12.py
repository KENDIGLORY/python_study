# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user.
#  Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.
num1=float(input('enter num1: '))
num2=float(input('enter num2: '))
num3=float(input('enter num3: '))
num4=float(input('enter num4: '))
if num1!=num2 and num1!=num3 and num1!=num4 \
and num2!=num3 and num2!=num4 and num3!=num4:

    if num1>num2 and num1>num3 and num1>num4:
        largest=num1
    elif num2>1 and num2>num3 and num2>num4:
        largest=num2
    elif num3>num1 and num3>num2 and num3>num4:
        largest=num3
    else:
        largest=num4
    print(f'{largest}is the largest')
else:
    print('two numbers cannot be the same')        