#!/usr/bin/env python3

import os
import tempfile
import json
import yaml
import unittest
from .deserialiser import Deserialiser

class DeserialiserTest(unittest.TestCase):
    json_str = """\
{"key1": "value1", "key2": "value2", "key3": "value3"}
{"key4": "value4", "key5": "value5", "key6": "value6"}
"""
    yaml_str = """\
---
key1: value1
key2: value2
key3: value3

---
key4: value4
key5: value5
key6: value6
"""

    def basic(self, format):
        self.assertIsInstance(Deserialiser.list_formats(), list)

        # Check if we get correct dictionaries after applying the deserialisation method.
        method_name = "deserialise_{}".format(format)
        deserialise_method = getattr(Deserialiser, method_name)
        str_name = "{}_str".format(format)
        test_str = getattr(self, str_name)

        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
        fname = f.name
        f.write(test_str)
        f.close()

        ret = deserialise_method(fname)
        self.assertIsInstance(ret, list)
        assert ret[0].get("key1") == "value1"
        assert ret[1].get("key6") == "value6"

        # Check for incorrect format in the input file
        f = open(fname, mode='w')
        if format == "json":
            test_str = getattr(DeserialiserTest, "yaml_str")
        elif format == "yaml":
            test_str = getattr(DeserialiserTest, "json_str")
        f.write(test_str)
        f.close()
        try:
            ret = deserialise_method(fname)
        except Exception as e:
            # Correct, invalid input format, we should error.
            if format == "json" and type(e) == json.decoder.JSONDecodeError:
                pass
            elif format == "yaml" and type(e) == yaml.parser.ParserError:
                pass
            else:
                assert False, "Unknown exception, should raise a related decoding/parsing exception!"
        finally:
            os.unlink(fname)

    def test_json(self):
        self.basic("json")

    def test_yaml(self):
        self.basic("yaml")

if __name__ == "__main__":
    unittest.main()
