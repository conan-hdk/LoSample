# -*- coding: utf-8 -*-
# ＵＴＦ－８
'''
Created on 2014/12/12

@author: conan
'''


class _constCellFlags(object):
    from com.sun.star.sheet.CellFlags import (VALUE, DATETIME, STRING, ANNOTATION, FORMULA, HARDATTR, STYLES, OBJECTS, EDITATTR, FORMATTED,) 


class cellflags(object):
    '''
    classdocs
    '''

    @property
    def VALUE(self):
        return _constCellFlags.VALUE

    @property
    def DATETIME(self):
        return _constCellFlags.DATETIME

    @property
    def STRING(self):
        return _constCellFlags.STRING

    @property
    def ANNOTATION(self):
        return _constCellFlags.ANNOTATION

    @property
    def FORMULA(self):
        return _constCellFlags.FORMULA

    @property
    def HARDATTR(self):
        return _constCellFlags.HARDATTR

    @property
    def STYLES(self):
        return _constCellFlags.STYLES

    @property
    def OBJECTS(self):
        return _constCellFlags.OBJECTS

    @property
    def EDITATTR(self):
        return _constCellFlags.EDITATTR

    @property
    def FORMATTED(self):
        return _constCellFlags.FORMATTED


CellFlags = cellflags()


def main():
    pass


if __name__ == '__main__':
    main()
