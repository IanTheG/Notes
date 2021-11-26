# Python Notes on Advanced topics

"""
itertools

Properties
- collection of tools for handling iterators
- iterators: data that can be used in a for loop

Functions
- product, permutations, combinations, accumulate, groupby, and infinite iterators
"""

from itertools import product

# Calculates the cartesian product
listA = [1, 2]
listB = [3, 4]
prod = product(listA, listB)
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
# With repetition
prod = product(listA, listB, repeat=2)

from itertools import permutations

# Permutations
listA = [1, 2, 3]
perm = permutations(listA)
perm = permutations(listA, 2) # specify shorter permutations with length values
print(list(perm))

from itertools import combinations, combinations_with_replacement

# Combinations, no repetitions
listA = [1, 2, 3, 4]
comb = combinations(listA, 2) # length is req
print(list(comb))
# combinations_with_replacement
combWR = combinations_with_replacement(listA, 2)

from itertools import accumulate
import operator

# Accumulate sums of a list
listA = [1, 2, 3, 4]
acc = accumulate(listA)
print(listA)     # [1, 2, 3, 4]
print(list(acc)) # [1, 3, 6, 10]
# Multiplication
listB = [1, 2, 5, 3, 4]
acc = accumulate(listB, func=operator.mul) # [1, 2, 10, 30, 120]
acc = accumulate(listB, func=max) # [1, 2, 5, 5, 5]

from itertools import groupby

def smaller_than_3(x):
    return x < 3

# Returns keys and groups from an iterable
# Use a function for key= as a filter
listA = [1, 2, 3, 4]
groupObj = groupby(listA, key=smaller_than_3)
for key, value in groupObj:
    print(key, list(value))
# This prints:
# True [1, 2]
# False [3, 4]

# Written with a lambda function
groupObj = groupby(listA, key=lambda x: x<3)

# If listA is a list of dictionaries and you want to gropuby a given key...
groupObj = groupby(listA, key=lambda x: x['key'])

from itertools import count, cycle, repeat

# count
for i in count(10):
    print(i) # starts counting at 10 and goes to infinity

# cycle
listA = [1, 2, 3]
for i in cycle(listA):
    print(i) # infinitely cycles through elements of listA

# repeat
for i in repeat(1):
    print(i) # infinitely repeats 1
for i in repeat(1, 4):
    print(i) # repeats 1 four times
