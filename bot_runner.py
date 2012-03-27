
import os
import signal

from daemon import Daemon
import settings
from twisted.internet import reactor, ssl


class BotDaemon(Daemon):

    def __init__(self, pid_file, bot_factory):
        super(BotDaemon, self).__init__(pid_file)
        self.factory = bot_factory

    def run(self):
        factory = self.factory(settings)
        if settings.USE_SSL:
            reactor.connectSSL(settings.HOST, settings.PORT, factory,
                ssl.ClientContextFactory())
        else:
            reactor.connectTCP(settings.HOST, settings.PORT, factory)
        reactor.run()


class BotRunner(object):

    def __init__(self, pid_file, bot_factory):
        self.pid_file = pid_file
        self.bot_factory = bot_factory

    def start(self):
        bot = BotDaemon(self.pid_file, self.bot_factory)
        bot.start()

    def stop(self):
        try:
            pid_file = open(self.pid_file)
        except IOError:
            print "pid file '%s' not found; perhaps the process is not running"\
                % (self.pid_file)
            return
        pid = pid_file.read()
        pid_file.close()
        os.kill(int(pid), signal.SIGHUP)
        os.remove(self.pid_file)
        
    def restart(self):
        self.stop()
        self.start()
