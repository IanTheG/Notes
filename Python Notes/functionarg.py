# Advanced Python notes

"""
Function Arguments

- difference between arguments and parameters
- positional and keyword arguments
- default arguments
- variable length arguments (using *args **kwargs)
- container unpacking into function arguments
- local v global arguments
- parameter passing (by value or by reference)

"""

# Arguments are the values passed in the () while calling a function
# Paremeters are defined inside the function definition

def func(a, b, c): # Paremeters
    print(a, b, c)

func(1, 2, 3) # Arguments

func(a=1, b=2, c=3) # Keyword arguments, order does not matter!

func(1, c=3, b=2) # use a mix

# func(1, b=2, 3) # Raises an error

# func(1, a=1, b=2) # Do not use both a positional and keyword argument!

# Default Arguments
# Must be the last parameter! (a, b=2, c, d) throws an error
def func2(a, b, c, d=4):
    print(a, b, c, d)

func2(1, 2, 3) # d is not needed in the function call


# Passing any number of arguments, use *args
# Passing any number of keyword arguments, use **kwargs
def func3(a, b, *args, **kwargs):
    
    for arg in args: # A list
        print(arg)
    
    for key in kwargs: # A dictionary
        print(key, kwargs[key])

func3(1, 2, 34, 56, 78, ninety=90, hundred=100)

# Enforce using only keyword arguments with a single *
def func4(a, b, *, c, d):
    print(a, b, c, d)

func4(1, 2, c=3, b=4)

# Another to enforce using only keyword arguments
def func5(*args, last):
    for arg in args:
        print(arg)
    print(last)

func5(1, 2, 3, last=100)


# Unpack a list into a function call's arguments
# The container's length must match the number of function parameters
def func6(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
func6(*my_list)
func6(*my_tuple)

# With dictionaries, the key names must match the function's parameters
# The length must match too
my_dictionary = {
  "a": 1,
  "b": 2,
  "c": 3,
}
func6(**my_dictionary)


# Local v Global variables
def foo():
    global number # Use the global keyword to reference number at the global level
    x = number
    number = 3
    print("number inside function", x)

number = 0
foo() # Prints 0
print(number) # Print 3
