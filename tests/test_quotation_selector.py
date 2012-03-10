import os
import unittest

from quotation_selector import QuotationSelector

class TestQuotationSelector(unittest.TestCase):

    QUOTE1 = "A fool without fear is sometimes wiser than an angel with fear. ~ Nancy Astor"
    QUOTE2 = "You don't manage people, you manage things. You lead people. ~ Grace Hopper"

    def setUp(self):
        super(TestQuotationSelector, self).setUp()

    def test_select(self):
        selector = QuotationSelector(os.path.join(os.getcwd(),
            "tests/test_quotes.txt"))

        quote = selector.select()

        self.assertTrue(quote in (self.QUOTE1, self.QUOTE2),
            "Got unexpected quote: '%s'" % (quote))