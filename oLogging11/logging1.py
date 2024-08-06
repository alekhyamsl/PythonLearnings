""" suppose we have a requirement to collect data from different sources -> merge them ->
 Filter specific data -> and store it in DB
 there is more chances that gliches in code can happen at that time in real time env we
 use logging
 we can create different log files for different functionalities
 we can print the exceptions in log file instead of printing in console
 so that it can be stored in system/server and it can be investigated in future

  """

import logging

"""
5 different logging levels
Info (number assigned ->20) # to store generic info on file we can use Info
DEBUG 10 # when we have to perform some sort of investigation on code
warning 30 # to give waring at any point of time
Error 40 # if error/exception is raised during execution it can be logged as error
Critical 50 # If severe error occurs we can call critical log
"""

logging.basicConfig(filename="test.log", level=logging.INFO)
# if level is not mentioned the message is not printed in test.log file
logging.info("this is my first logging code")
logging.warning("this is my warning message")
logging.error("this is error message from system")
l = [1, 2, 3, 4, 5, 6, 6, 7]
for i in l:
    if i == 2:
        logging.info(i)
        logging.info(l)
        logging.warning("waring to the user that 2 is found in list")
logging.shutdown() # after this no logs will be stored

