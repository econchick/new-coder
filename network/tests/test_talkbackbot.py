from twisted.test import proto_helpers
from twisted.trial import unittest

from talkback.bot import TalkBackBotFactory


QUOTE = "Nobody minds having what is too good for them. ~ Jane Austen"


class FakePicker(object):
    """Always return the same quote."""
    def __init__(self, quote):
        self._quote = quote

    def pick(self):
        return self._quote


class TestTalkBackBot(unittest.SynchronousTestCase):
    _channel = "#testchannel"
    _username = "tester"
    _us = 'tbb'

    def setUp(self):
        factory = TalkBackBotFactory(
            self._channel,
            self._us,
            'Jane Doe',
            FakePicker(QUOTE),
            ['twss'],
        )
        self.bot = factory.buildProtocol(('127.0.0.1', 0))
        self.fake_transport = proto_helpers.StringTransport()
        self.bot.makeConnection(self.fake_transport)
        self.bot.signedOn()
        self.bot.joined(self._channel)
        self.fake_transport.clear()

    def test_privmsgNoTrigger(self):
        """Shouldn't send a quote if message does not match trigger"""
        self.bot.privmsg(self._username, self._channel, "hi")
        self.assertEqual('', self.fake_transport.value())

    def test_privmsgWithTrigger(self):
        """Should send a quote if message matches trigger"""
        self.bot.privmsg(self._username, self._channel, "twss")
        self.assertEqual(
            'PRIVMSG {channel} :{username}: {quote}\r\n'.format(
                channel=self._channel, username=self._username, quote=QUOTE
            ),
            self.fake_transport.value())

    def test_privmsgAttribution(self):
        """If someone attributes the bot in public, they get a public response."""
        self.bot.privmsg(self._username, self._channel, self._us + ': foo')
        self.assertEqual(
            'PRIVMSG {channel} :{username}: {quote}\r\n'.format(
                channel=self._channel, username=self._username, quote=QUOTE
            ),
            self.fake_transport.value())

    def test_privmsgPrivateMessage(self):
        """For private messages, should send quote directly to user"""
        self.bot.privmsg(self._username, self._us, "hi")
        self.assertEqual(
            'PRIVMSG {username} :{quote}\r\n'.format(
                username=self._username, quote=QUOTE
            ),
            self.fake_transport.value()
        )
