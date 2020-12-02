import json
import yaml

class Deserialiser(object):
    @staticmethod
    def list_formats():
        method_prefix = "deserialise_"
        format_list = []
        for attr in dir(Deserialiser):
            if attr.startswith(method_prefix):
                format_list.append(attr[len(method_prefix):])

        return format_list

    @staticmethod
    def deserialise_json(input_file):
        output_list = []
        with open(input_file, "r") as infile:
            for json_obj in infile:
                result = json.loads(json_obj)
                output_list.append(result)

        return output_list

    @staticmethod
    def deserialise_yaml(input_file):
        with open(input_file, "r") as infile:
            output_list = list(yaml.load_all(infile, Loader=yaml.SafeLoader))

        return output_list
