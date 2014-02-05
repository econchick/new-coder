#!/usr/bin/env python

"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.
"""
from collections import Counter

import argparse
import csv
import geojson
import matplotlib.pyplot as plt
import numpy.numarray as na


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data


def visualize_days(data_file):
    """Visualize data by day of week"""

    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Days.png".  This is our graph!
    plt.savefig("Days.png")

    # Close figure
    plt.clf()


def visualize_type(data_file):
    """Visualize data by category in a bar graph"""

    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = na.array(range(len(labels))) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x- and y-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    plt.yticks(range(0, max(counter.values()), 5))

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Type.png".  This is our graph!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()


def create_map(data_file):
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com.  Just copy the output file and
    paste into a new Gist, then create either a public or
    private gist.  GitHub will automatically render the GeoJSON
    file as a map.
    """

    # Define type of GeoJSON we're creating
    geo_map = {"type": "FeatureCollection"}

    # Define empty list to collect each point to graph
    item_list = []

    # Iterate over our data to create GeoJSOn document.
    # We're using enumerate() so we get the line, as well
    # the index, which is the line number.
    for index, line in enumerate(data_file):

        # Skip any zero coordinates as this will throw off
        # our map.
        if line['X'] == "0" or line['Y'] == "0":
            continue

        # Setup a new dictionary for each iteration.
        data = {}

        # Assigne line items to appropriate GeoJSON fields.
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Add data dictionary to our item_list
        item_list.append(data)

    # For each point in our item_list, we add the point to our
    # dictionary.  setdefault creates a key called 'features' that
    # has a value type of an empty list.  With each iteration, we
    # are appending our point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # Now that all data is parsed in GeoJSON write to a file so we
    # can upload it to gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--csvfile',
                            help="Parses the given CSV/Excel file. The full\
                            path to the file is needed.",
                            type=str, required=True)
    arg_parser.add_argument('--delimiter',
                            help="Delimiter of the Input File",
                            type=str, default=",")
    arg_parser.add_argument('--type',
                            help="Visualize data over days of the week,\
                            type frequency,\ or Google Maps",
                            choices=["Days", "Type", "Map"],
                            type=str, required=True)
    # Returns a dictionary of keys = argument flag, and value = argument
    args = vars(arg_parser.parse_args())

    # Parse data
    data = parse(args['csvfile'], args['delimiter'])

    # Call appropriate visualization function
    if args['type'] == 'Days':
        visualize_days(data)
    elif args['type'] == "Type":
        visualize_type(data)
    else:
        create_map(data)

if __name__ == "__main__":
    main()
