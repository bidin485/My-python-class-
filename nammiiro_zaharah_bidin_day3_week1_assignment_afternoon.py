my_friends=["zaharah","cloe","cathy","vinnie","jose"]
print(my_friends[1])
#2
print("======================================================================")
my_friends[0]="Bidin"
print(my_friends)

#3
print("======================================================================")
my_friends.append("patra")
print(my_friends)
#4
print("======================================================================")
my_friends.insert(2, "Bathel")
print(my_friends)
#5
print("======================================================================")
del my_friends[3]
#6

print("======================================================================")
print(my_friends[-1])  

#7
print("======================================================================")
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers[2:5])  

#8
print("======================================================================")
countries = ["USA", "Uganda", "Kenya", "Saudi Arabia"]
countries_copy = countries.copy()
print(countries_copy)  

#9

print("======================================================================")
for country in countries:
    print(country)

#10
print("======================================================================")
animal_names = ["Elephant", "Tiger", "Lion", "Zebra", "Giraffe"]

# Ascending order
print("======================================================================")
animal_names.sort()
print(animal_names) 

# Descending order
print("======================================================================")
animal_names.sort(reverse=True)
print(animal_names)  


#11
print("======================================================================")
a_animals = [name for name in animal_names if 'a' in name.lower()]
print(a_animals) 

#12
print("======================================================================")
first_names = ["John", "Alice", "Michael"]
second_names = ["Doe", "Smith", "Johnson"]
my_names=first_names+second_names
print(my_names)
full_names = [first + " " + second for first, second in zip(first_names, second_names)]
print(full_names)  

#EXERCISE 2
#1
print("======================================================================")
phones = ("samsung", "iphone", "tecno", "redmi")
print(phones[1])  

#2
print("======================================================================")
print(phones[-2]) 

#3
print("======================================================================")
phones=list(phones)
phones[1]="itel"
print(phones)

#4
phones=tuple(phones)
phones=phones+("huawei",)
print(phones)

#5
print("======================================================================")
for x in phones:
    print(x)

#6
phones=phones[1:]
print(phones)
#or
#phones=list(phones)
#del phones[0]
#or 
#phones=list(phones)
#phones.remove("samsung")
#print(tuple(phones))

#7
print("======================================================================")
uganda_cities = tuple(["Kampala", "Masaka", "Jinja", "Mbarara","Jinja"])
print(uganda_cities)  

#8
print("======================================================================")
names = ("Zaharah", "Bidin")
first_name, last_name = names
print(first_name)  
print(last_name)  

#9
print("======================================================================")
uganda_cities = ("Kampala", "Masaka", "Jinja", "Mbarara", "Gulu", "Mbale")
print(uganda_cities[1:])

 #10
print("======================================================================")
first_names = ("Martha", "Bidin", "Rahmah")
second_names = ("Namugga", "Nammiiro", "Nanyonga")
full_names = first_names + second_names
print(full_names) 

#11
print("======================================================================")
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)  

#12
print("======================================================================")
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = this_tuple.count(8)
print(count)  


#EXERCISE 3(SETS)
#1
print("======================================================================")
beverages = set(["coffee", "tea", "juice"])
print(beverages)  

#2
print("======================================================================")
beverages.add("water")
beverages.update(["soda", "lemonade"])
print(beverages)

#3
print("======================================================================")
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

#4
print("======================================================================")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)

#5
print("======================================================================")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

#6
print("======================================================================")
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet) 

#7
print("======================================================================")
ages = {25, 30, 35}
first_names = {"Zaharah", "Allen", "shady"}
joined_set = ages.union(first_names)
# or
# joined_set = ages | first_names
print(joined_set)

#EXERCISE 4 (STRINGS)
#1
print("======================================================================")
integer_var = 10
string_var = " years old"
concatenated_string = str(integer_var) + string_var
print(concatenated_string)

#2
print("======================================================================")
txt = " Hello, Uganda! "
trimmed_txt = txt.strip()
print(trimmed_txt)

#3
print("======================================================================")
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

#4
print("======================================================================")
txt = "Hello, Uganda!"
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#5
print("======================================================================")
y = "I am proudly Ugandan"
substring = y[1:4]
print(substring)

#6
print("======================================================================")
x = 'All "Data Scientists" are cool!'
print(x)

#EXERCISE 5  (DICTIONARIES)

#1( printing a shoe size)
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print(shoe_size)

#2( change brand to adidas )
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print(Shoes)

#3(Adding key/value pair)
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print(Shoes)

#4(returning keys  in the dictionary)
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

keys_list = list(Shoes.keys())
print(keys_list)

#5(return values )
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

values_list = list(Shoes.values())
print(values_list)

#6(check if size exists)
print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

if "size" in Shoes:
    print("Key 'size' exists in the dictionary")
else:
    print("Key 'size' does not exist in the dictionary")
#7(looping through dictionary)

print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

for key, value in Shoes.items():
    print(key, ":", value)
#8(remove color from dictionary)

print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

del Shoes["color"]
print(Shoes)
#9 (emptying the dictionary)

print("======================================================================")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

Shoes.clear()
print(Shoes)
# 10(copying a dictionary)
print("======================================================================")
original_dict = {"name": "John", "age": 30}
copied_dict = original_dict.copy()
# or
# copied_dict = dict(original_dict)
print(copied_dict)
 
#11 (nested dictionary)
print("======================================================================")
nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Alice", "age": 25}
}

for person, details in nested_dict.items():
 print(person)
 for key, value in details.items():
  print(key, ":", value)
print()








 



