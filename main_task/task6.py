# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check
#  the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.
attempts=4
correct_password="admin@123"
display=''
for i in range(attempts):
    password=input('enter your password: ')
    if password==correct_password:
            display='access_granted'
            break
    else:
          attempts-=1
          print(f'access_denied{attempts}attempts remaining')
    if(attempts==0):
        display='sorry! pin blocked'

        print(display)
       
