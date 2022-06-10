"""
Basic GUI code
"""

from systemaniac import _

import os

try:
    import gi
except ModuleNotFoundError as e:
    print('#'*60)
    print("Please install PyGObject")
    print("https://pygobject.readthedocs.io/en/latest/getting_started.html")
    print('#'*60)
    raise e

