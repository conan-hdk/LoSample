# -*- coding: utf-8 -*-
# ＵＴＦ－８
'''
Created on 2014/10/17

@author: conan
'''

__all__ = ['getScriptContext', 'createUnoService' , 'createProperty']

# import time
import uno
import unohelper
import htuno.connectSub

__all__ = ['getScriptContext', ]


def createUnoService(serviceName, Context=None):
#    if Context == None:
    ctx = Context if Context != None else XSCRIPTCONTEXT.getComponentContext()
#    ctx = uno.getComponentContext()
#    ctx = uno.getComponentContext()
    sm = ctx.getServiceManager()
#    print(sm)
#    return sm.createInstance(serviceName)
#    inst = sm.createInstanceWithContext(serviceName, ctx)
    inst = sm.createInstance(serviceName)
#    print("{}:{}".format(serviceName,dir(inst)))
    return inst


from ht.com.sun.star.beans import PropertyValue


def createProperty(name, value):
    prop = PropertyValue()
    prop.Name = name
    prop.Value = value
    return prop


def getScriptContext():
    if 'XSCRIPTCONTEXT' not in globals():
        XSCRIPTCONTEXT = htuno.connectSub.getScriptContext()
    return XSCRIPTCONTEXT
#    return htuno.connectSub.getScriptContext()


def main():
    from pprint import pprint
    print(globals())
    pprint(globals())

    
if __name__ == '__main__':
    main()
