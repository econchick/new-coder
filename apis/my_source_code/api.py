#!/usr/bin/python

import datetime
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

    def load_from_url(self, url, save_as_file="cpi.dat"):
        """Loads data from a given url. 
        The downloaded file can also be saved into a location for later 
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.
        """
        fp = requests.get(url)

        with open(save_as_file, 'wb+') as out:
            for line in fp.iter_lines():
                out.write(line + '\n')

        # After the data has been written to a file, call load_from_file to 
        # populate the CPIData object with the data
        self.load_from_file(save_as_file)

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""
        current_year = None
        year_cpi = []
        data_reached = False
        with open(fp) as out:
            for line in out:
                # The content of the file starts with a header line which starts
                # with the string "DATE ". Until we reach this line, we can skip
                # ahead.
                if not data_reached:
                    if not line.startswith("DATE  "):
                        continue
                    else:
                        data_reached = True
                        continue
                
                # Remove the newline from the end of each line
                data = line.rstrip().split()

                # Extract the year
                year = int(data[0].split('-')[0])
                cpi = float(data[1])

                if self.first_year is None:
                    self.first_year = year
                self.last_year = year

                # The moment we reach a new year, we have to reset the CIP data
                # and calculate the average cpi for the year we just looped over.
                if current_year != year:
                    # This is just for when it first starts the loop, when
                    # current_year is still initialized at None
                    if current_year is not None:
                        self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                    year_cpi = []
                    current_year = year
                year_cpi.append(cpi)

            # We have to do the calculation oce again for the last year in the
            # dataset
            if current_year is not None and current_year not in self.year_cpi:
                self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)

    def get_adjusted_price(self, price, year, current_year=None):
        """
        Returns the adapted price from a given year compared to what current
        year has been specified.

        This is essentially is the calculated inflation for an item.
        """
        if current_year is None:
            current_year = datetime.datetime.now().year
        # If our data range doesn't provide a CPI for the given year, use
        # the edge data
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi

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
