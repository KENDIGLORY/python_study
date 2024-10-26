#if statement

if 20>30:
    print("This is true")
else:
    print('this is false')

    #declare a variable marks and checkif the marks is above 50 print pass otherwise print fail
    marks=70
    if 70>50:
        print('pass')
    else:
        print('fail')
        #declare variable num check if the number is even or odd
        num=11
        if num%2==0:
            print('even')
        else:
            print('odd')

#grading system 
#taking marks from input
marks=int(input('enter marks: '))

if marks>=80 and marks<=100:
    print('A')
elif marks>=70 and marks<80:
    print('B')
elif marks>=60 and marks<70:
    print('C')
elif marks>=50 and marks<60:
    print('D')
else: 
    print('E')

#check if the age from input s greater then 60 print you are old if the age is above 18 and less than 60 print you are an adult
#otherwise print you are a child
age=int(input('enter your marks: '))
if age>=60:
    print('you are old')
elif age>=18 and age<60:
    print('you are an adult')
else:
    print('you are a child')

#task1
# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive

age=int(input('enter your age: '))
if age>18:
    licence=input('do you have a driving licence yes/no: ')
    if licence=='yes':
        print('eligible to drive')
    else:
        print('dot eligible to drive')
else:
    print('too young to drive')



#task2
# Write a program that:
# =>Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low

#Write a program that:
#Takes the user's credit score and annual income as input.
creditscore=float(input('credit score: '))
income=float(input('annual income: '))
#If the credit score is above 700, check if the income is above 50,000:
if creditscore>700:
    if income>50000:
        print('loan approved')
    else:
        print('income requirement not met')
#If the credit score is below 700, print "Credit score too low
else:
    print('credit score too low')
    






