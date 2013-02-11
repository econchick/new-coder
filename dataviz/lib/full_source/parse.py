#! -*- coding: utf-8 -*-

"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.
"""

import csv


# Put the full path to your CSV/Excel file here
my_file = "/Users/lynnroot/MyDev/new-coder/dataviz/lib/data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses raw CSV file to JSON-like objects"""

    # open a CSV file with the appropriate delimiter (comma, tab, other char)
    csv_data = csv.reader(open(raw_file), delimiter=delimiter)

    # set up an empty list
    parsed_data = []

    # skip over the first line of the file for the headers
    fields = csv_data.next()

    # iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data += [dict(zip(fields, row))]

    return parsed_data


def main():
    # Call our parse function and give it the needed parameters
    parsed_data = parse(my_file, ",")

    # Let's see what the data looks like!
    print parsed_data


if __name__ == "__main__":
    main()
