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

Simple install requirements, run the build command within `docs` directory. 

You will need a C compiler: [GCC](http://gcc.gnu.org/) or [clang](http://clang.llvm.org/).  To test if you have either GCC or clang, type `gcc` or `clang` into your terminal. If you get an error that says “command not found” then follow the install instructions for your OS:

* Mac: 
	* You will need [XCode](http://developer.apple.com/xcode). Once you have XCode on your machine, you will need to navigate to **Preferences** –> **Downloads** –> and select **Command Line Tools** to download & install.
* Fedora: `sudo yum install gcc python-devel`
* Ubuntu: `sudo apt-get install build-essential python-dev` – you may need to run `sudo apt-get update` first.

Once the compiler is set up:

    pip install -r docs/requirements.txt
    mynt gen docs build
    (cd build && python -m SimpleHTTPServer)


CONTRIBUTING
============

PLEASE – When editing tutorial or full source code, please edit the documentation to go along with it within the `docs` folder (and vice versa).

When writing documentation, please use [smart quotes](http://en.wikipedia.org/wiki/Quotation_mark_glyphs).


TODOs
=====

1. Network/IRC bot tutorial language
2. Sudoku/GUI tutorial language
5. Add better tags for subjects that are covered in tutorial parts (e.g. Generators, Iterators, classes, etc).
6. Learn anchoring for Mynt/Markdown
7. Remove the opening of the dataviz files in the tutorial to not "give away the answers"!
