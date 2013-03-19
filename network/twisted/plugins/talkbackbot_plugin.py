#!/usr/bin/env python
import logging

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.internet import ssl

from zope.interface import implements

import settings
from talkback.bot import TalkBackBotFactory

logging.basicConfig(filename=settings.LOG_FILE, level=logging.DEBUG)


class Options(usage.Options):
    optParameters = []


class BotServiceMaker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "twsrs"
    description = "IRC bot that provides quotations from notable women"
    options = Options

    def makeService(self, options):
        """
        Construct the talkbackbot TCP client
        """
        if settings.USE_SSL:
            bot = internet.SSLClient(settings.HOST, settings.PORT,
                TalkBackBotFactory(settings), ssl.ClientContextFactory())
        else:
            bot = internet.TCPClient(settings.HOST, settings.PORT,
                TalkBackBotFactory(settings))
        return bot


# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = BotServiceMaker()