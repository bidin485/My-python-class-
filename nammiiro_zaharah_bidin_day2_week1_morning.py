#CONTROL FLOW 
#Conditional Statements(if ,elif,else)
#example 1
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# example 2
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")




#example 3
age =43
if (age<18):
        print("you are under age")
elif(age>=18 and age<=65):
        print("You are an adult")
else:
        print("Your are a senior citizen")


#LOOPS (for and while )
#for loop
#eg1

fruits=["orange","apple","pear"]
for x in fruits:
  print (x)

#eg2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#eg3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#example 3
#(while loop)
#eg1
i = 1
while i < 6:
  print(i)
  i += 1




#CONTROL FLOW STATEMENTS (using the break and continue)

print ("using continue")
i=0
while i < 6:
        i += 1 
        if i==3:
         continue
        print(i)

#Using a list        
print("using a list") 
fruits=["apple","mango","coconut","melon"]
for x in fruits:
        if x=="mango":
         continue
        print (x)

#EXCEPTION HANDLING IN PYTHON
# using try ,Except EXERCISE
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# mental health survey (CLASS EXERCISE)
print("Welcome to the Student Mental Health Assessment")

student_name = input("Please enter your name: ")

print(f"\nHello, {student_name}! Let's assess your mental health.")

rating = input("On a scale of 1 to 10, how would you rate your current mental health? (1 being low, 10 being high): ")

try:
    rating = int(rating)
    if rating < 1 or rating > 10:
        raise ValueError
except ValueError:
    print("Invalid input. Please enter a number between 1 and 10.")
    exit()

print("\nThank you for sharing. Here is your assessment:")

print(f"Name: {student_name}")
print(f"Mental Health Rating: {rating}/10")

