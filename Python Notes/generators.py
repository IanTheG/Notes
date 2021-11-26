# Advanced Python notes

"""
Generator

A function that returns an object that can be iterated over
Generate items one at a time, only when you need it
Function runs until the first yield statement

Can use as inputs to other functions that take iterables as arguments.
Useful for saving memory when working with large data.
"""

# Basic definition

def my_generator():
    yield 2
    yield 1
    yield 3

g = my_generator()
print(g)

for i in g:
    print(i)

value = next(g)
print(value) # 2
value = next(g)
print(value) # 1
value = next(g)
print(value) # 3

value = next(g)
print(value) # Raises a StopIteration error!

# Use Generators with other methods
print(sum(g)) # 6
print(sorted(g)) # [1, 2, 3]

# Execution of generators example
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
cd = countdown(4)
value = next(cd)


# Advantage of generators
import sys

def firstn(n):
    num = 0
    nums = [] # numbers are saved in an array
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num # numbers aren't stored in a generator
        num += 1

myList = firstn(10) # 45
myList = firstn_generator(10) # 45

# With large n, the memory storage is significantly more using arrays
# Use generators to decrease memory usage
print(sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_generator(10)))


# Fibonacci sequence example

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b
fib = fibonacci(30)
for i in fib:
    print(i)


# Generator expressions
# Written like list comprehension, uses () instead of []
import sys

# List comprehension
my_list = [i for i in range(10) if i % 2 == 0]
print(sys.getsizeof(my_list))

# Puts all even integers from 0 to 9 in a generator
my_gen = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(my_gen))
print(list(my_gen)) # convert the generator to a list
