import unittest
import platform_pricing as pp
from StringIO import StringIO


class CsvTest(unittest.TestCase):
    def test_data(self):
        """
        If all the required data is present (name, abbreviation, adapted_price,
        original_price, year) the output should contain it all.
        """
        data = [
            dict(name='Console1', abbreviation='C1', year=1994,
                 adapted_price=123, original_price=99),
            dict(name='Console2', abbreviation='C2', year=2000,
                 adapted_price=124, original_price=100)
        ]
        output = StringIO()
        pp.generate_csv(data, output)
        self.assertEquals('''Abbreviation,Name,Year,Price,Adapted price\r\nC1,Console1,1994,99,123\r\nC2,Console2,2000,100,124\r\n''',
                          output.getvalue())


class PlatformFiltering(unittest.TestCase):
    """
    A couple of tests to make sure that invalid platforms are filtered out
    before affecting the result.
    """

    def test_valid(self):
        self.assertTrue(pp.is_valid_dataset({
            'name': 'Console',
            'original_price': 123,
            'release_date': '2012-12-12 12:12:12',
            'abbreviation': 'C1'
        }))

    def test_missing_price(self):
        self.assertFalse(pp.is_valid_dataset({
            'name': 'Console',
            'release_date': '2012-12-12 12:12:12',
            'abbreviation': 'C1'
        }))

    def test_missing_release_date(self):
        self.assertFalse(pp.is_valid_dataset({
            'name': 'Console',
            'original_price': 123,
            'abbreviation': 'C1'
        }))

    def test_missing_name(self):
        self.assertFalse(pp.is_valid_dataset({
            'original_price': 123,
            'release_date': '2012-12-12 12:12:12',
            'abbreviation': 'C1'
        }))

    def test_missing_abbreviation(self):
        self.assertFalse(pp.is_valid_dataset({
            'name': 'Console',
            'original_price': 123,
            'release_date': '2012-12-12 12:12:12',
        }))


class CpiDataTest(unittest.TestCase):
    def test_year_range(self):
        """
        Tests that first_year and last_year are set appropriately.
        """
        data = StringIO('''DATE          VALUE
1981-01-01   100.000
2012-02-01   123.000''')
        cpi = pp.CpiData()
        cpi.load_from_file(data)
        self.assertEquals(1981, cpi.first_year)
        self.assertEquals(2012, cpi.last_year)
    
    def test_year_in_range(self):
        data = StringIO('''DATE          VALUE
1981-01-01   100.000
2012-02-01   123.000''')
        cpi = pp.CpiData()
        cpi.load_from_file(data)
        self.assertEquals(123, cpi.get_adapted_price(100, 1981, current_year=2012))

    def test_year_before_range(self):
        data = StringIO('''DATE          VALUE
1981-01-01   100.000
2012-02-01   123.000''')
        cpi = pp.CpiData()
        cpi.load_from_file(data)
        self.assertEquals(123, cpi.get_adapted_price(100, 1980, current_year=2012))

    def test_current_year(self):
        data = StringIO('''DATE          VALUE
1981-01-01   100.000
2012-02-01   123.000''')
        cpi = pp.CpiData()
        cpi.load_from_file(data)
        self.assertEquals(100, cpi.get_adapted_price(100, 2012, current_year=2012))

    def test_year_after_range(self):
        data = StringIO('''DATE          VALUE
1981-01-01   100.000
2012-02-01   123.000''')
        cpi = pp.CpiData()
        cpi.load_from_file(data)
        self.assertEquals(100, cpi.get_adapted_price(100, 2013, current_year=2012))
