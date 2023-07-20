#Exception handling in Python allows you to handle and manage errors or exceptional situations that may occur during the execution of a program.
# It helps prevent your program from crashing and provides a way to gracefully handle errors.
try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("An error occurred:", str(e))

else:
    print("No exception occurred.")

finally:
    print("Program execution completed.")


#types of exceptions in python with examples 
"""
#Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred.")

#value error
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid conversion to integer.")

#fileNotFound error
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
#index error
my_list = [1, 2, 3]
try:
    print(my_list[3])
except IndexError:
    print("Error: Index out of range.")
#key error
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Error: Key not found in dictionary.")

#type error
try:
    sum = 5 + "10"
except TypeError:
    print("Error: Unsupported operand types.")

#Attribute error
my_list = [1, 2, 3]
try:
    my_list.append(4)
    print(my_list.nonexistent_method())
except AttributeError:
    print("Error: Object has no such attribute or method.")
#Import error
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found.")

#Syntax error
try:
    print("Hello")
except SyntaxError:
    print("Error: Invalid syntax.")

#Indentation error
try:
    if True:
        print("Hello")
except IndentationError:
    print("Error: Incorrect indentation.")

#Name error
try:
    x = 10
    print(x)
except NameError:
    print("Error: Name 'x' is not defined.")

#Module not found error
try:
    import sys
except ModuleNotFoundError:
    print("Error: Module not found.")

"""




#FILE HANDLING IN PYTHON open()
"""
file = open("filename.txt", "r")  # Open for reading
file = open("filename.txt", "w")  # Open for writing (creates a new file or truncates the existing one)
file = open("filename.txt", "a")  # Open for appending (adds content to the end of the file)
"""
#reading 
"""
read(): Reads the entire contents of the file as a single string.
readline(): Reads a single line from the file.
readlines(): Reads all the lines from the file and returns them as a list."""
 #eg
file = open("filename.txt", "r")
content = file.read()
print(content)
file.close()

#writing( here we use write())
file = open("filename.txt", "w")
file.write("Hello, World!")
file.close()

#appending (mode will be "a")
file = open("filename.txt", "a")
file.write("New log entry")
file.close()
#closing a file (we use close() or we use the with )
"""
with open("filename.txt", "r") as file:
    content = file.read()
    # Do something with the content

# The file is automatically closed outside the 'with' block

"""
#other modes that can be applied on to the files
"""
"r" - Open for reading.
"w" - Open for writing (creates a new file or truncates the existing one).
"a" - Open for appending (adds content to the end of the file).
"x" - Open for exclusive creation (fails if the file already exists).
"+" - Open for updating (reading and writing).
"""
#An examples that applies to both fileHandling and Exception handling
try:
    # Open the file in read mode
    with open('filename.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")




