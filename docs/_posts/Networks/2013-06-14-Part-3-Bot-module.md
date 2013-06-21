---
layout: post.html
title: "Part 3: Bot.py Module"
tags: [Network]
url: "/~drafts/networks/part-3/"
---

Writing our `bot.py` module.

### Module Setup


Then we will import selected modules from Twisted.  There’s no expectation that you would know which modules from Twisted to import; this is just an introduction to the package’s vast capabilities in Networking.  In this package, we are taking advantage of Twisted’s `log` module for logging rather than using Python’s `logging` module, `protocol` module to create our bot factory (to be explain), as well as leverage Twisted’s `irc` module so we don’t reinvent the wheel.

<<<<<<< Updated upstream
Note that the order of import statements are alphabetical per [PEP-8](http://www.python.org/dev/peps/pep-0008/), Python’s style guide.
=======
Our last import will be the `QuotationSelector` class we wrote in our custom module, `quotation_selector`. 

Note the order of the import statements: standard library, third-party packages, then self-written modules, each alphabetical order within the three groupings.  The convention of ordering import statements this way is defined in Python’s style guide, [PEP-8](http://www.python.org/dev/peps/pep-0008/#imports).
>>>>>>> Stashed changes

```python
from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc
```


### scaffolding for bot.py module

We will be writing two classes: `TalkBackBot` and `TalkBackBotFactory`.  The factory class actually instantiates the bot, while the bot class defines the bot’s behavior.

Let’s first start off with the bot factory scaffolding with comments and docstrings:

```
# <--snip-->
class TalkBackBotFactory(protocol.ClientFactory):
    # instantiate the TalkBackBot IRC protocol

    def __init__(self, settings):
        """Initialize the bot factory with our settings."""

    def clientConnectionLost(self, connector, reason):
        """Reconnects IRC client to service if connection is lost."""
```

 The factory is in charge of creating/instantiating a protocol (here, the `TalkBackBot`).  With the bot factory, we inherit from Twisted’s `protocol.ClientFactory`.  This is so we can make use of creating a connection between our client and the protocol (our IRC connection), and handle any connection errors.

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
        """Called when the bot joins the channel."""


    def privmsg(self, user, channel, msg):
        """Called when the bot receives a message."""


# <--snip-->
```

The `TalkBackBot` class inherits from `irc.IRCClient` from the Twisted library.  This is so we can make use of functions like `connectionMade`, `signedOn`, etc, and define desired behavior.  

First, we’ll code out the bot factory, then return to the bot itself.


### TalkBackBotFactory class

**TODO**: Why isn't it `protocol = TalkBackBot()`? We first instantiate our protocol with `protocol = TalkBackBot`.  

Notice that in our import statements, we didn’t import our `settings.ini` file.  When we run our program, the plugin that we write (detailed in [Part 4]({{ get_url('/networks/part-4')}})) will pick up the file.  With that, our `TalkBackBotFactory` will initialize with the settings:

```python
# <--snip-->

def __init__(self, channel, nickname, realname, quotes, triggers):
    """Initialize the bot factory with our settings."""
    self.channel = channel
    self.nickname = nickname
    self.realname = realname
    self.quotes = quotes
    self.triggers = triggers

# <--snip-->

```

The initialization of our factory is pretty self explanatory – the factory is created with settings that are defined in `settings.ini`.  When we write our plugin in [part 4]({{ get_url('/networks/part-4')}}), we will code out the passing of those configuration settings into our factory.

Next, we define a function called `clientConnectionLost`:

```python
def clientConnectionLost(self, connector, reason):
    """Reconnects IRC client to service if connection is lost."""
    log.msg("connection lost, reconnecting: {!r}".format(reason))
    connector.connect()
```

This function does two things:

1. Logs the issue when the connection is lost to our server.
2. Calls `connector.connect()` to reconnect IRC client to the service.

In our `log.msg()` line, we pass in a string, `"connection lost, reconnecting {!r}"` followed by the string method, `format`.  The curly braces, `{}`, indicate a replacement field.  This field will be populated by `reason`, an argument passed into our `clientConnectionLost` function.  

The `!r` tells `format` to call the function `repr()` (rather than the `str()` function) on `reason`.  If we were to do `!s` instead, `format` would *not* include quotes around `reason`, [like so](http://docs.python.org/2/library/string.html#formatexamples):

```python
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"
```

To understand `repr()` versus `str()` better, [StackOverflow](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python) as a great explanation.


### TalkBackBot class
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