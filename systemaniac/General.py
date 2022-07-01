"""
General code
"""

# for using logging funtionality
from asyncio.log import logger
import logging
# for interacting with operating system and make it platform-independent
import os
# for interaction with the interpreter
import sys
import systemaniac

logger = logging.getLogger(__name__)

#######
# XML Part
#######

def boolstr_to_bool(value):
    """Convert a boolean string to a python boolean"""
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False
    raise RuntimeError("Invalid boolean: '%s'" % value)
    