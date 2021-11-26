# Python Notes on Advanced topics

"""
Lists

Properties
- ordered
- mutable
- allows duplicate elements
- allows elements of multiple data types
- reference elements with 0-based bracket notation (like arrays in JavaScript)

Used for objects that belong together that can be changed
"""

# Define a list with []
myList = ["banana", "cherry", "apple"]

# Grab the first element
firstItem = myList[0]

# Grab the last element
lastItem = myList[-1]

# Grab the second to last element
lastItem = myList[-2]

# Iterate through a list with a 'for in' loop
for i in myList:
    print(i)

# Check if element is in list with 'if in' syntax
if "apple" in myList:
    print("yes")
else:
    print("no")

# Grab length of list
len(myList)

# Append items
myList.append("lemon")

# Insert item at a specific index, items are shifted right
myList.insert(1, "blueberry")

# Remove and return the last item
poppedItem = myList.pop()
print(poppedItem)

# Remove a specific element
# If attempting to remove an element that doesn't exist => ValueError
myList.remove("cherry")

# Reverse a list
myList.reverse()

# Sort a list, ascending order by default in place
# Changes the original list
myList.sort()
# Use sorted() method to avoid changing the original list
newList = sorted(myList)

# Create a new list with a certain number of the same elements
myList = [0] * 5 # becomes [0, 0, 0, 0, 0]

# Concat two lists with the plus + operator
myList = [0] * 5
myList2 = [1, 2, 3, 4, 5]
myList3 = myList + myList2 # becomes [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

# Access parts of the list with array slicing and the colon :
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = myList[1:5]  # becomes [2, 3, 4, 5]
b = myList[:5]   # becomes [1, 2, 3, 4, 5]
c = myList[1:]   # becomes [2, 3, 4, 5, 6, 7, 8, 9]
# Use another colon like :: to use a step index
d = myList[::2]  # becomes [1, 3, 5, 7, 9] takes every other item
e = myList[::-1] # becomes [9, 8, 7, 6, 5, 4, 3, 2, 1] reverses a list

# Copying a list is dangerous!
# Both lists refer to the same list in memory
originalList = ["banana", "cherry", "apple"]
copiedList = originalList
copiedList.append("lemon")
print(copiedList)   # Has "lemon"
print(originalList) # Also has "lemon"!!!

# Copy a list without modifying the original with copy()
originalList = ["banana", "cherry", "apple"]
copiedList = originalList.copy()
# Or
copiedList = list(originalList)
# Or
copiedList = originalList[:]

# Remove all elements
myList.clear()

# List comprehension
# Create a new list from an existing one with one line
numbersList = [1, 2, 3, 4, 5, 6]
squaredList = [i*i for i in myList]
