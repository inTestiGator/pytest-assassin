def test_read_file_populates_data_0():
    """ Checks that the reading of the small text file works """
    storage_manager = compute_tf_objectoriented.DataStorageManager("inputs/input.txt")
    word_list = storage_manager.words()
    assert word_list is not None
    assert len(word_list) == 12


def test_self():
    """ This asserts self"""
    selfie = compute_tf_objectoriented.TFExercise()
    assert selfie


def test_words():
    """This asserts words"""
    manage = compute_tf_objectoriented.DataStorageManager("stopwords/stop_words.txt")
    words = manage.info()
    assert words is not None
    assert len(words) == 52


def test_stop_words():
    """This will be testing the word frequency manager"""
    stop_manage = compute_tf_objectoriented.WordFrequencyManager()

    assert stop_manage is not None
    # pylint: disable=len-as-condition
    assert stop_manage


def test_read_file_populates_data_1():
    """ Checks that the reading of the small text file works """
    storage_manager = compute_tf_objectoriented.DataStorageManager(
        "stopwords/stop_words.txt"
    )
    word_list = storage_manager.words()
    assert word_list is not None
    assert len(word_list) == 1

"This is the example test file"


def test_nick_sucks():
    "this method creates the string to test"
    # pylint: disable=redefined-builtin
    str = "Hello"
    assert str


def tester_test():
    "This is the tester"
    return 10


# pylint: disable=pointless-statement
# pylint: disable=undefined-variable
x + 10

