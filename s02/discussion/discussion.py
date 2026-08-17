# Creating Comments in Python
# In Python, comments are written use the "#" symbol
# Remember that comments are not read by the program; they are only for the user


# Python Syntax
# print() is a built-in function that displays text or other data in the terminal

print("Hello, World!")

# In Python, indentation is required because it defines blocks of code.

# Variables and Data Types in Python
# Naming Convention
# Variable names in Pythons are called identifiers
# Identifiers must begin with a letter (A-Z or a-z) or an underscore (_)
# After the first character, identifiers may contain letters, numbers, and underscores
# Python follows the snake_case naming convention for variable names
# Reserved keywords cannot be used as identifiers or variables
# Identifiers are case-sensitive

_age = 21
middle_initial = "C"


# firstName = "Rodnee"

# Data Types
# A data type defines the kind of a value a variable can store
# Python has different data types, each used to represent a specific kind of data

# String (str) - for alphanumeric characters and symbols
full_name = "Rodnee Glen A. Martin"
secret_code = "Pa$$w0rd"

# Numbers (int, float, complex) - for integers, decimals, and complex numbers
num_of_days = 365
pi_approx = 3.1416
complex_num = 1 + 5j # This is a complex number, j represents imaginary component

# Boolean (bool) - for truth values
is_learning = True
is_difficult = False

# Display variable values using the print() function
print(full_name)

# String Concatenation
# In Python, the "+" symbol can be used to concatenate strings
print("Concatenation in Python:")
print("My name is " + full_name)
# print("My age is" + _age)

# Typecasting in Python
# Type casting is the process of converting a value from one data type to another
print("Typecasting in Python:")
# str() converts a value into a string
print("My age is " + str(_age))
# Other type casting functions, such as int(), float()
    # int() converts a value into an integer (whole number)
    # float() converts a value into a floating-point number (decimal)


# f-string
# To use an f-string, add a lowercase f before the string, and place the variable you want to display inside curly braces {}
print(f"Hi my name is {full_name} and I am {_age} years old.")


# Operations
# Python has families of operators that can be used to manipulate variables 
# Arithmetic Operators - performs mathematical operations

print("Arithmetic Operators:")
print(1+ 10)
print(15 - 8)
print( 18 * 9)
print(18 / 9)
print(18 % 4)
print(2**6)

# Assignment Operators - used to assign or update variable values
print("Assignment Operators:")
num1 = 3
num1 += 4 # num1 = num1 + 4
print(num1)

# Note: Other assignmnent operators include -=, *=, /=, %=

# Comparison Operators - used to compare values (returns a boolean value)
print("Comparison Operators:")
print(1 == 1)

# Note: Other comparison operators include !=, >, <, >=, <=


# Logical Operators - used to combine or evaluate multiple conditions
print("Logical Operators:")
print(True and False)
print(False or True)
print(not False)


# User Input
# Python allows input from the user
# The input() function lets the user provide input to the program
# num_one= int(input("Enter 1st number:\n"))
# num_two= int(input("Enter 2nd number:\n"))

# print(f"The sum of num_one and num_two is: {num_one + num_two}")


# Control Structures
    # Selection control structures and repetition structures

# Selection Control Structures
# if-else statements are used to choose betweeen two or more code blocks depending on the condition
# test_num2 = int(input("Please enter the test number: \n"))
# if test_num2 > 0:
#    print("The number is positive")
# elif test_num2 == 0:
#   print("The number is zero")
# else:
#    print("The number is negative")

# Repetition Control Structures
# Repetition control structures, also known as loops, allows you to execute a block of code repeatedly

# While loops - used to repeatedly execute a block of code as long as a specifiedcondition is true

i = 1
while i <= 5:
    print(f"Current count: {i}")
    i += 1

# For Loops in Python are used to iterate over a sequence
print("For Loop:")


fruits = ["apple", "banana", "cherry"]

for indiv_fruit in fruits:
    print(indiv_fruit)

# while - Keep going while this condition is true
# for - Go through each item in this sequence


# To use a for loop to iterate through vlaues, the range() function can be used
# range() function is a built-in function in Python used  to generate a sequence of numbers

# range() function with start, stop and step values
# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)
# default: start = 0, step = 1

print("Range function:")
for x in range(6, 20, 2):
    print(f"The current value is {x}")


# Break Statement
print("Break Statement in a While Loop:")
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j += 1



# Continue Statement
print("Continue Statement in a While Loop:")
k = 1
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k)