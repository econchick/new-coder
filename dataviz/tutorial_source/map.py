#!usr/bin/env python

"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part III: Take the data we parsed earlier and create a different format
for Google Maps. The first two functions are helper-functions.  First one
creates a KML Document, and the second parses each data point into KML-
format. The last function then uses these to helper-functions to create
a KML file for upload.
"""

import xml.dom.minidom

import parse as p


def create_document(title, description=''):
    """Create the overall KML document."""

    # Initialization of an XML doc
    doc = xml.dom.minidom.Document()

    # Define as a KML-type XML doc
    kml = doc.createElement('kml')

    # Pull in common attributes and set it for our doc
    kml.setAttribute('xmlns', 'http://www.opengis.net/kml/2.2')
    doc.appendChild(kml)

    # Create common elements that Google will read/plot
    document = doc.createElement('Document')
    kml.appendChild(document)
    docName = doc.createElement('name')
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

    # Create a new KML doc with our previously-defined
    # create_document() function
    kml_doc = create_document("Crime map", "Plots of Recent SF Crime")

    # Get the specific DOM element that we created with create_document()
    # Returns a list, so call the first one
    document = kml_doc.documentElement.getElementsByTagName("Document")[0]

    # Iterate over our data to create KML document
    for line in data_file:
        # Parses the data into a dictionary
        placemark_info = {'longitude': line['X'],
                       'latitude': line['Y'],
                       'name': line['Category'],
                       'description': line['Descript'],
                       'date': line['Date']}

        # Avoid null values for lat/long
        if placemark_info['longitude'] == "0":
            continue

        # Calls create_placemark() to parse line of data into KML-format
        placemark = create_placemark(placemark_info)

        # Adds the placemark we just created to the KML doc
        document.appendChild(placemark.documentElement)

    # Now that all data is parsed in KML-format, write to a file so we
    # can upload it to maps.google.com
    with open('file_sf.kml', 'w') as f:
        f.write(kml_doc.toprettyxml(indent="  ", encoding='UTF-8'))


def main():
    data = p.parse(p.MY_FILE, ",")

    return create_gmap(data)

if __name__ == "__main__":
    main()
