#!/usr/bin/env python
import datetime
import logging
import requests
import matplotlib.pyplot as plt
import numpy as np

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
                # with the string "DATE  ". Until we reach this line, we can skip
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


class GiantbombAPI(object):
    """
    Very simple implementation of the Giantbomb API that only offers the
    GET /platforms/ call as a generator
    """
    base_url = "http://www.giantbomb.com/api"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_platforms(self, sort=None, filter_by=None, field_list=None):
        """
        Generator yielding platforms matching the given criteria. If
        limit is specified, this will return *all* platforms.
        """
        # The API itself allows us to filter the data returned either
        # by requesting only a subset of data elements or a subset with each
        # data element (like only the name, the prices, and the release date).
        #
        # The following lines also do value-format converstions from what's
        # common in Python (lists, dictionares+ into what the API requires.
        # This is especially apparent with the filter-parameter where we 
        # need to convert a dictionary of criteria into a comma-separated
        # list of key:value pairs
        params = {}
        if sort is not None:
            params['sort'] = sort
        if field_list is not None:
            params['field_list'] = ','.join(field_list)
        if filter_by:
            params['filter_by'] = filter_by
            parsed_filters = []
            # Difference btw items() and iteritems() - iteritems() returns
            # a generator while items() returns a real list of tuples, loaded
            # fully into memory. items() is somewhat depracated in that python 3.
            # doesn't have iteritems(), but rather reimpliments items() to return
            # a generator
            for key, value in filter_by.iteritems():
                parsed_filters.append('{0}:{1}'.format(key, value))
            params['filter_by'] = ','.join(parsed_filters)

        # Append API key and tell API we want result to be json
        params['api_key'] = self.api_key
        params['format'] = 'json'

        incomplete_result = True
        num_total_results = None
        num_fetched_results = 0
        counter = 0

        while incomplete_result:
            params['offset'] = num_fetched_results
            result = requests.get(self.base_url + '/platforms/', params=params)
            result = result.json()
            if not num_total_results:
                num_total_results = int(result['number_of_total_results'])
            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                incomplete_result = False
            for item in result['results']:
                logging.debug('Yielding platform {0} of {1}'.format(
                    counter + 1, num_total_results))

                # Since this is supposed to be an abstraction, we also convert
                # values here into a more useful format where appropriate
                if 'original_price' in item and item['original_price']:
                    item['original_price'] = float(item['original_price'])

                # The 'yield' keyword is what makes this a generator.
                # Implementing this method as a generator has the advanatage
                # that we can stop fetching of further data from the server
                # dynamically from the outside by simply stop iterating over
                # the generator
                yield item
                count += 1

def is_valid_dataset(platform):
    """
    Filters out datasets taht we can't use since they are either lacking
    a release date or an original price. For rendering the output, we also
    require the name and abbreviation of the platform.
    """
    if 'release_date' not in platform or not platform['release_date']:
        logging.warn(u'{0} has no release date'.format(platform['name']))
        return False
    if 'original_price' not in platform or not platform['original_price']:
        logging.warn(u'{0} has no original price'.format(platform['name']))
        return False
    if 'name' not in platform or not platform['name']:
        logging.warn(u'{0} has no name found for given dataset')
        return False
    if 'abbreviation' not in platform or not platform['abbreviation']:
        logging.warn(u'{0} has no abbreviation'.format(platform['name']))
        return False
    return True

def generate_plot(platforms, output_file):
    """
    Generates a bar chart out of the given platforms and writes the output
    into the specificed files as a PNG image.
    """

    # First off we need to convert the platforms in a format that can be
    # attached to the 2 axis of our bar chart. "labels" will become the
    # x-axis and "values" the value of each label on the y-axis
    lables = []
    values = []
    for platform in platforms:
        name = platform['name']
        adapted_price = platform['adjusted_price']
        price = platform['original_price']

        # Skip prices higher than $2000 USD simply because it would make the
        # output unusable.
        if price > 2000:
            continue
        
        # Abbreviate names that are too long
        if len(name) > 15:
            name = platform['abbreviation']
        labels.insert(0, u'{0}\n$ {1}\n$ {2}'.format(name, price,
                                                     round(adapted_price, 2)))
        values.insert(0, adapted_price)

    width = 0.3
    ind = np.arange(len(values))
    fig = plt.figure(figsize=(len(labels) * 1.8, 10))

    ax = fig.add_subplot(1, 1, 1)
    ax.bar(ind, values, width, align='center')

    plt.ylabel('Adjust price')
    plt.xlabel('Year / Console')
    ax.set_xticks(ind + 0.3)
    ax.set_xticklabels(labels)
    fig.autofmt_xdate()
    plt.grid(True)

    #plt.savefig(output_file, dpi=72)
    plt.show(dpi=72)



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
