'''
Created on 2020/10/24

@author: conan
'''

from logging import getLogger
logger = getLogger(__name__)


def main():
    ShowNamesInObject(XSCRIPTCONTEXT, 'XSCRIPTCONTEXT')
    desktop = XSCRIPTCONTEXT.getDesktop()
    ShowNamesInObject(desktop, 'desktop')
    Book = desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, ())
    ShowNamesInObject(Book, 'Book')
    Sheet = Book.getSheets().getByIndex(0)
    ShowNamesInObject(Sheet, 'Sheet')
    Cell = Sheet.getCellByPosition(0, 0)
    ShowNamesInObject(Cell, 'Cell')
    Cell.Value = 123456


def ShowNamesInObject(obj, objName):
    '''
    指定のObjectに含まれる全てのメソッドやプロパティをログに出力する
    '''
    logger.debug(f'dir({objName}):')
    for n in dir(obj):
        logger.debug(f'\t[{n}]')


if __name__ == '__main__':
    from htutil import loggerInit
    loggerInit(logger)
    from htuno import getScriptContext
    XSCRIPTCONTEXT = getScriptContext()
    main()
