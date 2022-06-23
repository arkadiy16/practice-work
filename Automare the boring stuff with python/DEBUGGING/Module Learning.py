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
