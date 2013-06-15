---
layout: post.html
title: "Part 3: Bot.py Module"
tags: [Network]
url: "/~drafts/networks/part-3/"
---

Writing our `bot.py` module.

### Module Setup

With our bot, we will log every action that the bot makes, so we will take advantage of the `logging` module in Python’s standard library.  

Then we will import selected modules from Twisted.  There’s no expectation that you would know which modules from Twisted to import; this is just an introduction to the package’s vast capabilities in Networking.

Our last import will be the `QuotationSelector` class we wrote in our custom module, `quotation_selector`. 

Note the order of the import statements: standard library, third-party packages, then self-written modules, each alphabetical order within the three groupings.

```python
import logging

from twisted.internet import reactor, protocol
from twisted.words.protocols import irc

from quotation_selector import QuotationSelector
```


### scaffolding for bot.py module

We will be writing two classes: `TalkBackBot` and `TalkBackBotFactory`.  The factory class actually instantiates the bot, while the bot class defines the bot’s behavior.

Let’s first start off with the bot factory scaffolding:

```python
# <--snip-->

class TalkBackBotFactory(protocol.ClientFactory):

    def __init__(self, settings):
        """Initialize the bot factory with settings and quote files."""

    def buildProtocol(self, addr):
        """Returns a bot based off of settings file."""

    def clientConnectionLost(self, connector, reason):
        """Reconnects IRC client to service if connection is lost."""

    def clientConnectionFailed(self, connector, reason):
        """Stops the reactor/event loop if client connection cannot be made."""

```

 The factory is in charge of creating/instantiating a protocol (here, the `TalkBackBot` in the `buildProtocol` function).  With the bot factory, we inherit from Twisted’s `protocol.ClientFactory`.  This is so we can make use of creating a connection between our client and the protocol (our IRC connection), and handle any connection errors.

 Now our `TalkBackBot` scaffolding:


```python
# <--snip-->

class TalkBackBot(irc.IRCClient):

    def connectionMade(self):
    """Called when a connection is made."""

    def connectionLost(self, reason):
    """Called when a connection is lost."""

    # callbacks for events

    def signedOn(self):
        """Called when bot has successfully signed on to server."""


    def joined(self, channel):
        """This will get called when the bot joins the channel."""


    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""


# <--snip-->
```

The `TalkBackBot` class inherits from `irc.IRCClient` from the Twisted library.  This is so we can make use of functions like `connectionMade`, `signedOn`, etc, and define desired behavior.  

First, we’ll code out the bot factory, then return to the bot itself.


### TalkBackBotFactory class

Notice that in our import statements, we didn’t import our `settings` module.  When we run our program, we will pass the settings file as an argument (detailed in [Part 4]({{ get_url('/networks/part-4')}})).  With that, our `TalkBackBotFactory` will initialize with the settings file:

```python
# <--snip-->

def __init__(self, settings):
    """Initialize the bot factory with settings and quote files."""
    self.settings = settings
    self.channel = self.settings.CHANNEL
    self.quotation = QuotationSelector(self.settings.QUOTES_FILE)

# <--snip-->

```

Notice that we also refer to the `QuotationSelector` class we wrote, which will pull a random quote from the `QUOTES_FILE` that is defined in our settings file, and assign it to `self.quotation`. 

Next, we’ll create a bot.  Notice it calls `TalkBackBot()` – we will write this class once we finish the Factory.

```python
# <--snip-->

def buildProtocol(self, addr):
    """Returns a bot based off of settings file."""
    bot = TalkBackBot()
    bot.factory = self
    bot.nickname = self.settings.NICKNAME
    bot.realname = self.settings.REALNAME
    return bot

```



**TODO**:

* clientConnectionLost/Failed
* logging
* make a bot (bot behavior)
  * functions
    * connection made
    * connection lost
      * how is this different from the Factory connection lost/failed functions?
    * signed on
    * joined
    * private message (response from within channel or private ping)
* why `__init__.py` within `network/talkback/` directory


One bit before our tests: [our custom twisted plugin &rarr;]( {{ get_url("/~drafts/networks/part-4/")}})