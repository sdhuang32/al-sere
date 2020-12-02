#!/usr/bin/env python3

import unittest
from .serialiser import Serialiser

class SerialiserTest(unittest.TestCase):
    test_dict = """\
{"key1": "value1", "key2": "value2", "key3": "value3"}
{"key4": "value4", "key5": "value5", "key6": "value6"}
"""

    def test_json(self):
        self.assertIsInstance(Serialiser.list_formats(), list)
        self.assertIsInstance(Serialiser.serialise_json(self.test_dict), str)

    def test_yaml(self):
        self.assertIsInstance(Serialiser.list_formats(), list)
        self.assertIsInstance(Serialiser.serialise_yaml(self.test_dict), str)


if __name__ == "__main__":
    unittest.main()
