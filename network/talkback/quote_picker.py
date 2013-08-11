# -*- test-case-name: tests.test_quote_picker -*-

from random import choice


class QuotePicker(object):

    def __init__(self, quotesFilename):
        """Initialize our QuotationPicker class"""
        with open(quotesFilename) as f:
            self.quotes = f.readlines()

    def pick(self):
        """Return a random quote."""
        return choice(self.quotes).strip()
