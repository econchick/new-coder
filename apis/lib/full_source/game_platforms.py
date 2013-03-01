"""
This is a very simple example of how you can use web APIs to let completely
distinct web apps play nicely together. In this example we are interested in
getting a timeline of all video game platform release dates.

To achieve this we tap into the API of Giantbomb.com, extract all the platforms
from it and put them onto a timeline created on Dipity.com.

Before you can use this script, you have to get an API key from Giantbomb
(http://api.giantbomb.com/) and an API key and an API secret from Dipity
(http://www.dipity.com/developer/register). These you then have to pass
to this script as commandline arguments::

    python game_platforms.py --giantbomb-api-key=123 --dipity-api-key=123 --dipity-api-secret=123

This will then create a new timeline in your account named
"Video game platforms" from the data fetched from giantbomb.com.
"""
from __future__ import print_function
import datetime
import argparse
import requests
import hashlib
import logging


def main():
    """
    This is where the main execution takes place.
    """
    opts = parse_args()
    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Now that this whole bulk is out of the way, let's create a timeline
    timeline_id = create_timeline(opts.dipity_api_key, opts.dipity_api_secret,
        opts.timeline_name, description=opts.timeline_description)

    # Once we have a timeline id, we can start fetching platforms and create
    # events for them on the timeline.
    for idx, platform in enumerate(fetch_platforms(opts.giantbomb_api_key)):
        # There are also platforms that haven't been released yet which we have
        # to skip.
        if not ('release_date' in platform and platform['release_date']):
            logging.info("{0} has not yet been released".format(
                platform['name']))
            continue

        title = platform['name']
        link_url = platform['site_detail_url']
        timestamp = parse_giantbomb_date(platform['release_date'])
        create_timeline_event(timeline_id, opts.dipity_api_key,
            opts.dipity_api_secret, title, link_url, timestamp)


def parse_args():
    """
    Parses the commandline arguments like API keys, titles etc. using argparse.
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--giantbomb-api-key',
        required=True,
        help="API key used to communicate with Giantbomb's API")
    argparser.add_argument('--dipity-api-key', required=True,
        help="API key used to communicate with Dipity's API")
    argparser.add_argument('--dipity-api-secret', required=True,
        help="API secret used to communicate with Dipity's API")
    argparser.add_argument('--debug', action='store_true', default=False,
        help="Verbose log output")
    argparser.add_argument("--timeline-name", default="Video game platforms",
        help="Sets the title of the generated timeline")
    argparser.add_argument('--timeline-description',
        default="Data provided by giantbomb.com",
        help="Sets the description of the generated timeline")

    return argparser.parse_args()


def fetch_platforms(api_key):
    """
    Fetches all video game platforms from Giantbomb.com and returns them
    as a generator of objects.

    Since giantbomb has a limit of 100 result elements per response, we will
    have do multiple requests to their API and pass an offset with each request.
    """
    incomplete_result = True
    num_total_results = None
    num_fetched_results = 0
    counter = 0
    while incomplete_result:
        logging.debug("Fetching platforms with offset {0}".format(
            num_fetched_results))
        result = requests.get('http://api.giantbomb.com/platforms/', params={
            'api_key': api_key,
            'fields': 'name,abbreviation,release_date,site_detail_url',
            'format': 'json',
            'limit': 100,
            'offset': num_fetched_results
            }).json()
        num_total_results = result['number_of_total_results']
        num_fetched_results += result['number_of_page_results']
        if num_fetched_results >= num_total_results:
            incomplete_result = False
        for item in result['results']:
            logging.info("Yielding platform {0} of {1}".format(counter + 1,
                num_total_results))
            yield item
            counter += 1


def create_timeline(api_key, api_secret, name, description=None):
    """
    This method creates a timeline on Dipity and returns the newly created
    timeline's id.
    """
    params = {
        'key': api_key,
        'public': 'false',
        'title': name
    }
    if description is not None:
        params['description'] = description
    params['sig'] = create_dipity_signature(params, api_secret)
    resp = requests.post('http://api.dipity.com/rest/timelines', data=params,
        headers={'Accept': 'application/json'})

    # requests can raise an exception if we get a response status that is in
    # the 400 or 500 range.
    resp.raise_for_status()

    return resp.headers['location'].split('/')[-1]


def create_timeline_event(timeline_id, api_key, api_secret, title, link_url,
        timestamp):
    """
    Creates a new event on Dipity and attaches it to the timeline.
    """
    # First we have to create an event with the data we got from the caller.
    params = {
        'key': api_key,
        'title': title,
        'link_url': link_url,
        'timestamp': timestamp.isoformat('T') + 'Z'
    }
    params['sig'] = create_dipity_signature(params, api_secret)
    resp = requests.post('http://api.dipity.com/rest/events', data=params,
        headers={'Accept': 'application/json'})
    resp.raise_for_status()
    event_id = resp.headers['location'].split('/')[-1]

    # And now we have to attach this event to the timeline we created before
    params = {
        'key': api_key,
        'event_id': event_id
    }
    params['sig'] = create_dipity_signature(params, api_secret)
    resp = requests.post(
        'http://api.dipity.com/rest/timelines/{0}/events'.format(timeline_id),
        data=params, headers={'Accept': 'application/json'})
    resp.raise_for_status()


def create_dipity_signature(params, secret):
    """
    Dipity requires 2 special parameters besides those specific to the actual
    API method:

    1. key: the API key you got when registering for a developer account
    2. sig: a signature for the whole request.

    This method generates said signature.
    """
    raw_sig = [secret]

    # Now we have to operated on the parameter list, sorted by the parameter
    # name. The name and the value have to be appended to the raw signature.
    sorted_params = sorted(params.items(), cmp=lambda a, b: cmp(a[0], b[0]))
    for p in sorted_params:
        # The API key must not be part of the signature!
        if p[0] == 'key':
            continue
        raw_sig.append(p[0])
        raw_sig.append(p[1])

    # The signature itself is the MD5 digest of the raw signature (concatenated
    # into a string).
    hash = hashlib.md5()
    hash.update((''.join(raw_sig)).encode('utf-8'))
    return hash.hexdigest()


def parse_giantbomb_date(dt):
    """
    Returns a date string as provided by Giantbomb's API as native datetime
    object.
    """
    return datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    main()
