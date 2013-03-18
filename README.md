new-coder
=========

New Coder tutorials: 5 life jackets to throw the new coder

* Data Visualization
* Web Scraping
* APIs
* Networking
* GUI

Directory layout:

	├── <Project>/
	│   ├── README.md
	│   ├── requirements.txt
	│   ├── lib/
	│   │   ├── full_source/
	│   │   ├── tutorial_source/
	│   ├─── tests/
	│   │   ├── full_tests/
	│   │   ├── tutorial_tests/

Documentation Build Instructions
==================

Simple install requirements, run the build command within `docs` directory

    pip install -r docs/requirements.txt
    mynt gen docs build
    (cd build && python -m SimpleHTTPServer)


CONTRIBUTING
============

PLEASE – When editing tutorial or full source code, please edit the documentation to go along with it within the `docs` folder (and vis-versa.

When writing documentation, please use [smart quotes](http://en.wikipedia.org/wiki/Quotation_mark_glyphs).


TODOs
=====

1. Network/IRC bot tutorial language
2. Sudoku/GUI tutorial language
5. Add better tags for subjects that are covered in tutorial parts (e.g. Generators, Iterators, classes, etc).
6. Learn anchoring for Mynt/Markdown
7. Remove the opening of the dataviz files in the tutorial to not "give away the answers"!