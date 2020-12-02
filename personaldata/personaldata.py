import json
from lib.serialiser.serialiser import Serialiser

class PersonalData(object):
    def __init__(self, input_dict):
        self.__name = input_dict.get("name")
        self.__address = input_dict.get("address")
        self.__phone = input_dict.get("phone")

    def display(self, output_format):
        output_dict = { "name": self.__name, "address": self.__address, "phone": self.__phone }
        method_name = "serialise_{}".format(output_format)
        return getattr(Serialiser, method_name)(output_dict)
