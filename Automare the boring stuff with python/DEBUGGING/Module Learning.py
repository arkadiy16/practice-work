import logging


# level=logging.LEVEL - will show only LEVEL and higher level.
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')

# Logging levels.
logging.debug('Some debugging details.')
# 2019-05-18 19:04:26,901 - DEBUG - Some debugging details.
logging.info('The logging module is working.')
# 2019-05-18 19:04:35,569 - INFO - The logging module is working.
logging.warning('An error message is about to be logged.')
# 2019-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
logging.error('An error has occurred.')
# 2019-05-18 19:05:07,737 - ERROR - An error has occurred.
logging.critical('The program is unable to recover!')
# 2019-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!

# Disabling logging.
# logging.LEVEL - will disable LEVEL and lower lewer.
logging.disable(logging.WARNING) 
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
# 2019-05-18 19:05:07,737 - ERROR - An error has occurred.
logging.critical('The program is unable to recover!')
# 2019-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!

# Logging to file.
logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s -  %(message)s')

# Assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
assert spam > 10 and type(spam) == int

# Assert statement that triggers an AssertionError if the variables eggs and bacon contain strings 
# that are the same as each other, even if their cases are different.
assert isinstance(eggs, str) and isinstance(bacon, str) and eggs.lower() == bacon.lower()

# Write an assert statement that always triggers an AssertionError.
assert False

# What are the two lines that your program must have in order to have logging.debug() send a logging 
# message to a file named programLog.txt?
import logging
logging.basicConfig(filename='programmLog.txt')
