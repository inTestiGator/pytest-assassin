"""Configuration file for the test suite"""

import os
import sys
import pytest

# Cureently sets the system to contain the previous directory
# pylint: disable=no-member
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")


def pytest_addoption(parser):
    """ Turns features on with "--assassin" option"""
    group = parser.getgroup("assassin")
    group.addoption("--assassin", action = "store_true")


def pytest_report_header():
    """ Thank tester for running tests """
    # pylint: disable=no-member
    if pytest.config.getoption("assassin"):
        print ("Thanks for running tests")



def pytest_report_teststatus(report):
    """ Turn failures into opportunities """
    if report.failed and pytest.config.getoption("assassin"):
        print (report.outcome, "O", "OPPORTUNITY for improvement")
    else:
        print ("Thanks Running Tests")
