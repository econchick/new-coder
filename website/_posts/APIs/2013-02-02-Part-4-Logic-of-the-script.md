---
layout: post.html
title: "Part 4: The Logic of the Script"
tags: [api, argparse, logging]
url: "/api/part-4/"
---

Parse the command-line arguments and create the main logic of the script flow.

### Argparse

When running a python file in the command line, Python has the ability to take arguments that are passed to the command line:

```bash
(APIProj)$ python a_python_file.py --debug --output-file ~/MyDocuments/MyLogs/python_file.log
```

Certainly, we’d need to put some logic into our script in order to be able to parse arguments.  Let’s think of all the arguments that we could possibly want to pass to our API Python script are:

* API key for Giantbomb
* path to CPI file
* URL to get CPI data (default will be our global `CPI_DATA_URL` we defined earlier)
* Path to CSV file which will contain the data output
* Path to PNG file which will contain the graphed data output
* Output level for logging (whether just informational, or debugging, etc)
* Maximum number of platforms we want to look at, if any


Python’s standard library has a great module, `argparse` that we’ll use.  We’ll create separate parsing function as a helper to our main function that we’ll write out after this.

First, import argparse,

```python
import argparse
```

then let’s define our parsing function, and use `argparse`’s `ArgumentParser` to initialize a `parser` class:

```python
def parse_args():
	parser = argparse.ArgumentParser()
```

The `ArgumentParser` class implicitly gives us an argument for free, the `-h` and `--help` flags for showing the usage of the script, `python platform_pricing.py [options] [args]`, as well as a list of available commands and their `help` strings we assign. 

We will need the os module.

```python
import os
```

Now we should add all the arguments that could possibly be passed through from the command line with the `add_argument` method that `ArgumentParser` class gives us:

```python
def parse_args():
	parser = argparse.ArgumentParser()
    parser.add_argument('--giantbomb-api-key', required=True,
                        help='API key provided by Giantbomb.com')
```

The first parameter that we feed to `add_argument` is the flag that is used in the command line:

```bash
(APIProj)$ python platform_pricing.py --giantbomb-api-key <YOUR_API_KEY>
```

We also tell `add_argument` that this is a required field by passing the `required=True` parameter. The `ArgumentParser` class will take care of erroring out for us if that argument isn't given in the command line.

Lastly, we pass in a string for our `help` parameter – this text will show whenever a user passes the `-h` or `--help` flag.

The rest of our arguments:

```python
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
```

Note that when running this script, you don’t have to have the output files, CSV or PNG, already created – just tell the script where you want it saved and what you want it saved as by giving it the full directory path and desired filename.

The Python docs have a great [tutorial](http://docs.python.org/2/howto/argparse.html) on how to use the `argparse` module if you’d like additional work on this module.


### Main function

The `CPIData` and `GiantbombAPI` classes have been defined with their methods, as well as functions `generate_plot`, `generate_csv`, and `is_valid_dataset`.  Let’s now make one `main()` function that runs whenever we call our `platform_pricing.py` file (with arguments) that instantiates (uses) everything.

We will be needing the logging module.

```python
import logging
```

We’ll first want to take care of the arguments passed through the command line by calling our `parse_args` function.

```python
def main():
    """This function handles the actual logic of this script."""
    opts = parse_args()

    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
```

Here, we also handle the level of logging – if the user uses the `--debug` flag (perhaps s/he wants extra level of detail of what is going on, or is troubleshooting), then we assign our `logging` variable a level of `DEBUG`, else, the default will be `INFO`.

Since we did not specify any file to save our logs to, it will just write our logging statement that we defined in `GiantbombAPI.get_platforms()` to the terminal when we run our Python program.

Next, we’ll instantiate both the `CPIData` class and the `GiantbombAPI` class and use some of the arguments that we parsed to pass the API key, the CPI URL (if we don't want to use the default defined in our global variable, `CPI_DATA_URL`, and CPI file (if we gave it a file).

We also print to the console – using the print _function_ imported from future (Python 3), rather than the print _keyword_ in Python 2 – that gives a disclaimer to the user what the script will be doing.

```python
	# <-- snip -->

    cpi_data = CPIData()
    gb_api = GiantbombAPI(opts.giantbomb_api_key)

    print ("Disclaimer: This script uses data provided by FRED, Federal"
           " Reserve Economic Data, from the Federal Reserve Bank of St. Louis"
           " and Giantbomb.com:\n- {0}\n- http://www.giantbomb.com/api/\n"
           .format(CPI_DATA_URL))

    if os.path.exists(opts.cpi_file):
        with open(opts.cpi_file) as fp:
            cpi_data.load_from_file(fp)
    else:
        cpi_data.load_from_url(opts.cpi_data_url, save_as_file=opts.cpi_file)
```

Now comes the part where the two classes interact. 

We need to iterate over each platform (up to the limit if one is set as an argument from the command line) to fetch the adjusted price (the de/inflated price of the platform) based on the data we grabbed from the FRED.  We build/append each piece of data to the `platforms` list.

We then take our `platforms` list and pass it to either `generate_plot` or `generate_csv`, depending on what arguments were passed from the command line.

```python
	# <-- snip -->

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
        adjusted_price = cpi_data.get_adjusted_price(price, year)
        platform['year'] = year
        platform['original_price'] = price
        platform['adjusted_price'] = adjusted_price
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
```

That’s all for our `main()` function – just the final boilerplate code at the tail end:

```python
if __name__ == '__main__':
    main()
```

### Try it yourself

In your terminal, with your `APIProj` virtual environment activated, and from within your API project directory, try your new script with different arguments (be sure to use your own directory paths instead of `~/Projects/new-coder/apis/*` unless you have that exact directory setup):

```bash
(APIProj)$ python platform_pricing.py --giantbomb-api-key [YOUR_KEY] --plot-file ~/Projects/new-coder/apis/my_plot.png
(APIProj)$ python platform_pricing.py --giantbomb-api-key [YOUR_KEY] --csv-file ~/Projects/new-coder/apis/my_csv.csv
(APIProj)$ python platform_pricing.py --giantbomb-api-key [YOUR_KEY] --plot-file ~/Projects/new-coder/apis/my_plot.png --csv-file ~/Projects/new-coder/apis/my_csv.csv
(APIProj)$ python platform_pricing.py --giantbomb-api-key [YOUR_KEY] --debug --limit 40 --csv-file ~/Projects/new-coder/apis/my_csv.csv
```


[APIs – Extended: &rarr;]({{ get_url("/api/extended/")}})