"""Test to check for assert"""

# print every line of code
# print to prove

import ast
import os

os.walk

testerFile = open("new.py", "r")
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
