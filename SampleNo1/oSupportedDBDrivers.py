'''
Created on 2020/10/25

@author: conan
'''
from htuno import createUnoService, createProperty
from logging import getLogger
logger = getLogger(__name__)


def oSupportedDBDrivers():
    '''
    Supported Driver一覧
    https://openoffice3.web.fc2.com/OOoBasic_Base.html#OOoBC2
    '''
    logger.debug('oSupportedDBDrivers:Supported Driver一覧')
    oManager = createUnoService("com.sun.star.sdbc.DriverManager")        
    oEnum = oManager.createEnumeration()
    i = 1
    while (oEnum.hasMoreElements() and i <= 100):
        oDriver = oEnum.nextElement()
        DriverName = oDriver.getImplementationName()
        logger.debug(f'{i}) {DriverName}')
        i = i + 1


if __name__ == '__main__':
    from htutil import loggerInit
    loggerInit(logger)
    from htuno import getScriptContext
    XSCRIPTCONTEXT = getScriptContext()
    oSupportedDBDrivers()
