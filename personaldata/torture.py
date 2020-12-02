#!/usr/bin/env python3

import json
import yaml
import unittest
from .personaldata import PersonalData

class PersonalDataTest(unittest.TestCase):
    def test_json(self):
        test_dict = {"name": "test name", "address": "test address", "phone": "test phone"}
        pd = PersonalData(test_dict)
        ret = pd.display("json")
        self.assertIsInstance(ret, str)
        assert json.loads(ret).get("name") == "test name"

    def test_yaml(self):
        test_dict = {"name": "test name", "address": "test address", "phone": "test phone"}
        pd = PersonalData(test_dict)
        ret = pd.display("yaml")
        self.assertIsInstance(ret, str)
        assert yaml.load(ret, Loader=yaml.SafeLoader).get("name") == "test name"

if __name__ == "__main__":
    unittest.main()
