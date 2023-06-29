#dictionaries 
my_dictionary={
    "brand":"iphone",
    "model": 14,
    "year": 2022
}
print(my_dictionary)
print(len(my_dictionary))
print(type(my_dictionary))

#accessing items in a dictionary
print(my_dictionary.get("model"))
x=my_dictionary["model"]
print(x)

#you can still access through checking
if "model" in my_dictionary:
    print("yes a model exists")

 #METHODS

 #keys method ->this returns all keys 
print(my_dictionary.keys())

#values()->this returns all values of a dictionary
print(my_dictionary.values())

#items()->returns all items in the dictionary inform of a tuple
print(my_dictionary.items())

 #CHANGING ITEMS IN A DICTIONARY==>EXERCISES FOR DICTIONARY
my_dictionary["model"]="samsung"
print(my_dictionary)

# you can as well change using the update()method
print(my_dictionary.update({"year": 2021}))

 #ADDING  
my_dictionary["color"]="white"
my_dictionary.update({"size": 32})
print(my_dictionary)

 #REMOVING 
 #using pop()=>this removes a specified item in the pop()method
my_dictionary.pop("model")
print(my_dictionary)


 #using the popitem()=>This removes the last item placed in the dictionary
my_dictionary.popitem()
print(my_dictionary)

 #using del =>this removes the item that is identified ,it can as well delete the dictionary
del my_dictionary["brand"] 
print(my_dictionary)
  
#del my_dictionary
#print(my_dictionary) this prints an error since the dictionary was deleted

 
 #LOOP
 #this loops through values in a dictionary
for value in my_dictionary.values():
 print(value)


#this loops trough keys in a dictionary
for key in my_dictionary.keys():
 print(key)

#this loops through all items of a dictionary
for x,y in my_dictionary.items():
 print(x,y)
  
#this prints the key names in the dictionary as well
for x in my_dictionary:
  print(x)

#copy dictionaries
my_second_dictionary=my_dictionary.copy()
print(my_second_dictionary)

# you can also use the method dict()
my_second_dictionary=dict(my_dictionary)
print(my_second_dictionary)

#nest dictionaries

my_friends = {
  "friend1": {
    "name" : "cathy",
    "year" : 2002
  },
  "friend2": {
    "name" : "josephine",
    "year" : 2002
  },
  "friend3": {
    "name" : "martha",
    "year" : 2023
  }
}
 #accessing items in the dictionary called my_friends
 
print(my_friends["friend1"]["name"])
print(my_friends["friend2"]["name"])
print(my_friends["friend3"]["name"])


#NUMBERS

#integers
x = 2
y = -4
z = 39393002
print(type(x))
print(type(y))
print(type(z))

  #floats
q = 2.33
r = 344.002
s = -35353.363
print(type(q))
print(type(r))
print(type(s))

  #complex
t = 2j
u = 4+3j
v = 55j
print(type(t))
print(type(u))
print(type(v))

#conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#casting ->specifying a type onto a variable
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)

#STRINGS IN PYTHON
W="I am called Flower"
print(w)
#multiline strings
v=""" i am a girl,
i offer a course in software Engineering, 
it is so interesting"""
print(v)

#string arrays
f="anaconda"
print(f[0])

#length of the string EXERCISE 1
print(len(f))

# Using a for loop in a string EXERCISE 2
for m in f:
    print(m) 

if "co" in f:
    print("yes it is")
else:
    print("no it is not ")

#slicing strings EXERCISE 3
#here ,you can return a range of characters
string=" Hello, Good Afternoon "
print(string[2:5])
print(string[:5]) #slices from start of the string 5 not inclusive
print(string[2:]) #slices from end  2 inclusive
print(string[-5:-2]) # slices starting from the end since they are negative numbers

#modifying  strings EXERCISE 4
print(string.lower())
print(string.upper())
print(string.split(",")) #returns a list separated with a comma
print(string.replace("H","Y"))
print(string.strip()) # removes the whitespace at the beginning and the end

#Concatenating strings
string1="hello"
string2="world"
major_string= string1+string2
print(major_string)
#format string
  #example 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

 #example 2
quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

 #example 3 =>here we can put indexes in the curly braces to make sure the values are placed in the right positions
quantity = 3
item_no = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, item_no, price))



#BOOLEANS =>These evaluate to true or false
#evaluating values and variables using a boolean functions
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# using a condition to show how to use booleans EXERCISE 5
a = 200
b = 33

if (b > a)==True:
  print("b is greater than a")
else:
  print("b is not greater than a")