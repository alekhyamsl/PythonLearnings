import logging

logging.basicConfig(filename="test3.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')

try:
    logging.info("user trying to read a file")
    with open("alekhya.txt",'r'):
        logging.info("file read operation is performed")
except Exception as e:
    logging.critical("situation to be handled")
    logging.error(e) # try to log main error
    logging.exception(e) # logs entire exception