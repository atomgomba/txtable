#!/usr/bin/env python3
import os
from setuptools import setup

if __name__ == "__main__":
    setup(name="txtable",
          version="2.1.2",
          description="Plain text tables for Python 3",
          long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
          author="Károly Kiripolszky",
          author_email="karcsi@ekezet.com",
          url="https://github.com/atomgomba/txtable",
          packages=["txtable", "txtable.formatters"],
          license="UNLICENSE",
          test_suite="txtable.tests"
          )
