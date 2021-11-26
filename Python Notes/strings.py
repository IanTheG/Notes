# Python Notes on Advanced topics

"""
Strings

Properties
- collection data type
- ordered
- immutable

Used for text representation
"""

# Define a string using '' or ""
myString = "Hello World!"
myString = 'Hello World!'
# Adjust quotes based on using the other quote in the string:
myString = 'Ian\'s world'
myString = "Ian's world"

# Multiline strings
myString = """
Multi
line
String
"""
# Adding a single backslash tells Python to NOT break the line
myString = """
Multi \
line
String
"""

# Substrings and slicing with [] notation
myString = "Hello World!"
myString[0]  # "H"
myString[-1] # "!"
# Cannot change characters
myString[0] = "h" # Python throws a TypeError
# Substring slicing using :
myString[1:5] # Starts at index 1 and goes to 5 (non inclusive)
# Step index using ::
myString[::2] # Takes every second character
myString[::-1] # Reverses the whole string

# Concat strings with +
greeting = "Hello"
name = "Ian"
sentence = greeting + " " + name

# Iterate over a string using for in loop
for i in greeting:
    print(i) # Prints each one on a new line

# Check if a character or substring is in the string
if 'e' in greeting:
    print(True)
else:
    print(False)

# Trim whitespace at beginning and end
myString = "     Hello World!     "
myString = myString.strip() # .strip does not change the string, we overwrite it

# String functions
myString.upper() # uppercase
myString.lower() # lowercase
myString.startswith('H') # check if string starts with a character or substring
myString.endswith('!')

myString.find('o') # returns first index it finds character or substring, or -1 if not found
myString.count('o') # returns the count of the character or substring, 0 if not found
myString.replace('World', 'Universe') # returns a new string
# Can choose to replace a character or substring a certain number of times

# Convert strings to list
myString = "This is a real good sentence."
myList = myString.split() # by default the delimiter is a space, ["This", "is", "a", "real", "good", "sentence."]

# Convert a list to a string
myString = ''.join(myList) # "Thisisarealgoodsentence."
myString = ' '.join(myList) # "This is a real good sentence."
# DO NOT DO THIS
myList = ['a'] * 6 # ['a', 'a', 'a', 'a', 'a', 'a']
myString = ''
for i in myList:
    myString += i # expensive in memory, takes 0.526s
# Do this
myString = ''.join(myList) # takes 0.016s !!!

# Formatting strings: %, .format(), f-strings
# %
var = "imaginary"
myString = "The variable is %s" % var
number = 3.14
myString = "The variable is %d" % number # prints a decimal, not float
myString = "The variable is %f" % number # prints a float, default 6 digits after decimal
myString = "The variable is %.2f" % number # prints 2 digits after decimal
# .format()
myString = "The variable is {:.2f}".format(number)
myString = "The variable is {:.2f}, not {}".format(number, var)
# f-strings in Python 3.6
myString = f"The variable is {var}, not {number}"
myString = f"The variable is {var + ' pi'}, not {number * 2}" # evaluates at runtime
