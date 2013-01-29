TalkBackBot
================================

Are you tired of "That's what she said" jokes? Then this bot is for you!
It will join a specified channel and respond to the configured trigger phrases
with what she really said, i.e. a quotation from a notable woman. It will also
respond to any direct message with a quotation.

Many quotes taken from this excellent resource:
http://womenshistory.about.com/library/qu/blqulist.htm

Setup
------------

::

I highly recommend both virtualenv and virtualenvwrapper. If you have them
installed, you can create a sandbox for talkbackbot as simply as:
    mkvirtualenv talkbackbot

To install requirements:
    workon talkbackbot
    pip install -r requirements.txt


Usage
-----

::

    # Activate your virtualenv
    workon talkbackbot

    # Copy settings.py.EXAMPLE to settings.py and edit to suit yourself
    cp settings.py.EXAMPLE settings.py
    vim settings.py

    # Run the bot
    twistd twsrs

    # Stop the bot
    kill `cat twistd.pid`

    # Run unit tests
    nosetests

