#TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.

marks=float(input('enter marks: '))
output = ''
if marks>0 and marks<100:
        if(marks>79):
              output = 'Grade: A'
        elif(marks>=60 and marks<79):
              output= 'Grade: B'
        elif(marks>=49 and marks<=59):
              output = 'Grade: C'
        elif(marks>=40 and marks<=49):
              output = 'Grade: D'
        else:
              output = 'E'        
else:
    output = 'Invalid Marks'

print(output)