"""Configuration file for the test suite"""

import os
import sys
import pytest

# Cureently sets the system to contain the previous directory
# pylint: disable=no-member
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")
