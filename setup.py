#!/usr/bin/env python3
from distutils.core import setup


setup(name="txtable",
      version="2.0.0",
      description="Plain text tables in Python",
      long_description=open("README.rst").read(),
      author="Károly Kiripolszky",
      author_email="karcsi@ekezet.com",
      url="https://github.com/atomgomba/txtable",
      packages=["txtable", "txtable.formatters"],
      license="UNLICENSE"
      )
