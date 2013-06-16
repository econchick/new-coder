# -*- test-case-name: tests.test_quote_picker -*-

from random import choice


class QuotePicker(object):

    def __init__(self, quotesFilename):
        with open(quotesFilename) as f:
            self.quotes = f.readlines()

    def pick(self):
        return choice(self.quotes).strip()
