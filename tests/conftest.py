"""Configuration file for the test suite"""
import os
import sys

# Cureently sets the system to contain the previous directory
MYPATH = os.path.dirname(os.path.asbath(__file__))
sys.path.insert(0, MYPATH + "/../")

def pytest_addoption(parser):
    group = parser.getgroup('assasin')
    group.addoption("--assasin")
