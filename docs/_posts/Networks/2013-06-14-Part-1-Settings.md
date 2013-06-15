---
layout: post.html
title: "Part 1: Settings"
tags: [Network]
url: "/~drafts/networks/part-1/"
---

Define our settings for our IRC bot.

### Module setup

If you remember from earlier tutorials, variables that are in all caps are meant to convey that they are global variables.  

For our `settings.py` module, we don’t need to import any special library or package.  We are simply defining the settings that we want our IRC bot to use.

First, our connection-specific settings:


```python
# IRC settings
HOST = "irc.freenode.net"
PORT = 6667
USE_SSL = False
CHANNEL = "#newcoder"
```

The `HOST` identifies which network we want to connect to.  You may remember from the [introduction]( {{ get_url("/networks/intro/")}}) that there are many IRC networks.  You can see that for our bot, we are electing to connect to [Freenode](http://freenode.net).

It’s not enough just to identify the `HOST`, or hostname, of the network we want to connect to.  We also need to declare the `PORT` we want to go through at the `HOST`.  There are conventions about which types of services use which ports.  Ports can range from 1 through 65535, but about 250 are reserved by convention for certain processes/protocols.  For instance, by default, HTTP uses port 80, and HTTPS uses 443.  POP listens on port 110, SMTP on 25, and IMAP on 143.  Here, freenode makes port 6667 available to bind to for IRC.

`USE_SSL` is a boolean that if true, will connect to the `HOST` over an [SSL](http://en.wikipedia.org/wiki/Transport_Layer_Security) connection.  SSL is designed to provide security when communicating over the internet and prevent eavesdropping and tampering. 

Lastly, the `CHANNEL` variable, a string that needs to start with `#`. This is the channel that the bot will join when connecting to Freenode.


Next, our bot-specific settings:

```
# Bot settings
NICKNAME = "whatshereallysaid"
REALNAME = "bot: provides quotations from notable women"
```

This is pretty self-explanatory.  The bot’s `NICKNAME` will show when it’s connected to Freenode, and its `REALNAME` will show when a user queries or requests more information about the bot itself (e.g. with the command, `/whois whatshereallysaid` within a chat window).

Now the last few global variables:

```python
# Trigger phrases, in lowercase
TRIGGERS = (
    "that's what she said",
    )

# Process settings
LOG_FILE = "./talkbackbot.log"
QUOTES_FILE = "talkback/quotes.txt"
```

The `TRIGGERS` is the phrase a user says to which the bot will respond.  It could be multiple phrases, but here, we only care about responding when someone says “that‘s what she said”.

The `LOG_FILE` and `QUOTES_FILE` is pretty self-explanatory as well.  The “./” in `LOG_FILE` means the current directory.  No need to actually create the log file now; once the program is ran, you will see it created.  


All set? Let’s continue with [crafting our quote selector &rarr;]( {{ get_url("/~drafts/networks/part-2/")}})