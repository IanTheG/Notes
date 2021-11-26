# Python Notes on Advanced topics

"""
* operator

- Multiplication
- Creating lists, uples with repeated elements
- For args or kwargs arguments
- For unpacking lists, tuples, or dictionaries into function arguments
- For unpacking containers and mergining containers into a list, merging two dictionaries
"""

# Creating arrays, tuples, and strings
a = [0] * 10
b = [0, 1] * 10
c = (0, 1) * 10
d = "AB" * 10

# Function arguments
def foo(a, b, *args, **kwargs):
    print(a, b)

    for arg in args:
        print(arg)
    
    for key in kwargs:
        print(key, kwargs[key])
    
# a, b = 1, 2
# 3, 4, 5 are stored in args
# six, seven are kwargs
foo(1, 2, 3, 4, 5, six=6, seven=7)


# Function arguments
# Use * to enforce keyword arguments
# and disallow args
def bar(a, b, *, c):
    print(a, b, c)

bar(1, 2, c=3) # only takes three arguments!


# Argument unpacking
# The number of elements in the list MUST match
# the number of function arguments
def todo(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
}
todo(*my_list)
todo(*my_tuple)
# Key names MUST match when unpacking a dictionary
todo(**my_dictionary)

# Unpacking containers into single elements
# lists, tuples, sets are unpacked into lists

numbers = [1, 2, 3, 4, 5, 6] # Or as a tuple (1, 2, 3, 4, 5, 6) turns into a list
*beginning, last = numbers # unpacks 'last' into a single item:
print(beginning) # [1, 2, 3, 4, 5]
print(last) # 6

# Extracts first and last number in list
start, *middle, final = numbers

# Use the * operator to merge variables in a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
# Becomes a list
newList = [*my_tuple, *my_list, *my_set]

# Use ** to merge multiple dictionaries
dict_a = {
    "a": 1,
    "b": 2,
}
dict_b = {
    "c": 3,
    "d": 4,
}
my_dictionary = {**dict_a, **dict_b}
