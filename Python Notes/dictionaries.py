# Python Notes on Advanced topics

"""
Dictionaries

Properties
- collection data type
- unordered
- mutable
- key-value data type

Used for JSON like data objects
"""

# Define a dictionary with braces
myDictionary = {
  "name": "Max",
  "age": 28,
  "alive": True,
}

# Define a dictionary with the constructor function
myDictionary = dict(name="Mary", age=24, alive=True)

# Access a value with [] bracket notation
value = myDictionary["name"]
# If accessing a key that doesn't exist, Python throws a KeyError

# Add a key
myDictionary["email"] = "max28@gmail.com"

# Overwrite a value
myDictionary["age"] = 29

# Delete an item
del myDictionary["alive"]
myDictionary.pop("alive")
# Deletes the last item in the dictionary
myDictionary.popitem()

# Check if a key exists in a dictionary to avoid KeyError
if "name" in myDictionary:
    print(myDictionary["name"])
# Or
try:
    print(myDictionary["name"])
except:
    print("error")

# Iterate through a dictionary with for in loop
for key in myDictionary:
    print(key)
# Or, grab just keys
for key in myDictionary.keys():
    print(key)
# Or, grab just values
for value in myDictionary.values():
    print(value)
# Or, grab both!
for key, value in myDictionary.items():
    print(key, value)

# Copying a dictionary
# Modifying the copy will ALSO modify the original!
# Instead...
myDictionaryCopy = myDictionary.copy()
# Or
myDictionaryCopy = dict(myDictionary)

# Merge dictionaries with merge
# This overwrites keys in the dictionary on which you are calling the merge function
myDictionary = {
  "name": "Max",
  "age": 28,
  "email": "max28@gmail.com",
}
myDictionary2 = dict(name="Mary", age=24, alive=True)
myDictionary.update(myDictionary2)
print(myDictionary) # prints the following dictionary...
# myDictionary = {
#   "name": "Mary",
#   "age": 24,
#   "alive": True,
#   "email": "max28@gmail.com",
# }

# Key types, use any immutable types like numbers or even tuples, NOT lists
myDictionary = {
  3: 9,
  6: 36,
  9: 81,
}
# Be careful when accessing elements using [] notation
nine = myDictionary[3] # this way, returns 9

# Using tuples as keys
myDictionary = {
  (7, 8): 15
}
