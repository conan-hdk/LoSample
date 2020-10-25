'''
Created on 2014/11/08

@author: conan
'''

__all__ = ['getScriptContext', ]

import os
import time

from logging import getLogger
logger = getLogger(__name__)


def SearchFile(FileName, BasePath):
    """
    BasePathより上位フォルダに遡りながら最初に見つかったFileNameのパスを返す。
    """
    Path = os.path.join(BasePath, FileName)
    if os.path.exists(Path):
        return Path
    Path = os.path.dirname(BasePath)
    if Path == BasePath:
        return None
    return SearchFile(FileName, Path)


def get_sofficePath():
    """
    LibreOfficePortableの絶対パスを返す。
    :return:
    """
    FileName = 'LibreOfficePortable.exe'
    BasePath = None

    # logger.debug('hahaha:',os.sys.executable)
    if BasePath == None:
        BasePath = os.path.dirname(os.sys.executable)
    if BasePath == None:
        BasePath = os.environ.get('UNO_PATH', None)
    if BasePath == None:
        BasePath = os.environ.get('PYTHONHOME', None)
    if BasePath == None:
        return None

    BasePath = os.path.abspath(BasePath)
    loPath = SearchFile(FileName, BasePath)    
    logger.debug(f'Found LibreOfficePortable : {loPath} ')
    return loPath


import subprocess


def ExecLibreOffice(Port=2002):
    """
    LibreOfficeサービスを実行する。
    :return:
    """
    "C:\Program Files\OpenOffice.org 3\program\soffice.exe"
    "-accept=socket,host=127.0.0.1,port=2002;urp;StarOffice.ServiceManager"
    LibreOfficePath = get_sofficePath()
#    loargs = f'--accept=socket,host=127.0.0.1,port={listenPort};urp;StarOffice.ServiceManager'
    loargs = '--accept=pipe,name=htunopy;urp;StarOffice.ServiceManager'  # -minimized -norestore'

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#    startupinfo.wShowWindow = subprocess.SW_HIDE
    args = [LibreOfficePath, loargs]
    logger.debug(f'args={args}')
    proc = subprocess.Popen(args=args)  # , startupinfo=startupinfo)
    logger.debug(f'proc={dir(proc)}')
    time.sleep(1)
    logger.debug("Libreoffice Executed!")


import uno
import unohelper

from ht.com.sun.star.script.provider import ScriptContext


def connect(Port=2002):
    ctx = None
    try:
        localctx = uno.getComponentContext()
        sm = localctx.getServiceManager()
        resolver = sm.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", localctx)
        
        ctx = resolver.resolve(
#            f'uno:socket,host=localhost,port={Port};urp;StarOffice.ComponentContext')
            "uno:pipe,name=htunopy;urp;StarOffice.ComponentContext")
        if ctx:
            logger.debug(dir(ctx))
            return ScriptContext(ctx)
#    except:
#       pass
    finally:
        pass
    return None


import time
from ht.com.sun.star.connection import NoConnectException


def getScriptContext():
    ctx = None
    try:
        ctx = connect()
    except NoConnectException:
        ExecLibreOffice()
        st = time.time()
        timeout = 10
        while True:
            try:
                ctx = connect()
            except NoConnectException as e:
                e = time.time()
                l = e - st
                if l > timeout:
                    raise
                else:
                    logger.debug("Can not connect! wait...")
                    time.sleep(1)
            else:
                return ctx
    return ctx


def main():
    from htutil import loggerInit

    def loggerInit2(logger):
        import logging
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        logger.addHandler(sh)
        logger.setLevel(logging.DEBUG)

    loggerInit(logger)
    ctx = getScriptContext()
    if ctx != None:
        logger.debug("sucess!")
    else:
        logger.debug("Fail!")
    ctx.getDesktop().loadComponentFromURL("private:factory/scalc", "_blank", 0, ())


if __name__ == '__main__':
    main()
