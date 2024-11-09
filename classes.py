#define a clss named car
class Car:
#constructor method
    def __init__(self,color,brand,shape):
        self.color=color
        self.brand=brand
        self.shape=shape

    def describe(self):
            return f'the color of the car is{self.color} and the brand is {self.brand} the shape is {self.shape}'
        
mycar=Car('red','BMW','wagon')
print(mycar.describe()) 
print(mycar.color)

#1.Create a class called Student with attributes name and age.
#Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
         return f'hello, my name is,{self.name} and i am {self.age} years old.'
i_am=Student('glory',24) 
print(i_am.introduce())

#2.Define a class Calculator with methods add, subtract, multiply, and divide that perform
#  the respective operations on two numbers.
#Create an object of Calculator and use it to perform some calculations.
class Calculator:
     def __init__(self,a,b):
          self.a=a
          self.b=b
     def add(self):
          sum=self.a+self.b
          return sum
     def subtract(self):
          sub=self.a-self.b
          return sub
     def multiply(self):
          mult=self.a*self.b
          return mult
     def divide(self):
          div=self.a/self.b
          return div   

calc=Calculator(20,8)   
print(calc.add()) 
print(calc.subtract()) 
print(calc.multiply())
print(calc.divide()) 
