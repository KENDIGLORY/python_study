# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".
start_date='2024-01-01'
end_date='2024-12-31'
if start_date<end_date:
   print('valid period')
else:
   print('invalid period')
if start_date==end_date:
   print('One_day period')





# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
str1='beginning'
str2='between'
if len(str1)> len(str2):
   longer=str1
else:
   longer=str2

print(f'{longer} is longer')

   
     