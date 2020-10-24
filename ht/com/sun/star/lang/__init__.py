# -*- coding: utf-8 -*-
# ＵＴＦ－８

import unohelper

import ht.com.sun.star.uno
from com.sun.star.lang import (XEventListener, DisposedException)
from logging import getLogger
logger = getLogger(__name__)


class xEventListener(ht.com.sun.star.uno.xInterface, XEventListener):

    def disposing(self, Source):
        logger.debug('EventListener.disposing.Source:{},{}'.format(Source.typeName, dir(Source)))

