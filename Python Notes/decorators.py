# Advanced Python notes

"""
Decorators

- difference between function and class decorators
- use cases
- function decorators allow you to add additional functionality to an existing function
- functions are first-class objects:
  - can be defined inside other functions
  - can be passed as arguments
  - returned from functions
- class decorators are often used to...
  - debug
  - calculate execution time
  - check if args fulfill requirements
  - register plugins
  - cache return values
  - add info / update state

"""

# Function decorators

# The function do_something() has its functionality extended
# with the @my_decorator decorator
@my_decorator
def do_something():
    pass


# Example WITHOUT decorators

def start_end_decorator(func):
    def wrapper():
        # Do something before
        func()
        # Do something after
    return wrapper

def print_name():
    print('Alex')

print_name = start_end_decorator(print_name)

print_name()


# Example with decorators

def start_end_decorator(func):
    def wrapper():
        # Do something before
        func()
        # Do something after
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)

print_name()


# Example with arguments

def start_end_decorator(func):
    # Use arguments and keyword arguments
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

# print_name = start_end_decorator(print_name)

print(add5(10))


# Example with functools to maintain function identity
# Use this as a template!

import functools

def start_end_decorator(func):
    # Use arguments and keyword arguments
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

# print_name = start_end_decorator(print_name)

print(help(add5)) 
print(add5.__name__) # add5 is returned


# Decorators with arguments 

import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('I')


# Nested decorators

def start_end_decorator(func):
    # Use arguments and keyword arguments
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        print('before')
        result = func(*args, **kwargs)
        # Do something after
        print('after')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper

# Multiple decorators are executed in the order of definition
@debug
@start_end_decorator
def say_hello(name):
    print(f'Hello {name}')


# Class decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # Allows execution of this class, like a function!
    def __call__(self, *args, **kwargs):
        # print('Called!')
        self.num_calls += 1
        print(f'This is executed {self.num_calls + 1} times')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc() # Prints 'Called!'

@CountCalls
def new_function():
    print('Hello')

new_function()
new_function()
new_function()
