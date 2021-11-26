# Advanced Python programming notes

"""
Random numbers!

Random module: pseudo random nums
Secrets module: cryptographic random nums
NumPy module: generate arrays with random nums
"""

# Generate pseudo random numbers

import random

a = random.random() # random float from 0 to 1
b = random.uniform(1, 10) # specify range, like .random()
c = random.randint(1, 10) # upper bound is included
d = random.randrange(1, 10) # upper bound is NOT included

# Random numbers on a normal distribution curve
# mu (mean), sigma (standard deviation)
e = random.normalvariate(0, 1)

# Sequences

# Pick a random element from a list
myList = list("ABCDEFGH")
f = random.choice(myList)
g = random.sample(myList, 3) # picks 3 unique elements
h = random.choices(myList, k=3) # picks 3 elements, can pick the same one multiple times
i = random.shuffle(myList) # shuffles the list in place

# Reproduceable random numbers with .seed()
# This prints only two random numbers!
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# Or
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# For cryptography, passwords, security tokens, authentication
# Takes some time, but generates a true random number

import secrets

j = secrets.randbelow(10) # produces a random int from [0, 10)
k = secrets.randbits(4) # produces a random int with 4 bits, [1, 15]
mylist = list('ABCDEFH')
l = secrets.choice(mylist) # produces a choice that is NOT reproduceable

import numpy as np

m = np.random.rand(3) # produces a 1x3 array with three floats
n = np.random.rand(3, 3) # produces a 3x3 array with three floats
o = np.random.randint(0, 10, 3) # [0, 10) with 3 elements
p = np.random.randint(0, 10, (3, 4)) # [0, 10) with 3x4 array
q = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(q) # shuffles first level of array, not the inside arrays

# Use a seed to generate the same result
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
