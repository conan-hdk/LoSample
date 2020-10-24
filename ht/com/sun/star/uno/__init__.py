# -*- coding: utf-8 -*-
# ＵＴＦ－８

import unohelper

from com.sun.star.uno import XInterface
from logging import getLogger
logger = getLogger(__name__)


class xInterface(unohelper.Base, XInterface):

    def queryInterface(self, aType):
        logger.debug('Interface.queryInterface.aType:{}'.format(dir(aType)))
        return XInterface.queryInterface(self, aType)

    def acquire(self):
        XInterface.acquire(self)

    def release(self):
        XInterface.release(self)


__all__ = ['xInterface']
