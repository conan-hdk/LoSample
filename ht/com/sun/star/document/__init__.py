# -*- coding: utf-8 -*-
# ＵＴＦ－８

import unohelper

import ht.com.sun.star.lang
from com.sun.star.document import XEventListener, XDocumentEventListener
from logging import getLogger
logger = getLogger(__name__)


class xEventListener(ht.com.sun.star.lang.xEventListener, XEventListener):

    def notifyEvent(self, Event):
        logger.debug('EventListener.notifyEvent.Event.EventName:{}'.format(Event.EventName))


class xDocumentEventListener(ht.com.sun.star.lang.xEventListener, XDocumentEventListener):

    def documentEventOccured(self, EventName, ViewController, Supplement):
        logger.debug('DocumentEventListener.notifyDocumentEvent.EventName:{}'.format(EventName))

