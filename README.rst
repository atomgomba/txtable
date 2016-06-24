txtable - Plain text tables for Python 3
========================================

Pretty-print tabular data as plain text. Supports Markdown and reStructuredText tables too.

Sample outputs
==============

Default formatter
-----------------

::

    Date        Mobile Operating System  Percent of Usage
    ==========  =======================  ================
    2008-12-01                  Android                 0
    2008-12-01                      iOS             32.56
    2008-12-01                SymbianOS             42.02
    2008-12-01                Series 40                 0
    2008-12-01            BlackBerry OS                 0
    2008-12-01                  Samsung                 0
    2008-12-01                  Unknown                16
    2008-12-01            Windows Phone                 0

Headless formatter
------------------

::

    Date        Mobile Operating System  Percent of Usage
    2008-12-01                  Android                 0
    2008-12-01                      iOS             32.56
    2008-12-01                SymbianOS             42.02
    2008-12-01                Series 40                 0
    2008-12-01            BlackBerry OS                 0

MD formatter
------------

::

    Date       | Mobile Operating System | Percent of Usage
    ---------- | ----------------------- | ----------------
    2008-12-01 |                 Android |                0
    2008-12-01 |                     iOS |            32.56
    2008-12-01 |               SymbianOS |            42.02
    2008-12-01 |               Series 40 |                0
    2008-12-01 |           BlackBerry OS |                0

RST formatter
-------------

::

    +------------+-------------------------+------------------+
    | Date       | Mobile Operating System | Percent of Usage |
    +============+=========================+==================+
    | 2008-12-01 |                 Android |                0 |
    +------------+-------------------------+------------------+
    | 2008-12-01 |                     iOS |            32.56 |
    +------------+-------------------------+------------------+
    | 2008-12-01 |               SymbianOS |            42.02 |
    +------------+-------------------------+------------------+
    | 2008-12-01 |               Series 40 |                0 |
    +------------+-------------------------+------------------+
    | 2008-12-01 |           BlackBerry OS |                0 |
    +------------+-------------------------+------------------+

Installation
============

It's the usual process as with any other Python package:

.. code:: bash

    python3 setup.py install

Or install with pip:

.. code:: bash

    pip3 install txtable

Usage as a module
=================

Default usage:

.. code:: python

    # let's pretty-print a CSV file
    import csv
    from txtable import TextTable

    with open("cities.csv") as f:
        data = list(csv.reader(f))

    # the TextTable constructor takes a sequence type as the first argument
    print(TextTable(data))

Use a formatter (available formatters are DefaultFormatter, HeadlessFormatter, MdFormatter, RstFormatter):

.. code:: python

    print(TextTable(data, formatter=MdFormatter()))

Command-line usage
==================

The command-line interface supports formatting input data in JSON and CSV format. Input can be a list of files or stdin.

.. code:: bash

    cat cities.csv | python3 -m txtable -t csv -f md

.. code:: bash

    curl http://ponydealer.com/api/available.json | python3 -m txtable -t json

Command-line help
-----------------

.. code:: bash

    usage: txtable [-h] [-f FORMATTER] [-t TYPE] [files [files ...]]

    positional arguments:
      files                 Path to input files (json/csv) or read from stdin when
                            empty (default: [])

    optional arguments:
      -h, --help            show this help message and exit
      -f FORMATTER, --formatter FORMATTER
                            Table format: default, headless, md (Markdown) or rst
                            (ReStructuredText) (default: default)
      -t TYPE, --type TYPE  Input data type to read from stdin: json/csv (default:
                            json)

