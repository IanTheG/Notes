# Python Notes on Advanced topics

"""
Lambdas

Properties
- an anonymous function, can have arguments
- no name!
- lambda keyword

Used to simplify functions to one line,
functions that require functions for arguments

"""

# Define a lambda function
add10 = lambda x: x + 10
print(add10(5)) # 15
# Exactly the same as
def add10_func(x): 
    return x + 10

# Multiple arguments
mult = lambda x,y: x * y
print(mult(2,3)) # 6

# Sorted method on points / tuples
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)
# Automatically sorted by 'x' value
# [(1,2), (5,-1), (15,1), (10,4)]

# Sort by y using a lambda to sort the points / tuples
points2D_sorted = sorted(points2D, key=lambda x: x[1])
# [(5,-1), (15,1), (1,2), (10,4)]

# Sort by sum of values in point / tuple
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
# [(1,2), (5,-1), (10,4), (15,1)]

# Map transforms each element with a function, like JS .map()
listA = [1, 2, 3, 4, 5]
listB = map(lambda x: x*2, listA)
print(list(listB)) # [2, 4, 6, 8, 10]

# List comprehension
listC = [x*2 for x in listA] # [2, 4, 6, 8, 10]

# Filter a list with a lambda, must return True or False
# Returns all elements tha evaluate to True
listA = [1, 2, 3, 4, 5, 6]
listB = filter(lambda x: x%2 == 0, listA)
print(list(listB)) # [2, 4, 6]
listC = [x for x in listA if x %2 == 0] # [2, 4, 6]

from functools import reduce

# Reduce takes a function and sequence, 
# repeatedly applies a function to the elements and returns a single value
listA = [1, 2, 3, 4, 5]
product_a = reduce(lambda x,y: x*y, listA)
print(product_a) # 720
