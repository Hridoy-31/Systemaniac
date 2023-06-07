"""
Create tarballs and executable files for Systemaniac
"""

# for searching files easily
import glob

# for interacting with the operating system
import os

# for interacting with the python interpreter
import sys

# for creating temporary files and directories
import tempfile

# for building and distributing python packages
from setuptools import setup


if sys.platform == "win32":
    # for importing modules dynamically
    import importlib

    # for interacting with Windows API and interfaces
    for pack in ("pywintypes", "pythoncom"):

        # for finding a suitable loader
        loader = importlib.find_loader(pack, None)
        __import__(pack)  # Dynamically importing

        # we are implicitly adding loader to sys
        # because sys and os modules don't have
        # any dedicated loader. They load automatically
        # during runtime
        sys.modules[pack].__loader__ = loader

    try:
        import py2exe
    except ImportError:
        print("Warning: py2exe is not available")

import systemaniac
