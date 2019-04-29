"This class allows the pytest to run in the terminal"

import ast
import inspect
import pytest


def pytest_addoption(parser):
    """ Turns features on with "--assassin" option"""
    group = parser.getgroup("assassin")
    group.addoption("--assassin", action="store_true")


def pytest_report_header():
    """ Executuion is run if assassin is presented in terminal """
    # pylint: disable=no-member
    if pytest.config.getoption("assassin"):
        execution()


# def walk():
#     directory = os.listdir("./")
#     for object in directory:
#         if object == "tests":
#             walk = os.walk("tests")
#             print("hi")
#         elif object == "testing":
#             os.walk("testing")
#         else:
#             print("Not a test folder")


def execution():
    """ Checks for the instance of an assert and prints pass or fail """
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
                pass
            elif isinstance(item, ast.Expr):
                pass
            elif isinstance(item, ast.Assert):
                print("Pass")
            else:
                print("Fail")


def pytest_collection_modifyitems(items):
    """ Changes what tests are executed by removing those without an assert """
    nick = []
    for item in items[:]:
        # itemz = inspect.getsource(item)
        # print(inspect.isfunction(item))
        funcItem = item.function
        itemz = inspect.getsource(funcItem)
        chicken = [item for item in ast.parse(itemz).body]
        for itemt in chicken:
            var = False
            item1 = ast.parse(itemt).body
            for i in item1:
                if isinstance(i, ast.Assign):
                    pass
                elif isinstance(i, ast.Expr):
                    pass
                elif isinstance(i, ast.Assert):
                    var = True
                    break
            if var is False:
                print(itemt.name)
                nick.append(itemt.name)
                items.remove(item)
