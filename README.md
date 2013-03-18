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
	│   ├── docs/
	│   │   ├── full_docs/
	│   │   ├── tutorial_docs/
	│   ├── lib/
	│   │   ├── full_source/
	│   │   ├── tutorial_source/
	│   ├─── tests/
	│   │   ├── full_tests/
	│   │   ├── tutorial_tests/

Build Instructions
==================

Simple install requirements, run the build command

    pip install -r docs/requirements.txt
    mynt gen docs build
    (cd build && python -m SimpleHTTPServer)

