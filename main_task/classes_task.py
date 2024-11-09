# 1#.Create a class Animal with attributes species and sound.Add a method make_sound 
# #that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.
# class Animal:
#     def __init__(self,species,sound):
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         return f"the {self.species} goes {self.sound}!"
# cow=Animal('cow','moaws')
# cat=Animal('cat','meaws')   
# print(cow.make_sound())   
# print=(cat.make_sound())
     


# # 2.Create a class Book with attributes like title, author, and year.
# # Add a method that returns a description of the book.
# # Create an object of Book and print out the description.
# class Book:
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year
#     def description(self):
#         return f'the book title is{self.title},the author is {self.author}and the year is {self.year}'

# book1=Book('The breaking','kamala H',2000)
# print(book1.description())        
    



#3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).
# Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
#Ensure that the withdraw method does not allow the balance to go negative.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance=balance
    
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            return f'hello {self.owner} {amount} has been deposited.Your balance is KES{self.balance}'
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f'hello {self.owner}{amount}has been withdrawn.Your new balance is KES{self.balance}'
        else:
            return 'insufficient funds to withdraw {amount}'
    def get_balance(self):
        return f'hello {self.owner}your current balance is {self.balance}'

person1 =BankAccount('kendi')
person1.deposit(10000)
person1.withdraw(10000)
print(person1.get_balance())            
        
        
     

 


# #Define a class Rectangle with attributes width and height.
# #Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# #Instantiate a few rectangle objects and print their area and perimeter.
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
#     def perimeter(self):
#         return self.width+self.height
# rec1=Rectangle(40,60)  
# rec2=Rectangle(10,5)  
# print(rec1.area()) 
# print(rec2.perimeter())   
# print(rec2.area())