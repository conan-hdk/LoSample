'''
Created on 2020/10/24

@author: conan
'''

from logging import getLogger
logger = getLogger(__name__)


def main():
    logger.debug('debug message!')
    logger.info('info message!')
    logger.warning('warning message.')
    logger.error('error message!')
    logger.critical('critical message!')


if __name__ == '__main__':

    def loggerInit(logger):
        import logging
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        logger.addHandler(sh)
        logger.setLevel(logging.DEBUG)

    loggerInit(logger)
    main()
