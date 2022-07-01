"""
General code
"""

# for using logging funtionality
from asyncio.log import logger
import logging
# for interacting with operating system and make it platform-independent
import os
from platform import node
# for interaction with the interpreter
import sys

from matplotlib.pyplot import rc
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

def getText(nodelist):
    """Return the text data in an XML Node"""
    rc = "".join(node.data for node in nodelist if node.nodeType == node.TEXT_NODE)
    return rc

#######
# General Part
#######

class WindowsError(Exception):
    """Dummy class for non-windows systems"""
    def __str__(self):
        return "This is a dummy class for non-Windows systems"

def chownself(path):
    """When running in sudo, set path owner to real self"""
    if os.name != "posix":
        return
    uid = getrealuid()

def getrealuid():
    """Get the real user id when running in sudo mode"""
    if os.name != "posix":
        raise RuntimeError("getrealuid() requires POSIX")
    
    if os.getenv("SUDO_UID"):
        return int(os.getenv("SUDO_UID"))

    try:
        # for getting the username
        login = os.getlogin()
    except:
        login = os.getenv("LOGNAME")

    if login and login != "root":
        import pwd
        return pwd.getpwnam(login)[3]


