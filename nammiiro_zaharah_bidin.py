#THE SYNTAX

#print('lets kick off')
#print("lesson 1")
""" PEP8
PEP 8 is a set of guidelines and recommendations for coding style in Python ie some key guidelines covered by 
pep include 
                -indentions 
                -naming conventions
                        .Camel case ie myVariableName = "John"
                        .snake case ie my_variable_name = "John"
                        .Pascals case ie MyVariableName = "John"
                -line length
                -comments (single line comment(#) and below are multiline comments(""" """))
                -white space
                -functions and methods

VARIABLES
Variables are containers for storing data values.
name="ball"
size=50
print(name)

DATATYPES
 for example
        numeric type
                integer values are int 
                        y = int(3)   
                float values are float like
                        pi=3.14 
                        gpa= 5.0
                        z = float(3)   will be 3.0
                String values -> str (represented by single or double quotes):here we can also have numbers inform of strings 
                  x = str(3)    will be '3'


      
                Boolean ->bool :logical values  
                        isEmpty=True
        Sequence types :
                lists ->enclosed with the square brackets[] are the :(ordered way and allow duplicates and can be changed)
                        my_list = ["apple", "banana", "cherry"]

                tuple -> are used to store multiple items in a single variable enclosed with parentheses():(ordered and unchangeable, allow duplicates)
                        my_tuple = ("apple", "banana", "cherry")
                range ->used in iterations ,loops
                        for num in range(5):
                                print(num)
        Mapping types
                     dictionary represented with curly braces ie
                       this_dict = {
                        "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964
                        }
        Set Types A set is a collection which is unordered, unchangeable, and  not indexed.
            my_set = {"apple", "banana", "cherry"}
        None types;These represent absence of a value
                    eg 
                  
                    def greet(name=None):
                        if name is None:
                                print("Hello, stranger!")
                        else:
                                print("Hello, " + name + "!")
"""

