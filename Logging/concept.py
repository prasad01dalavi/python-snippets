import logging

"""
Logging Levels:
1.debug 	2.info 	3.warning 	4.error 	5.critical
Note: debug and info will not be printed because default logging level is warning
Therefor we have to configure the logging level as below to log these
"""
logging.basicConfig(level=logging.DEBUG,
                    filename='logfile.log',
                    filemode='a',
                    format='%(levelname)s: Line:%(lineno)d %(asctime)s ==> %(message)s')


logging.info("This info looks cool!")
# In logfile.log I will get the following
"""
INFO: Line:15 2019-02-26 16:47:16,927 ==> This info looks cool!
INFO: Line:15 2019-02-26 16:47:17,338 ==> This info looks cool!
INFO: Line:15 2019-02-26 16:47:17,508 ==> This info looks cool!
"""
