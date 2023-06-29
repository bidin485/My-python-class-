#functions ,arguments and parameters
# functions 
def my_function():
    print("Hello, good afternoon!")
print("===================================================================================================")

#calling a function
my_function()

#functions with parameters
def my_function(a,b):
    print(a+b)

print("===================================================================================================")
my_function(2,3)

#functions with default parameters
def my_function(a,b=10):
    print(a+b)
print("===================================================================================================")

my_function(2,3)

#functions with return values
def my_function(a,b=10):
    return a+b

print(my_function(2,3))# arguments are what is passed in  the function

#functions with multiple return values  
def my_function(a,b=10):
    return a+b,a-b

print(my_function(2,3))

#function that takes in more arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))

#Modules in python
# This code is going to be called in  product.py
def greet(name):
    print("Hello,", name)

def calculate_square(x):
    return x ** 2

#determining the square roots and factorial in the module math (which is a standard library module)
#import math
# from math import *(this imports all the modules in the library)

print("===================================================================================================")
"""import math
print(math.sqrt(9))
print(math.factorial(5))"""
#Using alias
import math as mtc

print(mtc.sqrt(16)) 
print(mtc.factorial(5))    

print("===================================================================================================")
 # input and output in python
name = input("Enter your name: ")
print("Hello, " + name)

 
 #input
 
print(input("Enter your name: "))
  
 #output
 
print("Hello,", input("Enter your name: "))
 
 # Multiple inputs in python
data = input("Enter name and age : ")
name, age = data.split()

print("Name:", name)
print("Age:", age)

 #or
"""name, age = map(str, input("Enter your name and age : ").split())

print("Name:", name)
print("Age:", age)"""



#Capturing input in a tuple 
my_tuple=(1,2,3,4)
print(type(my_tuple))
print(my_tuple)
my_list=list(my_tuple)
my_list.append (int(input("Enter any integer of your choice:")))
new_tuple=tuple(my_list)
print(new_tuple)

#capturing input in a set
my_set={"zaharah","bidin"}
print(type(my_set))
print(my_set)
my_list1=list(my_set)
my_list1.append (input("Enter any other name  of your choice:"))
new_set=set(my_list1)
print(new_set)


 


