# [new-coder](http://newcoder.io)

New Coder tutorials: 5 life jackets to throw the new coder

* Data Visualization
* Web Scraping
* APIs
* Networking
* GUI

Genearl directory layout:

	├── <Project>/
	│   ├── README.md
	│   ├── requirements.txt
	│   ├── lib/
	│   ├─── tests/  # only for more advanced tutorials

## CONTRIBUTING


*PLEASE* – When editing tutorial or full source code, please edit the documentation to go along with it within the `website` folder (and vice-versa).

When writing documentation, please use [smart quotes](http://en.wikipedia.org/wiki/Quotation_mark_glyphs). :)


## Documentation Build Instructions

Documentation is essentially the website itself.  Simple install requirements, run the build command within `website` directory.

You will need a C compiler: [GCC](http://gcc.gnu.org/) or [clang](http://clang.llvm.org/).  To test if you have either GCC or clang, type `gcc` or `clang` into your terminal. If you get an error that says “command not found” then follow the install instructions for your OS:

* Mac:
	* You will need [XCode](http://developer.apple.com/xcode). Once you have XCode on your machine, you will need to navigate to **Preferences** –> **Downloads** –> and select **Command Line Tools** to download & install.
* Fedora: `sudo yum install gcc python-devel`
* Ubuntu: `sudo apt-get install build-essential python-dev` – you may need to run `sudo apt-get update` first.

Once the compiler is set up:

    pip install -r website/requirements.txt
    mynt gen website build
    (cd build && python -m SimpleHTTPServer)

