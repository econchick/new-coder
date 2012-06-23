import logging

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

from quotation_selector import QuotationSelector


class TalkBackBot(irc.IRCClient):

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
        send_to = channel
        if self.factory.settings.NICKNAME.startswith(channel) or \
                channel.startswith(self.factory.settings.NICKNAME):
            trigger_found = True
            send_to = user.split('!')[0]
        else:
            for trigger in self.factory.settings.TRIGGERS:
                if msg.lower().find(trigger) >= 0:
                    trigger_found = True
                    break

        if trigger_found:
            quote = self.factory.quotation.select()
            self.msg(send_to, quote)
            logging.info("sent message to %s:\n\t%s" % (send_to, quote))


class TalkBackBotFactory(protocol.ClientFactory):

    def __init__(self, settings):
        self.settings = settings
        self.channel = self.settings.CHANNEL
        self.quotation = QuotationSelector(self.settings.QUOTES_FILE)

    def buildProtocol(self, addr):
        bot = TalkBackBot()
        bot.factory = self
        bot.nickname = self.settings.NICKNAME
        bot.realname = self.settings.REALNAME
        return bot

    def clientConnectionLost(self, connector, reason):
        logging.info("connection lost, reconnecting")
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        logging.info("connection failed: %s" % (reason))
        reactor.stop()