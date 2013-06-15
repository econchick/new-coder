---
title: IRC Bot
layout: post.html
tags: [irc, network, networks]
url: "/~drafts/networks/intro/"
---
## Intro

### The Project

This tutorial walks you through how to make an [IRC bot](http://en.wikipedia.org/wiki/Internet_Relay_Chat_bot) with [Twisted](http://twistedmatrix.com).  You will be introduced to testing, logging, an overview of how the internet works, as well as event-driven programming, different internet protocols, and making a portable application.

The project’s code is based off of [Jessamyn Smith](https://twitter.com/jessamynsmith)’s IRC bot – the [talkbackbot](https://github.com/jessamynsmith/talkbackbot), where if anyone says “That’s what she said” in an IRC channel, the bot replies with a notable quote from a woman (that’s what she really said!).

### Intro to IRC

IRC stands for Internet Relay Chat, and is a [protocol](http://en.wikipedia.org/wiki/Category:Internet_protocols) for live messaging over the internet.  Specifically, the IRC protocol is within the *application layer* (just a simple abstraction of types of protocols). Other examples of internet protocols within the application layer are [HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), [IMAP](http://en.wikipedia.org/wiki/Internet_Message_Access_Protocol), [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), [POP](http://en.wikipedia.org/wiki/Post_Office_Protocol), [SSH](http://en.wikipedia.org/wiki/Secure_Shell), among many others. 

IRC uses [TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol), Transmission Control Protocol (another protocol!).  TCP is within the *transport layer*, as opposed to application later.  Another popular transportation layer protocol is [UDP](http://en.wikipedia.org/wiki/User_Datagram_Protocol).

If you have heard of IRC before, you may think it’s an antiquated means of communication. Created in 1988, it remains one of the most popular protocols for instant messaging within many aspects of the tech community.

There are many IRC networks, the most popular in terms of users at peak hours are [freenode](http://freenode.net), [IRCNet](http://www.ircnet.org/), and [QuakeNet](http://www.quakenet.org/).  

[IRCHelp](http://www.irchelp.org/) is a great resource for learning IRC.  [PyLadies](http://pyladies.com) also has a great [introduction on how to setup and use IRC](http://www.pyladies.com/blog/irc-resources/).  Of the Python community, some frequent channels visited are #python, #django, #python-dev, #twisted, and of course, #pyladies, all on Freenode.

### Intro to Twisted

According to [Twisted](http://twistedmatrix.com/trac/)’s website, Twisted is an “event-driven networking engine written in Python”.  OK…what does that mean?

#### Event-driven programming

[Event-driven programming](http://en.wikipedia.org/wiki/Event-driven_programming) simply means that the flow of the program is determined by events.  Events may be a click of the mouse, a message from another program, a response from a server, etc. The primary activity is a _reaction_ to receiving a certain event(s).

A good description of event-driven programming can be found in an article at [Linux Journal](http://www.linuxjournal.com/article/7871) by Ken Kinder:

> Have you ever been standing in the express lane of a grocery store, buying a single bottle of water, only to have the customer in front of you challenge the price of an item, causing you and everyone behind you to wait five minutes for the price to be verified? 
>
> Plenty of explanations of asynchronous programming exist, but I think the best way to understand its benefits is to wait in line with an idle cashier. If the cashier were asynchronous, he or she would put the person in front of you on hold and conduct your transaction while waiting for the price check. Unfortunately, cashiers are seldom asynchronous. 
>
> In the world of software, however, event-driven servers make the best use of available resources, because there are no threads holding up valuable memory waiting for traffic on a socket. Following the grocery store metaphor, a threaded server solves the problem of long lines by adding more cashiers, while an asynchronous model lets each cashier help more than one customer at a time.


Other paradigms include [object-oriented](http://en.wikipedia.org/wiki/Object-oriented_programming), [imperative](http://en.wikipedia.org/wiki/Imperative_programming), and [function-level](http://en.wikipedia.org/wiki/Function-level_programming).  If you are curious about how to employ different programming paradigms for different problems, check out [How to Design Programs]("http://www.amazon.com/gp/product/0262062186/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0262062186&linkCode=as2&tag=roglyn-20").


### Intro to Logging

Logging is essentially a paper trail for your codebase. For instance, if you transfer money between accounts, there are records of activity. Implementing logging in your code helps you monitor, debug, and develop your application.  

For something simple the following:

```python
print "Adding two numbers."
two = 1 + 1
print "The result is: %s." % two
print "Adding a third number."
two += 3
print "The new result is: %s." % two
print "Done adding."
```

print statements are sufficient. But if you were to litter your code with print statements for the following tutorial, it would get way too messy and inefficient.  Also, all `print` statements go to [stdout](http://docs.python.org/2/tutorial/inputoutput.html) (a.k.a standard output, which will feed to your console), which can get cumbersome when data is also printed to stdout.

In this tutorial, we will get familiar with Python’s `logging` module that comes in the standard library.  With this module, will be able to configure where our logging messages print to (e.g. written/saved to a .log file, to the console, etc).  We will also be able to configure the level in which we log.  Perhaps we only want to see critical errors, or we want to see more verbose logs.

### Intro to Testing

On top of writing a bot for IRC, we’re going to write tests to make sure our bot behaves the way we expect.  We will be writing unit tests, a type of tests where each individual blocks of code (e.g. a function) are tested separately. The goal is to have a test for each function/procedure written, giving you 100% test coverage.

Tests also are another form of documentation (but don’t skip writing documentation!). They reveal the expected behavior of each function/class/module.  Tests should pass when the input is valid, and should not pass when invalid.  

In this tutorial, you will explore the `unittest` module within Python’s standard library, as well as how to approach writing unit tests for your Python code.

### Approaching the tutorial

We will first knock out the simple items by addressing the global variables/settings for our IRC bot.  We’ll then build a quick function to select quotes (a list of quotes can be found in the [GitHub repo](https://github.com/econchick/new-coder/blob/master/network/talkback/quotes.txt)).

Then we’ll approach the making of the bot module by first creating a class to create bots (a factory class), and then another class to define the behavior of the bot.  We will also write a quick plugin to easily create and start up our bot from the command line.

Lastly, we will write tests for the expected behavior of our talkback bot application.

All set? [Let’s begin with our setup!]( {{ get_url('/~drafts/networks/part-0')}})

