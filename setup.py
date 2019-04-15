"""Setup for pytest-assassin plugin"""

from setuptools import setup

setup(
    name='pytest-assassin',
    version='0.1.0',
    description='A pytest plugin to let users know if tests contain asserts',
    url='url here',
    author='Pytest-Assassin Team',
    author_email='email here',
    license='Pytest-Assasin Copyright ',
    py_modules=['pytest_assassin'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['assassin = pytest_assassin', ], },
)
