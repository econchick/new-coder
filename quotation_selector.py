
import random
import time

class QuotationSelector(object):

    def __init__(self):
        random.seed(time.localtime())
        quotes_file = open('quotes.txt')
        self.quotes = quotes_file.readlines()

    def select(self):
        index = random.randint(0, len(self.quotes) - 1)
        return self.quotes[index]