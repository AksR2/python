import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('This message should go to the log file')
logging.info('This too')
logging.warning('This as well')