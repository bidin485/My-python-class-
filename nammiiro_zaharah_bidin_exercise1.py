"""A set is a collection of unordered ,unchangeable but can be adjusted by adding or removing items, and 
they are not indexed"""
my_set = {"apple", "banana", "cherry"}
print(my_set)


#length of the set
print(len(my_set))


#data type
print(type(my_set))


#accessing items in a set
for x in my_set:
    print x


#check  if item is present in a set
 print(apple in my_set)


#Add items in a set
my_set.add("pineapple")
print (my_set)


# you can also add items of one set into another
set2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set2.update(tropical)
print(set2)
   
# to add two sets together, you can either use update or union
#using union
set1 = {"a", "b" , "c"}
set4 = {1, 2, 3}
set3 = set1.union(set4)
print(set3)
 # using update
 set1 = {"a", "b" , "c"}
set4 = {1, 2, 3}
set1.update(set4)
print(set1)