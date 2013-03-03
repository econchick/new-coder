---
layout: post.html
title: "Part 1: Setup Raw Data"
tags: [api]
---

A walkthrough of grabbing raw data from publicly available information.

```python
from __future__ import print_function
```

You might be curious as to why we're importing a `print_function`, and why it's from `__future__`.  This is a gentle introduction of the differences between Python 2.x and Python 3.x.  In Python 3, `print()` is a function, while in Python 2, `print` is a keyword. For now, the difference is just that using `print` requires paretheses around what you are printing.

### CPI data

First, we'll grab the CPI data from the FRED.  We'll create a CPI class to initialize the CPI data, load data from the URL, load data from a file, and 
```python
import argparse
import datetime
import os
import logging
import urllib2

import matplotlib.pyplot as plt
import numpy as np
import requests
import tablib

CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'


class CpiData(object):
    """
    Abstraction of the CPI data provided by FRED. This stores internally only
    one value per year.
    """

    def __init__(self):
        self.year_cpi = {}
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """
        Loads data from a given url. The downloaded file can also be saved
        into a location for later re-use with the "save_as_file" parameter
        specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.
        """
        fp = urllib2.urlopen(url)
        if save_as_file is None:
            return self.load_from_file(fp)
        else:
            with open(save_as_file, 'w+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

    def load_from_file(self, fp):
        """
        Loads CPI data from a given file-like object.
        """
        reached_dataset = False
        current_year = None
        year_cpi = []
        for line in fp:
            if not reached_dataset:
                if line.startswith("DATE "):
                    reached_dataset = True
                continue
            data = line.rstrip().split()
            year = int(data[0].split("-")[0])
            cpi = float(data[1])

            if self.first_year is None:
                self.first_year = year
            self.last_year = year

            # The moment we reach a new year, we have to reset the CPI data
            # and calculate the average CPI of the current_year.
            if current_year != year:
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)

        # We have to do the calculation once again for the last year in the
        # dataset.
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)

    def get_adapted_price(self, price, year, current_year=None):
        if current_year is None:
            current_year = datetime.datetime.now().year
        # If our data range doesn't provide a CPI for the given year, use
        # the edge data.
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi


class GiantbombApi(object):
    """
    Very simple implementation of the Giantbomb API that only offers the
    GET /platforms/ call as a generator.

    Note that this implementation only exposes of the API what we really need.
    """

    base_url = 'http://www.giantbomb.com/api'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_platforms(self, sort=None, filter=None, field_list=None):
        """
        This yields platforms matching the given criteria. If no limit is
        specified, this will return *all* platforms.
        """
        incomplete_result = True
        num_total_results = None
        num_fetched_results = 0
        counter = 0
        params = {}
        if filter is not None:
            params['filter'] = filter
        if sort is not None:
            params['sort'] = sort
        if field_list is not None:
            params['field_list'] = ','.join(field_list)
        if filter is not None:
            filters = ','.join(['{0}:{1}'.format(*itm)
                                for itm in filter.iteritems()])
            params['filter'] = filters
        params['api_key'] = self.api_key
        params['format'] = 'json'

        while incomplete_result:
            params['offset'] = num_fetched_results
            result = requests.get(self.base_url + '/platforms/',
                                  params=params)
            result = result.json()
            if num_total_results is None:
                num_total_results = int(result['number_of_total_results'])
            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                incomplete_result = False
            for item in result['results']:
                logging.debug("Yielding platform {0} of {1}".format(
                    counter + 1,
                    num_total_results))

                # Since this is supposed to be an abstraction, we also convert
                # values here into a more useful format where appropriate.
                if 'original_price' in item and item['original_price']:
                    item['original_price'] = float(item['original_price'])

                yield item
                counter += 1


def generate_plot(platforms, output_file):
    """
    Generates a bar chart out of the given platforms and writes the output
    into the specified file as PNG image.
    """
    labels = []
    values = []
    for platform in platforms:
        name = platform['name']
        adapted_price = platform['adapted_price']
        price = platform['original_price']

        # Skip prices higher than 2000 USD
        if price > 2000:
            continue

        # If the name of the platform is too long, replace it with the
        # abbreviation
        if len(name) > 15:
            name = platform['abbreviation']
        labels.insert(0, u"{0}\n$ {1}\n$ {2}".format(name, price,
                                                     round(adapted_price, 2)))
        values.insert(0, adapted_price)

    # Let's define the width of each bar and the size of the resulting graph.
    width = 0.3
    ind = np.arange(len(values))
    fig = plt.figure(figsize=(len(labels) * 1.8, 10))

    # Generate a subplot and put our values onto it.
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(ind, values, width, align='center')

    # Format the X and Y axis labels
    plt.ylabel('Adapted price')
    plt.xlabel('Year / Console')
    ax.set_xticks(ind + 0.3)
    ax.set_xticklabels(labels)
    fig.autofmt_xdate()
    plt.grid(True)

    plt.savefig(output_file, dpi=72)


def generate_csv(platforms, output_file):
    """
    Writes the given platforms into a CSV file specified by the output_file
    parameter.
    
    The output_file can either be the path to a file or a file-like object.
    """
    dataset = tablib.Dataset(headers=['Abbreviation', 'Name', 'Year', 'Price',
                                      'Adapted price'])
    for p in platforms:
        dataset.append([p['abbreviation'], p['name'], p['year'],
                        p['original_price'], p['adapted_price']])
    if isinstance(output_file, basestring):
        with open(output_file, 'w+') as fp:
            fp.write(dataset.csv)
    else:
        output_file.write(dataset.csv)


def is_valid_dataset(platform):
    """
    Filters out datasets that we can't use since they are either lacking
    a release date or an original price. For rendering the output we also
    require the name and abbreviation of the platform
    """
    if 'release_date' not in platform or not platform['release_date']:
        logging.warn(u"{0} has no release date".format(platform['name']))
        return False
    if 'original_price' not in platform or not platform['original_price']:
        logging.warn(u"{0} has no original price".format(platform['name']))
        return False
    if 'name' not in platform or not platform['name']:
        logging.warn(u"No platform name found for given dataset")
        return False
    if 'abbreviation' not in platform or not platform['abbreviation']:
        logging.warn(u"{0} has no abbreviation".format(platform['name']))
        return False
    return True


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--giantbomb-api-key', required=True,
                        help='API key provided by Giantbomb.com')
    parser.add_argument('--cpi-file',
                        default=os.path.join(os.path.dirname(__file__),
                                             'CPIAUCSL.txt'),
                        help='Path to file containing the CPI data (also acts'
                             ' as target file if the data has to be downloaded'
                             'first).')
    parser.add_argument('--cpi-data-url', default=CPI_DATA_URL,
                        help='URL which should be used as CPI data source')
    parser.add_argument('--debug', default=False, action='store_true',
                        help='Increases the output level.')
    parser.add_argument('--csv-file',
                        help='Path to CSV file which should contain the data'
                             'output')
    parser.add_argument('--plot-file',
                        help='Path to the PNG file which should contain the'
                             'data output')
    parser.add_argument('--limit', type=int,
                        help='Number of recent platforms to be considered')
    opts = parser.parse_args()
    if not (opts.plot_file or opts.csv_file):
        parser.error("You have to specify either a --csv-file or --plot-file!")
    return opts


def main():
    """
    This function handles the actual logic of this script.
    """
    opts = parse_args()

    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    cpi_data = CpiData()
    gb_api = GiantbombApi(opts.giantbomb_api_key)
    if os.path.exists(opts.cpi_file):
        with open(opts.cpi_file) as fp:
            cpi_data.load_from_file(fp)
    else:
        cpi_data.load_from_url(opts.cpi_data_url, save_as_file=opts.cpi_file)

    print ("Disclaimer: This script uses data provided by FRED, Federal Reserve Economic Data, from the Federal Reserve Bank of St. Louis and Giantbomb.com:\n- " + CPI_DATA_URL + "\n- http://www.giantbomb.com/api/\n")

    platforms = []
    counter = 0

    # Now that we have everything in place, fetch the platforms and calculate
    # their current price in relation to the CPI value.
    for platform in gb_api.get_platforms(sort='release_date:desc',
                                         field_list=['release_date',
                                                     'original_price', 'name',
                                                     'abbreviation']):
        # Some platforms don't have a release date or price yet. These we have
        # to skip.
        if not is_valid_dataset(platform):
            continue

        year = int(platform['release_date'].split('-')[0])
        price = platform['original_price']
        adapted_price = cpi_data.get_adapted_price(price, year)
        platform['year'] = year
        platform['original_price'] = price
        platform['adapted_price'] = adapted_price
        platforms.append(platform)

        # We limit the resultset on this end since we can only here check
        # if the dataset actually contains all the data we need and therefor
        # can't filter on the API level.
        if opts.limit is not None and counter + 1 >= opts.limit:
            break
        counter += 1

    if opts.plot_file:
        generate_plot(platforms, opts.plot_file)
    if opts.csv_file:
        generate_csv(platforms, opts.csv_file)


if __name__ == '__main__':
    main()
```