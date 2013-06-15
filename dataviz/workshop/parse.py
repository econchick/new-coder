import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build our data structure to return parsed_data
    parsed_data = []

    # header line
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip field -> row
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV
    opened_file.close()


    return parsed_data


def main(): 
    # Call parse() and give parameters
    new_data = parse(MY_FILE, ",")

    # Let’s see what the data looks like!
    print new_data

if __name__ == "__main__":
    main()










