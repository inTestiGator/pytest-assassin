"""This File will iterate through to see if the test cases contain an assert"""

import ast
import inspect
import enum
import dis
import types

class ASSERT_TYPES(enum.IntEnum):
    passes = True
    fails = False

    def __str__(self):
        return NOTATION_REPR[self]

NOTATION_REPR = {
    True: `passes`,
    False: `fails`,
}
