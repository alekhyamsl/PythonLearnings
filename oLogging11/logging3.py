import logging

logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')
# if logging is set to error then logging levels below that value are not looged
# division of 2 integers
def divide(a,b):
    logging.info("the number entered by user is %s and %s",a,b)
    # %s is the placeholder used for dynamic print
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have competed division operation")
        logging.info("the result is %s",div)
        return div
    except Exception as e:
        logging.exception(e)


print(divide(2,5))