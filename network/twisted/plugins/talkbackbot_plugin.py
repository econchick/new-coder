from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer

from talkback.bot import TalkBackBotFactory
from talkback.quote_picker import QuotePicker


class Options(usage.Options):
    optParameters = [
        ['config', 'c', 'settings.ini', 'Configuration file.'],
    ]


class TalkBackBotService(Service):
    _bot = None

    def __init__(self, client, factory):
        self._client = client
        self._factory = factory

    def startService(self):
        def connected(bot):
            self._bot = bot

        def failure(err):
            log.err(err, _why='Could not connect to specified server.')
            from twisted.internet import reactor
            reactor.stop()

        return (
            self._client.connect(self._factory)
            .addCallbacks(connected, failure)
        )

    def stopService(self):
        if self._bot and self._bot.transport.connected:
            self._bot.transport.loseConnection()


@implementer(IServiceMaker, IPlugin)
class BotServiceMaker(object):
    tapname = "twsrs"
    description = "IRC bot that provides quotations from notable women"
    options = Options

    def makeService(self, options):
        """
        Construct the talkbackbot TCP client
        """
        from twisted.internet import reactor
        config = ConfigParser()
        config.read([options['config']])
        triggers = [
            trigger.strip()
            for trigger
            in config.get('talkback', 'triggers').split('\n')
            if trigger.strip()
        ]
        quotes = QuotePicker(config.get('talkback', 'quotesFile'))

        return TalkBackBotService(
            clientFromString(reactor, config.get('irc', 'endpoint')),
            TalkBackBotFactory(
                config.get('irc', 'channel'),
                config.get('irc', 'nickname'),
                config.get('irc', 'realname'),
                quotes,
                triggers
            )
        )

# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = BotServiceMaker()
