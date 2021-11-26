# Python Notes on Advanced topics

"""
Logging

- log levels
- config options
- logging in different modules
- capture stack traces
- rotating file handler

"""

import logging
from logging import handlers

# Describes severity of events
logging.debug() # not printed to console
logging.info()  # not printed to console
logging.warning()
logging.error()
logging.critical()

logging.basicConfig(
  level=logging.debug,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  datefmt='%m/%d/%Y %H:%M:%S'
)

# Custom logger in a new py file
logger = logging.getLogger(__name__)
# logger.info('The __name__ of this logger is the name of the file')
# logger.propagate = False # disables logger output in another file that imports this file

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log') # Logs errors to a separate file

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')


# Stack tracing
import logging

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

# Or...
import logging
import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error("The error is %s", traceback.format_exc())


# Rotating FILE handling / logging
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The handler creates an app.log text file that holds 2kB
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000): # repeats many times, we don't care about the index
    logger.info('Hello world is repeated!')


# Rotating TIME handling / logging
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6): # repeats 6 times, we don't care about the index
    logger.info('Hello world is repeated!')
    time.sleep(5) # waits five seconds
