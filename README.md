# [new-coder](http://newcoder.io)

New Coder tutorials: 5 life jackets to throw the new coder

* Data Visualization
* Web Scraping
* APIs
* Networking
* GUI

General directory layout:

	├── <Project>/
	│   ├── README.md
	│   ├── requirements.txt
	│   ├── lib/
	│   ├── tests/  # only for more advanced tutorials

## CONTRIBUTING


*PLEASE* – When editing tutorial or full source code, please edit the documentation to go along with it within the `website` folder (and vice-versa).

When writing documentation, please use [smart quotes](http://en.wikipedia.org/wiki/Quotation_mark_glyphs). :)


## Documentation Build Instructions

Documentation is essentially the website itself.  Simply install requirements, run the build command within `website` directory:


```bash
$ mkvirtualenv newcoder-website
(newcoder-website) $ cd website
(newcoder-website) $ pip install -r requirements.txt
```

To build the site:

```bash
(newcoder-website) $ mynt gen -f _site
```

To serve the site locally:

```bash
(newcoder-website) $ mynt serve _site
```

And navigate to `localhost:5000`.

I’ve included a simple script that combines the two above commands:

```bash
(newcoder-website) $ ./_local.sh
```

If you get a `permission denied` message, you may need to change the file mode in order to run the `_local.sh` with the `./` preceeding:

```bash
(newcoder-website) $ chmod +x _local.sh
(newcoder-website) $ ./_local.sh
```
