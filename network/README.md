TalkBackBot
===========

Are you tired of “That’s what she said” jokes? Then this bot is for you!
It will join a specified channel and respond to the configured trigger phrases
with what she really said, i.e. a quotation from a notable woman. It will also
respond to any direct message with a quotation.

Many quotes taken from this excellent resource:
http://womenshistory.about.com/library/qu/blqulist.htm

Setup
-----

I highly recommend both virtualenv and virtualenvwrapper to manage the
environments for your different python projects.

::

    # Create a virtualenv
    mkvirtualenv talkbackbot

    # Install requirements
    workon talkbackbot
    pip install -r requirements.txt

Usage
-----

::

    # Activate your virtualenv
    workon talkbackbot

    # Copy settings.ini.EXAMPLE to settings.ini and edit to suit yourself
    cp settings.ini.EXAMPLE settings.ini
    vim settings.ini

    # Run the bot
    twistd -n twsrs

    # OR if you have 'make' installed
    make run

    # Optionally, you can set the config file
    twistd -n twsrs -c some-other-file.ini

    # Stop the bot
    <Ctrl-C>

    # Run unit tests
    trial tests

    # OR if you have 'make' installed
    make cov
