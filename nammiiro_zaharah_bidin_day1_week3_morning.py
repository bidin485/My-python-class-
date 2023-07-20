#Regular expressions
#examples of regular expressions and how they are used in python 
"""


"""
#MATCHING AND SEARCHING
""" re.match
    re.search
    re.findall
"""
#example 1
#match all numbers, match all characters, match group numbers, match last character,match first character
import re  # Importing the re module for regular expressions

text = "Hello, world! 123"

# Search for a specific pattern
pattern1 = r"world"
match1 = re.search(pattern1, text)  # Find the first occurrence of "world" in the text
print(match1)
print("=============================================================================")

# Search for a pattern at the beginning of the string
pattern2 = r"^Hello"
match2 = re.search(pattern2, text)  # Find the pattern "Hello" at the start of the text
print(match2)
print("=============================================================================")

# Search for a pattern at the end of the string
pattern3 = r"123$"
match3 = re.search(pattern3, text)  # Find the pattern "123" at the end of the text
print(match3)
print("=============================================================================")


# Search for multiple occurrences of a pattern
pattern4 = r"l"  # Match all occurrences of the letter "l"
matches4 = re.findall(pattern4, text)  # Find all "l" occurrences in the text
print(matches4)
print("=============================================================================")

# Split the text using a pattern
pattern5 = r",\s"  # Match a comma followed by a space
parts5 = re.split(pattern5, text)  # Split the text into parts using the pattern
print(pattern5) 
print("=============================================================================")

# Replace a pattern with a specified string
pattern6 = r"o"  # Match the letter "o"
replacement6 = "X"  # Replace the letter "o" with "X"
new_text6 = re.sub(pattern6, replacement6, text)  # Replace all "o" occurrences in the text
print(text)
print("=============================================================================")

# Find patterns using character classes
pattern7 = r"[0-9]"  # Match any digit
matches7 = re.findall(pattern7, text)  # Find all digits in the text
print(matches7)
print("=============================================================================")

# Match patterns with quantifiers
pattern8 = r"o+"  # Match one or more occurrences of the letter "o"
matches8 = re.findall(pattern8, text)  # Find all sequences of one or more "o" occurrences
print(matches8)
print("=============================================================================")

# Match patterns using groups and capturing
pattern9 = r"(l+),\s(w+)"  # Match a sequence of "l" characters followed by a comma and a space, and then a sequence of "w" characters
match9 = re.search(pattern9, text)  # Find the pattern with captured groups
print(match9)
print("=============================================================================")

# Match patterns using lookahead assertions
pattern10 = r"\b\w+(?=,)"  # Match word characters followed by a comma (without including the comma in the match)
matches10 = re.findall(pattern10, text)  # Find all words followed by a comma in the text
print(matches10)
print("=============================================================================")

# Match patterns using lookbehind assertions
pattern11 = r"(?<=Hello, )\w+"  # Match word characters preceded by "Hello, " (without including "Hello, " in the match)
matches11 = re.findall(pattern11, text)  # Find all words preceded by "Hello, " in the text
print(matches11)
print("=============================================================================")

#simple example
pattern = r"abc"  # raw string literal to avoid escaping backslashes
text = "abcdefg"
match = re.search(pattern, text)
if match:
    print("Pattern found!")
else:
    print("Pattern not found.")

print("=============================================================================")

#validate email example
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
text = "zaharabidin485@gmail.com"
match = re.search(pattern, text)
if match:
    print("Pattern found!")
else:
    print("Pattern not found.")
print("=============================================================================")
# example 2 


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Test the function with example email addresses
emails = ["example.email@gmail.com", "invalid.email", "another@example"]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is an invalid email address.")

#Generators and iterators
#An iterator is an object that represents a stream of data and allows you to traverse through it sequentially
#iterator methods used
#__next__()
#__iter__()
print("================================================================")

class NumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

#invoking the function
numbers = NumberIterator(5)
for num in numbers:
    print(num)
print("================================================================")


#Generators  are  used to define a function that generates a sequence of values
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#invoking the function by assigning to a variable   fibonacci
fibonacci = fibonacci_generator()
for i in range(10):
    print(next(fibonacci))
print("================================================================")

#An example of generators using factorial
def factorial_generator():
    n = 1
    result = 1
    while True:
        yield result
        n += 1
        result *= n

# Usage:
factorials = factorial_generator()
for i in range(10):
    print(next(factorials))

print("================================================================")

#An example of a generator finding the square of numbers
def square_generator():
    n = 1
    while True:
        yield n ** 2
        n += 1

# Usage:
squares = square_generator()
for i in range(10):
    print(next(squares))

print("================================================================")

#An example of a generator finding the cube of numbers
def cube_generator():
    n = 1
    while True:
        yield n ** 3
        n += 1

# Usage:
cubes = cube_generator()
for i in range(10):
    print(next(cubes))

print("================================================================")

#Decorators are a way to modify or enhance the functionality of a function or a class without directly modifying its source code
def uppercase_decorator(func):
    def modified_func(text):
        modified_text = text.upper()
        return func(modified_text)
    return modified_func

@uppercase_decorator
def greet(name): # type: ignore
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
print("================================================================")

#Simple example
def my_decorator(func):
    def inner():
        print("hello y'all")
        func()
    return inner()

@my_decorator
def my_function():
    print("am confused")
print("====================================================================")

#An example with a class 
class SayHelloDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Hello!")
        self.func()

@SayHelloDecorator
def greet():
    print("Welcome!")
greet()

#assignment for multiprocessing and multithreading functions
#Context Manager
"""
A context manager is a Python object that defines the methods __enter__() and __exit__() to enable the use of the with statement
. It allows you to allocate and release resources automatically before and after a block of code executes.
"""
class CustomContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Usage example
with CustomContextManager():
    print("Inside the context")

#Execution time using a context manager
print("=====================================================================================================")
import time

class TimeSeriesContextManager:
    def __enter__(self):
        # Start of the context
        print("Starting context")
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        # End of the context
        end_time = time.time()
        execution_time = end_time - self.start_time
        print("Ending context")
        print(f"Execution time: {execution_time} seconds")

# Usage example
with TimeSeriesContextManager():
       print("Time series operation completed")


#the use of the parameter passed in the exit method of the context manager
"""
def __exit__(self, exc_type, exc_value, traceback):
    if exc_type is not None:
        # Exception occurred within the context
        print(f"An exception of type {exc_type} occurred: {exc_value}")
        # Handle the exception 

    end_time = time.time()
    execution_time = end_time - self.start_time
    print("Ending context"
    print(f"Execution time: {execution_time} seconds")
"""
#multithreading and multi processing
#these are techniques that can be used to improve the performance of a python program
#multithreading is a technique where multiple threads are created with in a single process(share same memory space)
#multi processing is a technique where multiple processes are created

#example for multi threading
print("================================================================")

import threading

# Function to be executed in a separate thread
def thread_function(name):
    print(f"Thread '{name}' started")
    # Perform some task
    print(f"Thread '{name}' finished")

# Create three threads
thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))
thread3 = threading.Thread(target=thread_function, args=("Thread 3",))

# Execute the target function directly
thread_function("Direct Thread")

print("All threads finished")


print('================================================================')
#multi processing example
import multiprocessing

# Function to be executed in a separate process
def process_function(name):
    print(f"Process '{name}' started")
    print(f"Process '{name}' finished")

# Create three processes
process1 = multiprocessing.Process(target=process_function, args=("Process 1",))
process2 = multiprocessing.Process(target=process_function, args=("Process 2",))
process3 = multiprocessing.Process(target=process_function, args=("Process 3",))

# Execute the target function directly
process_function("Direct Process")

print("All processes finished")




#ASSIGNMENT
#opening a file and closing it automatically
# 1 create a class called FileManager which takes in 2 parameters:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

#when you exit with method ,the exit method will be called automatically and this will close the file automatically
with FileManager("example.txt", "w") as file:
    file.write("Hello, World!")

print("================================================================")
# 2 context manager for data connection
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

# Function to create a table in the database
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)")

#here am using a database on my machine and its called example
with DatabaseManager("example") as db:
    create_table(db)

print("================================================================")

#3 Context manager that shows a multithreading and multiprocessing  that allows us to run 
# the function for different amounts of time.
import threading
import multiprocessing

class TimeExecutionContext:
    def __init__(self, duration):
        self.duration = duration
#The __enter__ method simply returns the instance of the context manager itself.
    def __enter__(self):
        return self

#The __exit__ method is empty and doesn't perform any specific actions when exiting the context.
    def __exit__(self, exc_type, exc_value, traceback):
        pass
#we call run() to directly execute the target function in the current process instead of start method
    def run_multithreading(self, target_func):
        thread = threading.Thread(target=target_func, args=(self.duration,))
        thread.run()

    def run_multiprocessing(self, target_func):
        process = multiprocessing.Process(target=target_func, args=(self.duration,))
        process.run()

# Function to be executed for a specific duration
def long_running_task(duration):
    counter = 0
    while counter < duration:
        counter += 1
    print(f"Task completed after {duration} iterations.")


with TimeExecutionContext(2) as time_context:
    time_context.run_multithreading(long_running_task)
    time_context.run_multiprocessing(long_running_task)










