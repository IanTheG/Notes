# Python Notes on Advanced topics

"""
Exceptions

The program terminates when it encounters a syntax error or exception

Syntax: an incorrect statement Python doesn't like
Exception: even if a statement is syntatically correct, it may still cause an error at runtime

FileNotFoundError
IndexError
ModuleNoteFoundError
NameError
TypeError
ValueError
ZeroDivisionError

"""

# Raising an Exception
x = 0
if x < 0:
    raise Exception("x must be greater than 0")

# Raises an AssertionError if the condition is false
assert (x > 0), "x must be greater than 0"

# Try Except block
# Program continues, does not exit
try:
    a = 5 / 0
# Can catch specific exception types too
except Exception as e:
    print(e)
    print('You cannot divide by 0')
# Or
except ZeroDivisionError:
    print('You cannot divide by 0')

# Catch multiple exceptions
try:
    a = 5 / 0
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
# Use an else clause when no exception occurs
else:
    print('No exceptions were caught!')
# Use a finally clause after everything, clean up
finally:
    print('Runs after everything')

# Define your own error classes from existing ones
class ValueTooHighError(Exception): pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
test_value(200)

try:
    test_value(101)
except ValueTooHighError as e:
    print(e)

# Define error classes with some extra stuff
# Custom init method
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 0:
        raise ValueTooSmallError('Value is too small', x)
test_value(200)

try:
    test_value(101)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
