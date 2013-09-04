---
title: IRC Bot
layout: post.html
tags: [irc, network, networks]
url: "/~drafts/networks/intro/"
---


### The Project

This tutorial walks you through how to make an [IRC bot](http://en.wikipedia.org/wiki/Internet_Relay_Chat_bot) with [Twisted](http://twistedmatrix.com).  You will be introduced to testing, logging, an overview of how the internet works, as well as event-driven programming, different internet protocols, and making a portable application.

The project’s code is based off of [Jessamyn Smith](https://twitter.com/jessamynsmith)’s IRC bot – the [talkbackbot](https://github.com/jessamynsmith/talkbackbot), where if anyone says “That’s what she said” in an IRC channel, the bot replies with a notable quote from a woman (that’s what she really said!).

### Intro to IRC

IRC stands for Internet Relay Chat, and is a [protocol](http://en.wikipedia.org/wiki/Category:Internet_protocols) for live messaging over the internet.  Specifically, the IRC protocol is within the *application layer* (just a simple abstraction of types of protocols). Other examples of internet protocols within the application layer are [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), [IMAP](http://en.wikipedia.org/wiki/Internet_Message_Access_Protocol), [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [POP](http://en.wikipedia.org/wiki/Post_Office_Protocol), [SSH](http://en.wikipedia.org/wiki/Secure_Shell), among many others. 

IRC uses [TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol), Transmission Control Protocol (another protocol!).  TCP is within the *transport layer*, as opposed to application later.  Another popular transportation layer protocol is [UDP](http://en.wikipedia.org/wiki/User_Datagram_Protocol).

If you have heard of IRC before, you may think it’s an antiquated means of communication. Created in 1988, it remains one of the most popular protocols for instant messaging within many aspects of the tech community.

There are many IRC networks, the most popular in terms of users at peak hours are [freenode](http://freenode.net), [IRCNet](http://www.ircnet.org/), and [QuakeNet](http://www.quakenet.org/).  

[IRCHelp](http://www.irchelp.org/) is a great resource for learning IRC.  [PyLadies](http://pyladies.com) also has a great [introduction on how to setup and use IRC](http://www.pyladies.com/blog/irc-resources/).  Of the Python community, some frequent channels visited are #python, #django, #python-dev, #twisted, and of course, #pyladies, all on Freenode.

For more information, [Jessica McKellar](http://web.mit.edu/jesstess/) gave a great talk at PyCon 2013 about [How the Internet Works](http://pyvideo.org/video/1677/how-the-internet-works), with her slides [here](https://speakerdeck.com/pyconslides/the-internet-by-jessica-mckellar). She gives an overview of what happens when you click through your browser, what a protocol is, DNS, and generally how to communicate over the internet.

### Intro to Twisted

According to [Twisted](http://twistedmatrix.com/trac/)’s website, Twisted is an “event-driven networking engine written in Python”.  OK…what does that mean?

#### Event-driven programming

[Event-driven programming](http://en.wikipedia.org/wiki/Event-driven_programming) simply means that the flow of the program is determined by events.  Events may be a click of the mouse, a message from another program, a response from a server, etc. The primary activity is a _reaction_ to receiving a certain event(s).

Glyph, the author of Twisted, gave a great [talk on event-driven architecture](http://pyvideo.org/video/1681/so-easy-you-can-even-do-it-in-javascript-event-d) at PyCon 2013. He describes how to approach thinking about events and callbacks the right way.  Essentially, an event is just a function call that you asked for.  Glyph’s [slides](https://speakerdeck.com/pyconslides/so-easy-you-can-even-do-it-in-javascript-event-driven-architecture-for-regular-programmers-by-glyph?slide=113) encapsulates it well: 

* When a user clicks a button, then call this function.
* When a user answers this question, call this function.
* When a network answers a question, call this function.
* When a network sends me data, call this function.

#### Programming Paradigms

Some paradigms include [object-oriented](http://en.wikipedia.org/wiki/Object-oriented_programming), [imperative](http://en.wikipedia.org/wiki/Imperative_programming), and [functional](https://en.wikipedia.org/wiki/Functional_programming), all of which can use event-driven programming. If you are curious about how to employ different programming paradigms for different problems, check out [How to Design Programs](http://www.amazon.com/gp/product/0262062186/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0262062186&linkCode=as2&tag=roglyn-20).


### Intro to Logging


Logging is quite important for applications.  Transferring money, the black box on an airplane, cell phone bills - they all log actions to be referenced and checked later. As such, logging is quite important for developing, debugging, maintaining, and running systems and applications.

There is the `logging` module in Python’s standard library, and a great [how-to](http://docs.python.org/2/howto/logging-cookbook.html) write up for the `logging` module.

But Twisted has its own logging module, `log`. The initial reason that Twisted doesn’t use the `logging` module from the Python standard library is that the Twisted logging module predates the stdlib one.  There are many reasons that Twisted hasn’t moved to the stdlib logging module which you can read [here](http://twistedmatrix.com/trac/wiki/TwistedLogging).

You may start out simply adding `print` statements to your application, but this isn’t ideal for anything beyond a very basic script.  `print` does not allow you to set up different importance levels, e.g. `DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`, or `FAIL`; it's an all or nothing with `print`.

Identifying which level of importance to log a message at can get some getting use to.  Use the `debug` level for granular information, such as printing out variables that change within a for-loop:

```python
def some_awesome_function(items):
    for i, item in enumerate(items):
        # do some complex computation/iteration
        logger.debug('%s iteration, item=%s', i, item)
```

Use `info` for routines and such, like starting or connecting to a server:

```python
def start_IMAP_service():
    logger.info('Starting IMAP service at port %s ...', port)
    service.start()
    logger.info('IMAP Service is started')
```

Use `warn` for important events happen, but no error has occurred, like a password that was incorrectly inputted.  Finally, use `error` for when an exception is thrown, user isn’t found in the database, connectivity issue, etc.  As the admin of an application with a logging mechanism, you would setup your desired level of logs in some configuration for instance, if you only want to see errors, you would ideally set a configuration value to something like `debug_level=error`. 

These above examples use Python’s `logging` module.  For our tutorial, we’ll use Twisted’s `log` module, which has slightly different syntax when passing in log levels.


### Intro to Testing

Very similar to logging, testing is also quite important for your code base.  Writing tests in parallel to writing code is considered a good habit.  Submitting features and patches to projects without tests can be a big faux-pas. 

There are different types of testing, and with this tutorial we will focus on unit testing.

A unit test just focuses on one tiny bit of functionality to prove correct behavior based on inputs, and should be independent of other unit tests.

An example of a unit test using Pythons `unittest` module, taken from [python-guide.org](http://docs.python-guide.org/en/latest/writing/tests.html#unittest):

```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

The main part here is `assertEqual(fun(3), 4)`, where we feed `fun` the number `3`.  The test will pass if the return value of `fun(3) == 4`, else it will fail.

We will be using Twisted’s own unit testing framework that is built upon Python’s `unittest` module with the added ability to test event-driven code.

### Approaching the tutorial

We will first knock out the simple items by addressing the global variables/settings for our IRC bot.  We’ll then build a quick function to select quotes (a list of quotes can be found in the [GitHub repo](https://github.com/econchick/new-coder/blob/master/network/talkback/quotes.txt)).

Then we’ll approach the making of the bot module by first creating a class to create bots (a factory class), and then another class to define the behavior of the bot.  We will also write a quick plugin to easily create and start up our bot from the command line.

Lastly, we will write tests for the expected behavior of our talkback bot application.

All set? [Let’s begin with our setup!]( {{ get_url('/~drafts/networks/part-0')}})

