# Python advanced notes

"""
JSON

"""

import json

person = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hasChildren": 30,
  "titles": ["engineer", "programmer"]
}
# Dumps object to json string
# Format with indent= separators= sort_keys=
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# Dump python data into a separate .json file
# Serialization
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# De-serialization
person = json.loads(personJSON)
print(person)
# Or
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


# Encode python classes into JSON

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('Max', 27)

# Write a custom encoding function to turn a class into JSON
def encode_user(o):
    if isinstance(o, User):
        return {
          'name': o.name,
          'age': o.age,
          o.__class__.__name__: True # Returns the class name as a key
        }
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)

# Another way using JSONEncoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {
              'name': o.name,
              'age': o.age,
              o.__class__.__name__: True
            }
        return JSONEncoder.default(self, o)
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# Or
userJSON = UserEncoder().encode(user)
print(userJSON)

# Decode object back to python dictionary
user = json.loads(userJSON)
print(user)

# Write a custom decoding method to turn object back into a User object
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict
user: User = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
