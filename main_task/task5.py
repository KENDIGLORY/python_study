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
