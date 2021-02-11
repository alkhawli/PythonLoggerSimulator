import logging
import time
import random
from logging.config import fileConfig

def togglelogger(logger, i,message):
        if i==1:    
            return logger.info('payload: {}'.format(message))
        elif i==2:
            return logger.debug('payload: {}'.format(message))
        elif i==3:
            return logger.warning('payload: {}'.format(message))
        elif i==4:
            return logger.critical('payload: {}'.format(message))
        else:
            return logger.error('payload: {}'.format(message))
    
if __name__ == "__main__":
    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    
    for i in range(12000):
        random_bytes = bytes([random.getrandbits(8) for _ in range(0, 8)]).hex()
        togglelogger(logger,random.randint(1,5), random_bytes)
        time.sleep(0.04)
        print(i)
        
    # Release the files
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)
        
    
