"""
File related utilities
"""

from asyncio.log import logger
import systemaniac
from systemaniac import _

# for using multiple exit functions upon normal program termination 
import atexit
# for making available standard errno system symbols
import errno
# using filename globbing utility
import glob
# using locale support module
import locale
# for using logging funtionality
import logging
# for manipulating time values
import time
# for using temporary files (Backward compatibility reason)
import tempfile
# for interaction with the interpreter
import sys
import subprocess
import string
# for using the result of os.stat() and os.lstat()
import stat
# for using regular expressions
import re
import random
# for interacting with operating system and make it platform-independent
import os
# for using POSIX path or NT path
import os.path

logger = logging.getLogger(__name__)

if os.name == 'nt':
    # for supporting common windows types
    from pywintypes import error as winerror
    # for operations on windows file systems
    import win32file
    import systemaniac.Windows
    # for checking the given path represents an existing directory
    # which is a symbolic link or not 
    os_path_islink = os.path.islink
    os.path.islink = lambda path: os_path_islink(
        path) or systemaniac.Windows.is_junction(path)
    
