import json
import yaml

class Serialiser(object):
    @staticmethod
    def list_formats():
        method_prefix = "serialise_"
        format_list = []
        for attr in dir(Serialiser):
            if attr.startswith(method_prefix):
                format_list.append(attr[len(method_prefix):])

        return format_list

    @staticmethod
    def serialise_json(input_dict):
        return json.dumps(input_dict, sort_keys=False)

    @staticmethod
    def serialise_yaml(input_dict):
        return yaml.dump(input_dict, sort_keys=False, explicit_start = True)
