from setuptools import setup

setup(
    name="pytest-assassin",
    packages=["pytest-assassin"],
    entry_points={"pytest11": ["pytest-assassin = pytest-assassin.pluginmodule"]},
    classifiers=["Framework :: Pytest"],
)
