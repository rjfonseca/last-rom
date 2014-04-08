last-rom
========
I wrote this program to supply a demand of a friend in keeping tabs on new releases of his favorite android roms.

For this first release, the program only work with one rom family.

This project is not under active development since it depends on my free time. Anyone who wants to collaborate, fell free to join.

Running
-------

First of all, check the Requirements section of this document.

If you have installed the scripts:

	python -m lastrom.n7000

If you want to run them as a standalone:

	python lastrom/n7000.py

Requirements
------------

* Python 2.7
* lxml python module

To install lxml module from pip you will need some development packages: libxml2-dev, libxslt-dev, python-dev and lib32z1-dev.

If you are using a apt based Linux distro:

	sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev

then

	pip install -r requirements.txt

or you could install the lxml from the official repository.

	sudo apt-get install python-lxml

Installing
----------

You can run the scripts as standalone scripts or install them. To install the script:

	pip -e .

or

	python setup.py install

