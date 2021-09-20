# -*- coding=utf-8 -*-
r"""

"""
from .errors import *
exec(r"""
import sys
if sys.version_info < (3, 6):
    raise PythonVersionError("invalid python version") from None
""")  # check for python version without new variables
from .cmdapp import CommandApp

__author__ = "PlayerG9"
__copyright__ = "Copyright 2021, PlayerG9"
__credits__ = ["PlayerG9"]
__license__ = "MIT"
__version__ = "0.0.1"
__version_info__ = (0,0,1)
__maintainer__ = "PlayerG9"
__email__ = None
__status__ = "Prototype"  # Prototype, Development, Production
