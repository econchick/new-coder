#!/usr/bin/python

import requests

CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'

class CPIData(object):
    """
    Abstraction of the CPI data provided by FRED. 
    This stores internally only one value per year.
    """

    def __init__(self):
        # Each year available to the dataset will end up as a simple key-value
        # pari within this dict. We don't really need any order here so going
        # with a plain old dictionary is the best approach.
        self.year_cpi = {}
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url. 
        The downloaded file can also be saved into a location for later 
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.
        """
        # We don't really know how much data we are going to get here, so
        # it is recommended to just keep as little data as possible in memory
        # at all times. Setting stream to True will defer the downloading of the
        # body until the content is explicitly accessed. It's being used here in
        # conjunction with .raw to make the response a file-like-object. Since 
        # requests supports gzip-compression by default we just disable  gzip 
        # by setting "Accept-Encoding" to None.
        fp = requests.get(url, stream=True,
                          headers={'Accept-Encoding': None}).raw

        # If we did not pass in a save_as_file parameter, just return the raw
        # data we got from the previous line.
        if save_as_file is None:
            return self.load_from_file(fp)

        # Otherwise, write it to the desired file.
        else:
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(butter)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""
        current_year = None
        year_cpi = []
        import pdb; pdb.set_trace()
        for line in fp:
            # The content of the file starts with a header line which starts
            # with the string "DATE ". Until we reach this line, we can skip
            # ahead.
            while not line.startswith("Date "):
                # Logic error here? If it was a continue statement then the loop
                # would begin from the beginning, but it seems like this doesn't
                # do anything. The code below is executed regardless of what the
                # line starts with. 
                pass

    def get_adjusted_price(self, price, year, current_year=None):
        """
        Returns the adapted price from a given year compared to what current
        year has been specified.
        """

def main():
    """This function handles the actual logic of this script."""

    # Grab CPI/Inflation data.

    # Grab API/game platform data.

    # Figure out the current price of each platform.
    # This will require looping through each game platform we received, and 
    # calculate the adjusted price based on the CPI data we also received.
    # During this point, we should also validate our data so we do not skew
    # our results.

    # Generate a plot/bar graph for the adjusted price data.

    # Generate a CSV file to save for the adjusted price data.

if __name__ == '__main__':
    x = CPIData()
    x.load_from_url(CPI_DATA_URL)
