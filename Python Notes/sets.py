# Python Notes on Advanced topics

"""
Sets

Properties
- collection data type
- unordered
- mutable
- does NOT allow duplicate elements

Used
"""

# Define a set
mySet = {1, 2, 3}
# If defining a set with multiple same elements, the set only keeps the first occurrance
mySet = {1, 2, 3, 2, 1} # is just {1, 2, 3}

# Define a set with the constructor function
mySet = set([1, 2, 3])
mySet = set("Hello") # returns the elements in an arbitrary order, {'o', 'l', 'H', 'e'} for example

# Create an empty set
mySet = {}    # recognized as a dictionary!
mySet = set() # this is how you do it

# Add elements to a set
mySet.add(1)
mySet.add(2)
mySet.add(3)

# Remove elements from a set
mySet.remove(1)
mySet.remove(2)
mySet.remove(3)
# If attempting to remove an element that does not exist, Python throws a KeyError

# Using the .discard() method
mySet.discard(4) # does NOT throw a KeyError if the element is not found

# Clear a set
mySet.clear()

# Remove and return an arbitrary value from the set
mySet.pop()

# Iterate over a set with a for in loop
for i in mySet:
    print(i)

# Check if an element exists in a set with if in
if 1 in mySet:
    print(True)

# Union and Intersection of sets (returns a new set)
evens  = {1, 3, 5, 7, 9}
odds   = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
# Union combines elements without duplication
union = odds.union(evens) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Intersection combines elements similar to both sets
intersection = odds.union(primes) # {3, 5, 7}
# If you get an empty set, the console prints 'set()'

# Difference of two sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# .difference() returns a set with all elements from the first set that are NOT in the second set
diffAtoB = setA.difference(setB) # {1, 2, 3}
diffBtoA = setB.difference(setA) # {10, 11, 12}
# .symmetric_difference() returns a set with all elements from the first set and second set, but NOT elements in both
diffAtoBsym = setA.symmetric_difference(setB) # {4, 5, 6, 7, 8, 9, 10, 11, 12}
diffBtoAsym = setB.symmetric_difference(setA) # returns the same thing! ^^^

# Modify sets in place
# Updates setA to include all elements in B that aren't already in A
setA.update(setB) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# Updates setA to include elements found only in both sets
setA.intersection_update(setB) # {1, 2, 3}
# Updates setA by removing elements found in setB
setA.difference_update(setB) # {4, 5, 6, 7, 8, 9}
# Updates setA by only keeping elements found in setA and setB, but NOT both
setA.symmetric_difference_update(setB) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

# Subset and Super Set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}
# Sub set
setA.issubset(setB) # False
setB.issubset(setA) # True
# Super set
setA.issuperset(setB) # True
setB.issuperset(setA) # False

# Disjoint sets
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
# Disjoin returns true if both sets have a null intersection (no same elements)
setA.isdisjoint(setB) # False
setA.isdisjoint(setC) # True

# Copying sets, be careful, sets are copied by reference!
setA = {1, 2, 3, 4, 5, 6}
# Do this
setB = setA.copy()
# Or
setB = set(setA)

# Frozen set cannot be changed after created
a = frozenset([1, 2, 3, 4])
# Attempting to .add or .remove or .update will throw an AttributeError
