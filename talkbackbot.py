import logging

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

from quotation_selector import QuotationSelector
import settings


logging.basicConfig(filename=settings.LOG_FILE, level=logging.DEBUG)


class TalkBackBot(irc.IRCClient):
    password = settings.PASSWORD
    nickname = settings.NICKNAME
    realname = settings.REALNAME

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        logging.info("connectionMade")

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        logging.info("connectionLost")

    # callbacks for events

    def signedOn(self):
        """Called when bot has successfully signed on to server."""
        logging.info("Signed on")
        self.join(self.factory.channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        logging.info("[%s has joined %s]"
            % (self.nickname, self.factory.channel))

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""

        trigger_found = False
        for trigger in settings.TRIGGERS:
            if msg.lower().find(trigger) >= 0:
                trigger_found = True
                break

        if trigger_found:
            quote = self.factory.quotation.select()
            self.msg(channel, quote)
            logging.info("sent message:\n\t%s" % (quote))


class TalkBackBotFactory(protocol.ClientFactory):

    def __init__(self, channel):
        self.channel = channel
        self.quotation = QuotationSelector(settings.QUOTES_FILE)

    def buildProtocol(self, addr):
        p = TalkBackBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        logging.info("connection lost, reconnecting")
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        logging.info("connection failed: %s" % (reason))
        reactor.stop()