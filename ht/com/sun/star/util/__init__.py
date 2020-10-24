# -*- coding: utf-8 -*-
# ＵＴＦ－８

import unohelper

import ht.com.sun.star.lang
from com.sun.star.util import XCloseListener

from logging import getLogger
logger = getLogger(__name__)


class xCloseListener (ht.com.sun.star.lang.xEventListener, XCloseListener):

    def queryClosing(self, Source, GetsOwnership):
        logger.debug('CloseListener.queryClosing.Source:{}'.format(dir(Source)))
        pass

    def notifyClosing(self, Source):
        logger.debug('CloseListener.notifyClosing.Source:{}'.format(dir(Source)))
        pass

