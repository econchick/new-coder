#! -*- coding: utf-8 -*-

"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.
Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy.numarray as na


my_file = "/Users/lynnroot/MyDev/new-coder/dataviz/lib/data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses raw CSV file to JSON-like objects"""
    csv_data = csv.reader(open(raw_file), delimiter=delimiter)
    parsed_data = []
    fields = csv_data.next()
    for row in csv_data:
        parsed_data += [dict(zip(fields, row))]

    return parsed_data


def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(my_file, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [
                  counter["Monday"], counter["Tuesday"],
                  counter["Wednesday"], counter["Thursday"],
                  counter["Friday"], counter["Saturday"],
                  counter["Sunday"]
                ]
    day_list = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

    # Assign the data to a plot
    plt.plot(data_list)

    # Create labels for our x-axis
    labels = tuple(day_list)

    # Assign labels to the plot
    plt.xticks(range(len(data_list)), labels)

    # Render the plot!
    plt.show()


def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(my_file, ",")
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

    # Render the graph!
    plt.show()


def main():
    visualize_days()  # once this window is closed, the next graph shows
    visualize_type()


if __name__ == "__main__":
    main()
