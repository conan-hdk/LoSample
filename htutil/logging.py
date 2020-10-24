'''
Created on 2020/10/22

@author: conan
'''

__all__ = ['loggerInit',]

from logging import getLogger
logger = getLogger(__name__)
    
def loggerInit(logger):
    '''
    ログ出力をコンソールに設定する。
    '''
    import logging
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.setLevel(logging.DEBUG)

if __name__ == '__main__':  
    loggerInit(logger)
    logger.debug('debug message!')
    logger.info('info message!')
    logger.warning('warning message.')
    logger.error('error message!')
    logger.critical('critical message!')
