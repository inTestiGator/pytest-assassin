# Pytest-Assassin

  ![picture](images/assassinpic.jpg)

  [![Build Status](https://api.travis-ci.com/inTestiGator/pytest-assassin.svg?branch=master)](https://travis-ci.com/inTestiGator/pytest-assassin)
  [![codecov.io](http://codecov.io/github/inTestiGator/pytest-assassin/coverage.svg?branch=master)](http://codecov.io/github/inTestiGator/pytest-assassin?branch=master)

  Pytest-Assassin is a plugin for pytest that allows users to have the ability
  to check and see if their test cases contain assert statements or not. This
  will help with the problem of useless test cases that are not doing anything
  for the program.

## Features

  Welcome to Pytest-Assassin! Here at Pytest-Assassin, we want to destroy the
  test cases that is wrong for your program. Our key features are checking for asserts
  within your test cases. We are confident that mostly everyone has written a test
  case that either assert nothing or makes sure that a container, if you will, is
  filled. While the latter is not bad, it is not what a program needs! A program
  needs test cases that will run through the function, take the expected output
  and compare it to the actual output. So in other words, a program needs Pytest Assassin!

## Requirements

  In order to run Pytest Assassin, the user will need the Python version 3.6.7.
  The user will need the Pipenv version 2018.11.26.

  If the user does not have the correct version of Pipenv, follow the link below.
  [![Pyenv Version Directions](https://pypi.org/project/pipenv/)

  If the user does not have the correct version of Pytest, follow the link below.
  [![Python Version Directions](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)


## Installation

  Installation for Pytest Assassin, as of now, requires the cloning of its repository.
  This requires command-line interface, using the line:

  ```
  git clone git@github.com:inTestiGator/pytest-assassin.git
  ```

  Once completing that step, the next part is running Pytest Assassin! First, you
  must install the dependencies of pipenv by running the command:

  ```
  pipenv install --dev
  ```

  To follow that, it is important and a must to create a shell within your terminal
  window in order to run Pytest Assassin. Therefore, run this command in your terminal
  to open a shell:
  ```
  pipenv shell
  ```

  Next, it is needed to run the setup of Pytest Assassin, so it builds and is
  ready with the needed code. This requires you to type:

  ```
  python3 setup.py install
  ```

  Now, what we all have been waiting for, you run Pytest Assassin!!!

  ```
  pytest --assassin
  ```


## Usage

  For further use on the same project, as long as you are in the shell
  you are only requires to run:

  ```
  python3 setup.py install
  ```

  and

  ```
  pytest --assassin
  ```


## Example Output

  ```
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Fail
rootdir: /Users/mcorletti/Desktop/Software Engineering/pytest-assassin
plugins: xdist-1.27.0, sugar-0.9.2, forked-1.0.2, cov-2.6.1, assassin-0.1.0
collecting ... Fail
tester_test

 tests/test_new.py ✓✓✓✓✓✓                                        100% ██████████

Results (0.08s):
       6 passed
```
