import os

from twisted.trial import unittest

from talkback.quote_picker import QuotePicker


class TestQuotePicker(unittest.TestCase):
    QUOTE1 = (
        "A fool without fear is sometimes wiser than an angel with fear. "
        "~ Nancy Astor"
    )
    QUOTE2 = (
        "You don't manage people, you manage things. You lead people. "
        "~ Grace Hopper"
    )

    def test_pick(self):
        picker = QuotePicker(
            os.path.join(os.path.dirname(__file__), "test_quotes.txt")
        )
        quote = picker.pick()
        self.assertIn(quote, (self.QUOTE1, self.QUOTE2),
                      "Got unexpected quote: '%s'" % (quote))
