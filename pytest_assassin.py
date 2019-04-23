import os
import sys
import pytest
import ast

assert os  # silence pyflakes
assert sys  # silence pyflakes


def pytest_addoption(parser):
    """ Turns features on with "--assassin" option"""
    group = parser.getgroup("assassin")
    group.addoption("--assassin", action="store_true")


def pytest_report_header():
    """ Thank tester for running tests """
    # pylint: disable=no-member
    if pytest.config.getoption("assassin"):
        execution()


def pytest_report_teststatus(report):
    """ Turn failures into opportunities """
    if report.failed and pytest.config.getoption("assassin"):
        print(report.outcome, "O", "OPPORTUNITY for improvement")
    else:
        print("Thanks Running Tests")


def execution():
    """ undocumented """
    testerFile = open("tests/test_new.py", "r")
    nodes = [
        item
        for item in ast.parse(testerFile.read()).body
        if isinstance(item, ast.FunctionDef)
    ]
    for node in nodes:
        items = [item for item in ast.parse(node).body]
        for item in items:
            if isinstance(item, ast.Assign):
                print("Ignore")
            elif isinstance(item, ast.Assert):
                print("Pass")
            else:
                print("Fail")
