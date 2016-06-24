#!/usr/bin/env python3
import os
from distutils.core import setup


setup(name="txtable",
      version="2.0.1",
      description="Plain text tables in Python",
      long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
      author="Károly Kiripolszky",
      author_email="karcsi@ekezet.com",
      url="https://github.com/atomgomba/txtable",
      packages=["txtable", "txtable.formatters"],
      license="UNLICENSE"
)
