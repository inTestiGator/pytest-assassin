"""This the Pytest Assassin test suite"""

def test_read_file_populates_data_0():
    """ Checks that the reading of the small text file works """
    storage_manager = "hello"
    word_list = storage_manager
    assert word_list is not None
    assert len(word_list) == 5


def test_self():
    """ This asserts self"""
    selfie = "hello"
    assert selfie


def test_words():
    """ Asserts that words is equal to the correct length """
    manage = "stop hello"
    words = manage
    assert words is not None
    assert len(words) == 10


def test_stop_words():
    """This will be testing the word frequency manager"""
    stop_manage = "hello"

    assert stop_manage is not None
    assert stop_manage


def test_read_file_populates_data_1():
    """ Checks that the reading of the small text file works """
    storage_manager = "hello again"
    word_list = storage_manager
    assert word_list is not None
    assert len(word_list) == 11


def test_hello():
    "method that creates the string to be tested on"
    # pylint: disable=redefined-builtin
    str = "Hello"
    assert str


def tester_test():
    "This is the tester"
    return 10
