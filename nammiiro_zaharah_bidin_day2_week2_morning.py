#inheritance
class Animal:
    def __init__(self, name,sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print("I ",self.name,"i make " ,self.sound,"sound")
#object
animal=Animal("cat","mew")
animal.speak()

#child class
class Dog(Animal):
    def speak(self):
        print("I ",self.name,"i make " ,self.sound,"sound")
dog=Dog("dog","woof")
dog.speak()

#child class 2
class Donkey(Animal):
    pass
donkey=Donkey("donkey","crew crew")
donkey.speak()
print("=============================================================")

#exercise (calculate area and a parameter of a circle and a rectangle using inheritance)
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)



circle = Circle(5)
print("Circle area:", circle.calculate_area())
print("Circle perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.calculate_area())
print("Rectangle perimeter:", rectangle.calculate_perimeter())
print("================================================================")
#Multiple inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"is eating")
class Flyable:
    def fly(self):
        print(self.name,"is flying")
class Eagle(Animal,Flyable):
    def __init__(self, name):
        super().__init__(name)


eagle = Eagle("Bald Eagle")
eagle.eat()
eagle.fly()

print("================================================================")

#Overriding concept in python(method inheritance)
class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")



animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

print("=================================================================")

#polymorphism(allows )
#we shall use method overriding (occurs when a derived class(child) provides its own implementation of a method that is defined in its base class(super class)) 
#overloading(allows you to have multiple methods in a class with the same name but different parameters )
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
    def display_info(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        return f"Rectangle with length {self.length} and width {self.width}"


#invoking the methods
circle = Circle(5)
rectangle = Rectangle(4, 6)
shapes = [circle, rectangle]

for shape in shapes:
    print(shape.display_info())
    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())
    print()

print("=================================================================")

#the above example has used overriding
#below is an example of implementing polymorphism using overloading
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calculator = Calculator()

print("Sum of 2 numbers:", calculator.add(5, 3,9))
print("Sum of 3 numbers:", calculator.add(2, 4, 6))

print("=================================================================")

#Abstraction concept ( a concept that focuses on hiding the internal details and complexities of an object or class, and exposing only the essential features or behaviors to the outside world)

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def display_info(self):
        print(f"{self.name} is an animal.")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

 
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.display_info()
dog.make_sound()

cat.display_info()
cat.make_sound()

print("=================================================================")
#demo abstraction using calculating area and parameter of a circle and rectangle

#abstract methods should be implemented (If not implemented , an error will be arose)
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Usage example:
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle:")
print("Area:", circle.calculate_area())
print("Perimeter:", circle.calculate_perimeter())
print()

print("Rectangle:")
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())

print("=================================================================")

#ASSIGNMENT FOR A RECEIPT PRINTING PROGRAM USING A GUI 
from tkinter import *

def print_receipt():
    # Get input values
    customer_name = name_entry.get()
    product_name = product_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    total = quantity * price

    # Create a receipt string
    receipt = f"Customer Name: {customer_name}\n"
    receipt += f"Product: {product_name}\n"
    receipt += f"Quantity: {quantity}\n"
    receipt += f"Price: ${price:.2f}\n"
    receipt += f"Total: ${total:.2f}"

    # Display the receipt
    receipt_label.config(text=receipt)

root = Tk()
root.title("Receipt Printer")

root.geometry("500x500")

# Create input fields
name_label = Label(root, text="Customer Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

product_label = Label(root, text="Product Name:")
product_label.pack()
product_entry = Entry(root)
product_entry.pack()

quantity_label = Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()

price_label = Label(root, text="Price:")
price_label.pack()
price_entry = Entry(root)
price_entry.pack()

# Create a button to print the receipt
print_button = Button(root, text="Print Receipt", command=print_receipt)
print_button.pack()

# Create a label to display the receipt
receipt_label = Label(root, text="")
receipt_label.pack()

root.mainloop()
