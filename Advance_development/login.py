import logging
logging.basicConfig(format='',level=logging.DEBUG)
logger=logging.getLogger('test_logger')
filename='logs.txt'

logger.info("This will not show up")
logger.warning('This will')