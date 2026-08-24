# Lists
# A list is a collection of multiple values stored in a single variable
# Lists are created using square brackets ([])

names = ["John", "Paul", "George", "Ringo"] #string list
programs = ["developer career", "pi-shape", "tech career package"]

durations = [260, 180, 20] #Number list

truth_values = [True, False, True, False, False] #Boolean list

# This is not recommended
mixed_data = ["John", 25, True]

# Getting list size
# len() returns the number of elements in a list
print("Lists:")
print(programs)
print(len(programs))

#Accessing Values in Lists
print("Accessing Elements:")
print(names[0]) #access the first element

# Negative indexing
# last element/item: -1
print(names[-1])

# Second item
print(durations[1])

# Access a range of values
# Syntax: list[start_index:end_index]
# programs = ["developer career", "pi-shape", "tech career package"]
print(programs[0:2])
# Result: Displays elements at index 0 and 1
# Output:['developer career', 'pi-shape']

# Updating Lists
print(f"Current value: {programs[2]}")
programs[2] = "Short course"

print(f"New value: {programs[2]}")
print(programs)


# List Manipulation

# Adding list items
# append() to add an element to the end of the list
programs.append("global")
print(programs)

# Deleting list items
# del keyword removes an element from the list using its index
print(truth_values)
del truth_values[-1]
print(truth_values)

# Empty a list
# clear() method removes all elements from the list
test_list = [1, 2, 3, 4, 5]
print(test_list)
test_list.clear()
print(test_list)

# Membership Checks
# The in keyword checks whether an element exists in the list
print(20 in durations)
# durations = [260, 180, 20]
print(50 in durations)

# Sorting Lists
# sort() method sorts the list in ascending order by default
print(names)
names.sort()
print(names)

# mixed_data.sort()
# print(mixed_data)

truth_values.sort()
print(truth_values)

# Dictionaries
# A dictionary is a collection of key-value pairs
# Dictionaries are created using curly braces ({})

person1 = {
	"name": "Brandon",
	"age": 28,
	"occupation": "student",
	"isEnrolled": True,
	"subjects": ["Python", "SQL", "Django"]
}

# Geeting Dictionary Size
# The len() function returns the number of key-value pairs in a dictionary

print(len(person1))
# Result: 5

# Accessing values in Dictionaries
# Accessing a value by referring to its key
print(person1["name"])

# The keys() method returns all keys in the dictionary
print(person1.keys())

# The values() method retuns all values in the dictionary
print(person1.values())

# The items() method returns all key-value pairs in the dictionary
print(person1.items())


print(person1)

# Adding key-value pairs
# Add a new key-value pair by assignng a value to a new key or by using update() method

person1["nationality"] = "Filipino"
print(person1)

person1.update({"fav_food": "Sinigang", "address": "Cebu City"})
print(person1) 


# Deleting a key-value pairs
# Remove a key-value pair using the pop() method or the del keyword
person1.pop("fav_food")
print(person1)

del person1["nationality"]
print(person1)

# Emptying a dictionary
# The clear() method removes all key-value pairs from the dictionary
person2 = {
	"name": "John",
	"age": 18
}

print(person2)
person2.clear()
print(person2)


# Looping Through a Dictionary
# Use a for loop to iterate through keys in a dictionary

print(person1)

for key in person1:
	print(f"The value of {key} is {person1[key]}")

# Nested Dictionaries
# Dictionary can contain another dictionary as one of its value

person3 = {
	"name": "Monika",
	"age": 20,
	"occupation": "developer",
	"is_enrolled": True,
	"subjects": ["Python", "SQL", "Django"]
}

classroom = {
	"student1": person1,
	"student2": person3
}

print(classroom.items())

# Functions
# A function is a reusable block of code that performs a specific task
# Functions are defined using the def keyword


# Define a function named my_greeting
def my_greeting():
	# Code to execute
	print("Hello User!")

# Call a function using its name followed by parentheses
my_greeting()
my_greeting()
my_greeting()
my_greeting()


# Function Parameters
# Parameters are variables defined inside the parentheses of a function

def greet_user(username):
	print(f"Hello, {username}!")

# Arguments are the values passed to a function when it is called
greet_user("Miah")

greet_user("Amy")

# Return statements
# The return keyword sends a value back to the caller

def addition(num1, num2):
	return num1 + num2

sum = addition(5, 10)
print(f"The sum is {sum}")


# Lambda Functions
# A lambda function is a small anonymous function written in a single line
# It can accept multiple arguments but contains only one expression

greeting = lambda person: f"Hello, {person}!"
print(greeting("John"))

multiply = lambda a, b: a * b
print(multiply(5,6))