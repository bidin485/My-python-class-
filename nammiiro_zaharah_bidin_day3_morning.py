#DAY 3  morning session
#operators

#ARITHMETIC OPERATORS
#addition (+)
print("======================================================================")
add=23+43
print(add)

#subtraction (-)
print("======================================================================")
sub= 45-20
print(sub)

#multiplication (*)
print("======================================================================")
multiply=42*2
print(multiply)


#division(/)
print("======================================================================")
divide=32/4
print(divide)

#modulus(%)
print("======================================================================")
module=53%4
print(module)

#Exponentiation(**)
print("======================================================================")
exponent=4**2
print(exponent)


#floor division
print("======================================================================")
floor_division=24//4
print(floor_division)

"""COMPARISON OPERATORS
== equal to 
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than orr equal to"""

a=15
b=3
print("======================================================================")
if(a==b):
    print("They are equal")
print("======================================================================")
if(a>b):
    print("yes it is")
print("======================================================================")
if(a>=b):
    print("accurate ,it is in range")
print("======================================================================")
if(a<=b):
    print("no its not ")
print("======================================================================")
if(a!=b):
    print("false")
print("======================================================================")



"""LOGICAL OPERATORS
 or 
 and 
 not
"""
a = True
b = False
print("======================================================================")
result = a and b
print(result)  # Output: False

print("======================================================================")
a = True
b = False
print("======================================================================")
result = a or b
print(result)  # Output: True

print("======================================================================")
a = True
result = not a
print(result)  # Output: False

print("======================================================================")
a = True
b = False
result = a and b  # Since the first operand is False, there's no need to evaluate the second operand.
print(result)  # Output: False
result = a or b  # Since the first operand is True, there's no need to evaluate the second operand.
print(result)  # Output: True

print("======================================================================")
a = True
b = False
c = True
result = (a and b) or (not c)
print(result)  # Output: False

#ASSIGNMENT OPERATOR
# =
print("======================================================================")
a = 5
b = a
print(b)  # Output: 5

#+
print("======================================================================")
a = 5
a += 3  # Equivalent to: a = a + 3
print(a)  # Output: 8


#-
print("======================================================================")
a = 5
a -= 2  # Equivalent to: a = a - 2
print(a)  # Output: 3


#*
print("======================================================================")
a = 3
a *= 4  # Equivalent to: a = a * 4
print(a)  # Output: 12

#/
print("======================================================================")
a = 10
a /= 3  # Equivalent to: a = a / 3
print(a)  # Output: 3.3333333333333335

#%
print("======================================================================")
a = 17
a %= 5  # Equivalent to: a = a % 5
print(a)  # Output: 2

# **
print("======================================================================")
a = 2
a **= 3  # Equivalent to: a = a ** 3
print(a)  # Output: 8

#//
print("======================================================================")
a = 10
a //= 3  # Equivalent to: a = a // 3
print(a)  # Output: 3

#membership operators( check whether a value is a member of a collection or a sequence)
#in 
print("======================================================================")
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # Output: True
print('orange' in fruits)  # Output: False

#not in
print("======================================================================")
fruits = ['apple', 'banana', 'cherry']
print('banana' not in fruits)  # Output: False
print('orange' not in fruits)  # Output: True

"""IDENTITY OPERATORS(identity operators are used to compare the identity of two objects and as 
well determine whether the two objects refer to the same memory location or not)
is( checks if values are the same)
is not (checks if values are not the same)"""

#is 
print("======================================================================")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # Output: True (x and y refer to the same list object)
print(x is z)  # Output: False (x and z are different list objects)


#is not
print("======================================================================")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is not y)  # Output: False (x and y refer to the same list object)
print(x is not z)  # Output: True (x and z are different list objects)


#BITWISE OPERATORS

#Bitwise AND (&): Performs a bitwise AND operation on the corresponding bits of two integers.
print("======================================================================")
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b
print(result)  # Output: 1

#Bitwise OR (|): Performs a bitwise OR operation on the corresponding bits of two integers
print("======================================================================")
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a | b
print(result)  # Output: 7

#Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation on the corresponding bits of two integers
print("======================================================================")
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a ^ b
print(result)  # Output: 6

#Bitwise NOT (~): Performs a bitwise NOT operation on an integer. It flips all the bits, converting 0s to 1s and vice versa.
print("======================================================================")
a = 5  # 0101 in binary
result = ~a
print(result)  # Output: -6

#Bitwise Left Shift (<<): Shifts the bits of an integer to the left by a specified number of positions. Zeros are shifted in from the right.
print("======================================================================")
a = 5  # 0101 in binary
result = a << 2
print(result)  # Output: 20 (010100 in binary)

#Bitwise Right Shift (>>): Shifts the bits of an integer to the right by a specified number of positions. Zeros are shifted in from the left.
print("======================================================================")
a = 5  # 0101 in binary
result = a >> 1
print(result)  # Output: 2 (0010 in binary)





