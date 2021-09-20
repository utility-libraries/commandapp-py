# -*- coding=utf-8 -*-
r"""

"""
exec(r"""
import sys
if sys.version_info < (3, 6):
    raise RuntimeError("invalid python version")
""")  # check for python version without new variables
from .cmdapp import CommandApp

__version__ = (0,0,1)
