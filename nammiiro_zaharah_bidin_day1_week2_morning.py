#classes 
class my_account:
    def __init__(self, account_number, balance, amount):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount

    def display(self):
        print(self.account_number, self.balance, self.amount)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.balance)


account1 = my_account("123272gs", 23000000, 1000000)
account1.display()
account1.deposit(2000000)
account1.withdraw(2000)
account1.display_balance()

print("=====================================================================================================================")
#Example 2 showing how to calculate area of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print(self.length*self.width)
    def parameter(self):
        print(self.length+self.width)
rectangle = Rectangle(23, 12)
rectangle.calculate_area()
rectangle.parameter()

print("=====================================================================================================================")

#Example 3 showing that am a software Engineering Student
class Student:
    def __init__(self, name, student_no, age):
        self.name = name
        self.student_no = student_no
        self.age = age
    def display(self):
        print("am a software engineering student called " , self.name ,"of student number " , self.student_no , " with an of ", self.age," years")
student=Student("Nammiiro Zaharah Bidin","2100701614",20)
student.display()

print("=====================================================================================================================")
# Exercise 1 of calculating area and circumference of a  circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        print(3.14*self.radius**2)
    def calculate_circumference(self):
        print(2*3.14*self.radius)
circle = Circle(5)
circle.calculate_area()
circle.calculate_circumference()


print("=====================================================================================================================")

#Exercise to calculate the employees bonuses  of salary for 0.15 and display them
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name , "has a salary of ", self.salary)
    def calculate_bonus(self):
        if self.salary > 50000:
            print(self.salary*0.15)
        else:
            print(self.salary)
employee1= Employee("Zaharah",150000)
employee1.display()
employee1.calculate_bonus()
employee2= Employee("Bidin",230000)
employee2.display()
employee2.calculate_bonus()



#Encapsulation 
#provides several benefits, including data protection, code organization,hiding  and modularity
#An example of a bank account using encapsulation

class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    def drive(self, distance):
        self._mileage += distance


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Access the attributes using getter methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Access and modify the mileage attribute using a method
print("Mileage:", my_car.get_mileage())
my_car.drive(100)
print("Mileage after driving:", my_car.get_mileage())

print("=====================================================================================================================")  

# encapsulation  for converting temperature  from Celsius to degrees fahrenheit EXERCISE 
class TempConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Create an instance of the TempConverter class
temp_converter = TempConverter(37)

# Get the Celsius temperature
celsius_temp = temp_converter.get_celsius()
print("Celsius Temperature:", celsius_temp)

# Convert Celsius to Fahrenheit
fahrenheit_temp = temp_converter.get_fahrenheit()
print("Fahrenheit Temperature:", fahrenheit_temp)

print("=====================================================================================================================")  

#ASSIGNMENT 
# show encapsulation with employee information to give  a pay increamentation (salary with employee information  to new employee eg from 850000 to 1000000)
class Employee:
    def __init__(self, name, employee_id, salary): #constructor
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

#getter methods
    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_salary(self):
        return self._salary

#setter method

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increment_salary(self, increment_amount):
        self._salary += increment_amount


# Create an instance of the Employee class
employee = Employee(" Nammiiro Zaharah Bidin ", "EMP001", 850000)

# Get employee information
name = employee.get_name()
employee_id = employee.get_employee_id()
salary = employee.get_salary()
print("Name:", name)
print("Employee ID:", employee_id)
print("Salary:", salary)

# Increment the salary
increment_amount = 150000
employee.increment_salary(increment_amount)

# Get the updated salary
new_salary = employee.get_salary()
print("Updated Salary:", new_salary)




