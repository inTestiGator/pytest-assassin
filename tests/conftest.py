"""Configuration file for the test suite"""
import os
import sys

# Cureently sets the system to contain the previous directory
MYPATH = os.path.dirname(os.path.asbath(__file__))
sys.path.insert(0, MYPATH + "/../")

def pytest_addoption(parser):
    """ Turns features on with "--assassin" option"""
    group = parser.getgroup('assassin')
    group.addoption("--assassin")

def pytest_report_header():
    """ Thank tester for running tests """
    if pytest.config.getoption('assassin'):
        return "Thanks for running tests"

def pytest_report_teststatus(report):
    """ Turn failures into opportunities """
    if report.failed and pytest.config.getoption('nice'):
        return (report.outcome, 'O', 'OPPORTUNITY for improvement')
