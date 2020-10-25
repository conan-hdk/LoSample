# -*- coding: utf-8 -*-
# ＵＴＦ－８

import unohelper
from ht.com.sun.star.uno import xInterface

from com.sun.star.script.provider import XScriptContext


class ScriptContext(xInterface, XScriptContext):

    def __init__(self, ctx):
        self.ctx = ctx

    def getComponentContext(self):
        return self.ctx

    def getDesktop(self):
        return self.ctx.getServiceManager().createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)

    def getDocument(self):
        return self.getDesktop().getCurrentComponent()


__all__ = ['ScriptContext']
