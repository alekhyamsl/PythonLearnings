import logging

logging.basicConfig(filename="test1.log",level=logging.DEBUG,format=' %(name)s %(levelname)s %(asctime)s %(message)s')
# to add timestamp to log file
logging.info("this is logging info with timestamp")
