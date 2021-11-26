# Python Notes on Advanced topics

"""
Collections

Properties
- container data type
- Counter: 
- namedtuple
- OrderedDict
- defaultDict
- deque

"""

from collections import Counter

# Counter stores elements as dictionary keys, and their counts as dictionary values
a = "aaaaabbbcc"
myCounter = Counter(a)
print(myCounter) # prints a dictionary
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())
print(myCounter.most_common(1)) # returns the n most common elements as a list with tuples
print(myCounter.most_common(1)[0][0]) # returns the most common element
print(list(myCounter.elements())) # prints out each element, convert it to a list

from collections import namedtuple

# Create a class called Point with fields x and y
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) # prints Point(x=1, y=-4)
print(pt.x, pt.y)

from collections import OrderedDict

# This object remembers the order of items in a dictionary
# In Python 3.7, Python automatically remembers the order in a dictionary
# meaning you can use a regular dictionary!
orderedDictionary = OrderedDict()
orderedDictionary['a'] = 1
orderedDictionary['b'] = 2
orderedDictionary['c'] = 3
orderedDictionary['d'] = 4
print(orderedDictionary)

from collections import defaultdict

# Has a default value if a key has not been set
# A normal dictionary returns a KeyError
d = defaultdict(int) # float returns 0.0, list returns an empty list
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['d']) # prints 0, the default value for an integer

from collections import deque

# A double ended queue, can remove elements from both ends
de = deque()
# Put an element or a list into these to try them out
de.append()      # appends to the end of the queue
de.appendleft()  # appends to the beginning of the queue
de.pop()         # returns and removes the last element
de.popleft()     # returns and removes the first element
de.clear()       # removes all elements
de.extend()      # provided a list, adds all elements in order to the right
de.extendleft()  # provided a list, adds all elements in reverse order to the left
de.rotate(1) # rotates all elements n places to the right
de.rotate(-1) # rotates all elements n places to the left

# For example,
ex = deque()
ex.extend([8, 9])        # ex becomes deque([8, 9])
ex.extendleft([4, 5, 6]) # ex becomes deque([6, 5, 4, 8, 9])
