# Advanced Python notes

"""
Context Managers

Managing resources
Allocate and release resources when you need to
"""

# Use 'with' as a context manager
# Automatically closes file and handles errors

with open('notes.txt', 'w') as file:
    file.write('some data to write')

# NO CONTEXT MANAGER
file = open('notes.txt', 'w')
try:
    file.write('some data to write')
finally:
    file.close()


# Use a lock
from threading import Lock
lock = Lock
lock.acquire()
# Do something safely here, ensures thread safety
lock.release()

# CONTEXT MANAGER for LOCKS
from threading import Lock
lock = Lock
with lock:
    pass # Do something here...


# Use a class for a custom context manager

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    # Exectues as soon when 'with' statement starts
    def __enter__(self):
        print('enter method')
        self.file = open(self.filename, 'w')
        return self.file # the allocated resources

    # Correctly close the file when 'with' statement ends
    # Handle exceptions here
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit method')

with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todo...')



# Use a class for a custom context manager
# This time print the exceptions!

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    # Exectues as soon when 'with' statement starts
    def __enter__(self):
        print('enter method')
        self.file = open(self.filename, 'w')
        return self.file # the allocated resources

    # Correctly close the file when 'with' statement ends
    # Handle exceptions here
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exceptions:', exc_type, exc_value)
        print('exit method')
        return True # Must return True to avoid exception error printing in the console

with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todo...')
    file.thisThrowsAnError()



# Use a generator function as a context manager!

from contextlib import contextmanager

@contextmanager # Enables this function to be used as a context manager with a 'with' statement
def open_managedFile_generator(filename):
    f = open(filename, 'w') # Attempts to allocate resource
    try:
        yield f # yields resource and suspends execution
    finally:
        f.close()

with open_managedFile_generator('notes.txt') as f:
    f.write('some todo...') # Runs after 'yield f' statement
