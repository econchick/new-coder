import hashlib
import unittest
import datetime
from game_platforms import create_dipity_signature, parse_giantbomb_date


class DipitySignatureTests(unittest.TestCase):
    def test_no_parameters(self):
        hash = hashlib.md5()
        hash.update('123')
        digest = hash.hexdigest()
        self.assertEquals(digest, create_dipity_signature({}, '123'))

    def test_with_parameters(self):
        hash = hashlib.md5()
        hash.update('123p1v1p2v2')
        digest = hash.hexdigest()
        self.assertEquals(digest, create_dipity_signature(
            {'p2': 'v2', 'p1': 'v1'},
            '123'))


class GiantbombDateTests(unittest.TestCase):
    def test_release_date_parsing(self):
        inp = "1985-10-21 00:00:00"
        expected = datetime.datetime(1985, 10, 21, 0, 0, 0)
        self.assertEquals(expected, parse_giantbomb_date(inp))
