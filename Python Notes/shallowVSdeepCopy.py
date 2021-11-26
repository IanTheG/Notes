# Advanced Python notes

"""
Shallow vs Deep Copies

"""

org = 5
cpy = org # Both variables point to the same number, or same reference in memory
cpy = 6 # Now creates a new variable
# This works the same for any other data type

# Copying objects

# Shallow copy only copies one level deep,
# references nested child objects

import copy

array = [1, 2, 3, 4]
array_copy = copy.copy(array)
array[0] = -10
print(array) # [-10, 2, 3, 4]
print(array_copy) # [1, 2, 3, 4]

# Use:
# copy.copy(myList)
# myList.copy()
# list(myList)
# myList[:]


# Deep copy
# Full independent copy of an object
# Use for nested objects or nested lists

# myList.deepcopy()


# Copying classes / objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 28)
p2 = copy.copy(p1) # Shallow copy works for a simple object

# If one object references another object, use deepcopy to copy it
# and avoid copy errors
