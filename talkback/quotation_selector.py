from random import choice


class QuotationSelector(object):

    def __init__(self, quotes_filename):
        with open(quotes_filename) as quotes_file:
            self.quotes = quotes_file.readlines()

    def select(self):
        return choice(self.quotes).strip()