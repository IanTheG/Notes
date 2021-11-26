# Python Notes on Advanced topics

"""
Tuples

Properties
- collection data type
- ordered
- immutable (cannot be changed after created)

Used for objects that belong together
"""

# Define a tuple
myTuple = ("Max", 28, "Boston")
# Parenthesis are optional, just, use, commas
myTuple = "Max", 28, "Boston"

# Define a single item in a tuple
myTuple = ("Max")  # DOES NOT WORK! Python sees this as a string
myTuple = ("Max",) # Include a comma!

# Check the type of an object
type(myTuple)

# Use the tuple constructor to create a tuple from a list
myTuple = tuple(["Max", 28, "Boston"])

# Access elements with an index, 0-based like Lists
item = myTuple[0]
# IndexError appears when using an index out of range
# Access the last item, or second to last item with negative indexes
lastItem = myTuple[-1]

# Tuple does NOT support object assignment
myTuple[0] = "Tim" # THROWS A TypeError

# Iterate over a tuple
for i in myTuple:
    print(i)

# Check if an element exists in a tuple
if "Max" in myTuple:
    print(True)
else:
    print(False)

# Grab num of elements in tuple
myTuple = ('a', 'p', 'p', 'l', 'e')
len(myTuple) # returns 5

# Count num of an element in tuple
myTuple.count('p') # returns 2
# Returns 0 if not found

# Find the first index occurrance of a specific element
myTuple.index('p') # returns 1
# Throws a ValueError if an element is not found!

# Convert a tuple to a list
myList = list(myTuple)

# Convert a list to a tuple
myTuple = tuple(myList)

# Access a part of a tuple with slicing startIndex:stopIndex (non inclusive)
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]  # returns (3, 4, 5)
c = a[:5]   # starts from beginning to index 5
d = a[5:]   # starts at index 5 and goes to end
e = a[::2]  # returns every other element
f = a[::-1] # reverses a list
g = a[::-2] # reverses a list and returns every other element

# Assign each element in a tuple to a variable
# Number of elements MUST match, otherwise a ValueError appears!
myTuple = "Max", 28, "Boston"
name, age, city = myTuple

# Unpack multiple elements with a *
myTuple = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = myTuple
print(i1) # first element, 0
print(i2) # list of elements between i1 and i3, [1, 2, 3, 4]
print(i3) # last element, 5

# Compare a tuple and a list's size in memory
import sys
myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(myList), "bytes")  # returns '104 bytes'
print(sys.getsizeof(myTuple), "bytes") # returns '88 bytes'

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # returns 0.169...
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # returns 0.019...
# It takes more time to create and process a list
