# #create a function to culculate the area of a triangle
# def triangle_area():
#     base=40
#     height=70
#     area=(base*height)/2
#     print(area)
# triangle_area()
# #create a function that calculates the area of a rectangle

# def rectangle_area():
#     length=6
#     width=3
#     area=length*width
#     print(area)
# rectangle_area()
    

# #def rectangle_area(length,width):
# #    area=length*width
# #    print(area)
# #rectangle_area()    

#area of a triangle usimg parameters and arguments
def area_triangle(base,height):
    area=(base*height)/2
    return(area)
area_triangle(40,70)
area_triangle(200,100)

#calculate area of a rectangle
#using parameters and arguments
def area_rectangle(a,b):
    area=a*b
    return(area)
x=area_rectangle(40,10)
x1=area_rectangle(200,40)
print(x1)



#write a function thats going to check if a number is even or odd number
def check_even_odd(num):
    if num%2==0:
        result='even number'
    else:
        result='odd number'
    return result
    
user_input=int(input('enter number: '))
value=check_even_odd(user_input)
print(value)


# #Write a program that prints the largest of 4 inputs taken in from a 
# # user. Assume that the user would not enter any two numbers which
# #  are the same.

# num1=int(input('enter number 1'))
# num2=int(input('enter number 2'))
# num3=int(input('enter number 3'))
# num4=int(input('enter number 4'))

# if num1>num2 and num1>3 and num1>4:
#     print(f'{num1}is the largest')
# elif num2>num1 and num2>3 and num2>4:
#     print(f'{num2}is the largest')
# elif num3>num1 and num3>2 and num3>4:
#     print(f'{num3}is the largest')
# else:
#     print(f'{num4}is the largest')

# def check_largest(num1,num2,num3,num4):
            
#     if num1>num2 and num1>num3 and num1>num4:
#         result=f'{num1}is the largest'
#     elif num2>num1 and num2>num3 and num2>num4:
#         result=f'{num2}is the largest'
#     elif num3>num1 and num3>num2 and num3>num4:
#         result=f'{num3}is the largest'
#     else:
#         result=f'{num4}is the largest'
#     return result


# num1=int(input('enter number 1'))
# num2=int(input('enter number 2'))
# num3=int(input('enter number 3'))
# num4=int(input('enter number 4'))
# la=check_largest(num1,num2,num3,num4)      
# print(la)                          


#task68
# #Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

maths=float(input('enter maths: '))
eng=float(input('enter eng: '))
swa=float(input('enter swa: '))
sci=float(input('enter sci: '))
sos=float(input('enter sos: '))

def calc_total_marks(m,e,swa,sc,so):
    sum=m+e+swa+sc+so
    return sum  
total_marks=calc_total_marks(maths,eng,swa,sci,sos)
print(total_marks)

#calculate average
def calculate_average(total):
    average=total/5
    return average

avg=calculate_average(total_marks)
print(avg)

# Use the value from total to get the average and average to find the grade
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
def find_grade(average):
    if average >79:
        grade='A'
    elif 60<=average<=79:
        grade='B'
    elif 50<=average<=59:
        grade='C'
    elif 40<= average <=49:
        return'D'
    else:
        return 'E'
