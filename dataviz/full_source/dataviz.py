#!/usr/bin/env python

"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.
"""
from collections import Counter

import argparse
import csv
import matplotlib.pyplot as plt
import numpy.numarray as na
import xml.dom.minidom


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


def create_document(title, description=''):
    """Create the overall KML document."""

    # Initial XML doc
    doc = xml.dom.minidom.Document()

    # Define as a KML-type XML talk
    kml = doc.createElement('kml')

    # Pull in common attributes
    kml.setAttribute('xmlns', 'http://www.opengis.net/kml/2.2')
    doc.appendChild(kml)

    # Create common elements that Google will read/plot
    document = doc.createElement('Document')
    kml.appendChild(document)
    docName = doc.createElement('title')
    document.appendChild(docName)
    docName_text = doc.createTextNode(title)
    docName.appendChild(docName_text)
    docDesc = doc.createElement('description')
    document.appendChild(docDesc)
    docDesc_text = doc.createTextNode(description)
    docDesc.appendChild(docDesc_text)
    return doc


def create_placemark(address):
    """Generate the KML Placemark for a given address.

    This is the function that takes the info from the
    file we parse at the end of this script.

    """

    # Create an initial XML document
    doc = xml.dom.minidom.Document()

    # Create elements for Placemark and add to our new doc
    pm = doc.createElement("Placemark")
    doc.appendChild(pm)
    name = doc.createElement("name")
    pm.appendChild(name)
    name_text = doc.createTextNode('%(name)s' % address)
    name.appendChild(name_text)
    desc = doc.createElement("description")
    pm.appendChild(desc)
    desc_text = doc.createTextNode('Date: %(date)s, %(description)s' % address)
    desc.appendChild(desc_text)
    pt = doc.createElement("Point")
    pm.appendChild(pt)
    coords = doc.createElement("coordinates")
    pt.appendChild(coords)
    coords_text = doc.createTextNode('%(longitude)s,%(latitude)s' % address)
    coords.appendChild(coords_text)
    return doc


def create_gmap(data_file):
    """Creates Google Maps KML Doc.

    Returns a KML file to be uploaded at maps.google.com.
    Navigate to 'My places' -> 'Create Map' -> 'Import' to
    upload the file and see the data.

    """

    # Initialize a new KML doc with our previously-defined
    # create_document() function
    kml_doc = create_document("SF Crime Map")

    # Get the specific DOM element that we created with create_document()
    # Returns a list, so call the first one
    document = kml_doc.documentElement.getElementsByTagName("Document")[0]

    # Iterate over our data to create KML document
    for line in data_file:
        # Parses the data into a dictionary
        coordinates = {'longitude': line['X'],
                       'latitude': line['Y'],
                       'name': line['Category'],
                       'description': line['Descript'],
                       'date': line['Date']
                       }

        # Avoid null values for lat/long
        if coordinates['longitude'] == "0":
            continue

        # Calls create_placemark() to parse line of data into KML-format
        placemark = create_placemark(coordinates)

        # Adds the placemark we just created to the KML doc
        document.appendChild(placemark.documentElement)

    # Now that all data is parsed in KML-format, write to a file so we
    # can upload it to maps.google.com
    with open('file_sf.kml', 'w') as f:
        f.write(kml_doc.toprettyxml(indent="  ", encoding='UTF-8'))


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
        create_gmap(data)

if __name__ == "__main__":
    main()
