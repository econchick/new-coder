import unittest
import mock

from talkback.bot import TalkBackBotFactory
import test_settings

class TestTalkBackBot(unittest.TestCase):
    
    CHANNEL = "#testchannel"
    QUOTE = "Nobody minds having what is too good for them. ~ Jane Austen"
    USERNAME = "tester"

    def setUp(self):
        super(TestTalkBackBot, self).setUp()
        factory = TalkBackBotFactory(test_settings)
        self.bot = factory.buildProtocol(None)
        self.bot.msg = mock.MagicMock()

    def test_privmsg__no_trigger(self):
        """Shouldn't send a quote if message does not match trigger"""
        self.bot.privmsg(self.USERNAME, self.CHANNEL, "hi")
        self.assertFalse(self.bot.msg.called)

    def test_privmsg__with_trigger(self):
        """Should send a quote if message matches trigger"""
        self.bot.privmsg(self.USERNAME, self.CHANNEL, "twss")
        self.bot.msg.assert_called_with(self.CHANNEL, self.QUOTE)

    def test_privmsg__private_message(self):
        """ For private messages, should send quote directly to user """
        self.bot.privmsg(self.USERNAME, test_settings.NICKNAME, "hi")
        self.bot.msg.assert_called_with(self.USERNAME, self.QUOTE)

    def test_privmsg__private_message_truncated_nickname(self):
        """ Send quote directly to user even if name is truncated """
        self.bot.privmsg(self.USERNAME, test_settings.NICKNAME[:-2], "hi")
        self.bot.msg.assert_called_with(self.USERNAME, self.QUOTE)

    def test_privmsg__private_message_alternate_nickname(self):
        """ Send quote directly to user even if using alternate nickname """
        self.bot.privmsg(self.USERNAME, test_settings.NICKNAME + '_', "hi")
        self.bot.msg.assert_called_with(self.USERNAME, self.QUOTE)
        