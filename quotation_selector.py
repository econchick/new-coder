import random


class QuotationSelector(object):

    def __init__(self, quotes_filename):
        random.seed()
        quotes_file = open(quotes_filename)
        self.quotes = quotes_file.readlines()

    def select(self):
        index = random.randint(0, len(self.quotes) - 1)
        return self.quotes[index].strip()