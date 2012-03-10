TalkBackBot
================================

Are you tired of "That's what she said" jokes? Then this bot is for you!
It will join a specified channel and respond to the configured trigger phrases
with what she really said, i.e. a quotation from a notable woman.

Installation
------------

::

    virtualenv .
    pip install -r requirements.txt


Usage
-----

::

    # Activate your virtualenv
    . bin/activate

    # Copy settings.py.EXAMPLE to settings.py and edit to suit yourself
    cp settings.py.EXAMPLE settings.py

    # Run the bot
    ./talkbackbot start

    # Stop the bot
    ./talkbackbot stop

