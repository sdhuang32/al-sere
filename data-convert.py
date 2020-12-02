#!/usr/bin/env python3

import sys
import getopt
import json
from lib.deserialiser.deserialiser import Deserialiser
from lib.serialiser.serialiser import Serialiser
from personaldata.personaldata import PersonalData

def usage(exit_code):
    print('\n'.join(["Usage: {} [options] <input file>".format(sys.argv[0]),
                     "Valid options:",
                     "  -h, --help",
                     "\tShow this help menu.",
                     "  -l",
                     "\tShow supported input/output and display formats.",
                     "  -i, --informat",
                     "\tInput format.",
                     "\t(The input file will be parsed in json by default if this option not provided.)",
                     "  -o, --outformat",
                     "\tOutput format.",
                     "  -d, --displayformat",
                     "\tDisplay format.",]))

    print()
    sys.exit(exit_code)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hli:o:",
                                   ["help", "informat=", "outformat="])
    except getopt.GetoptError:
        usage(1)

    input_format = "json"
    output_format = "json"

    for opt in opts:
        if opt[0] in ('-h', '--help'):
            usage(0)
        elif opt[0] == '-l':
            print("Supported input format:")
            print("\t", Deserialiser.list_formats())
            print("Supported output format:")
            print("\t", Serialiser.list_formats())
            return 0
        elif opt[0] in ('-i', '--informat'):
            input_format = opt[1]
        elif opt[0] in ('-o', '--outformat'):
            output_format = opt[1]

    if len(args) != 1:
        usage(1)

    input_file = args[0]
    
    method_name = "deserialise_{}".format(input_format)
    ret = getattr(Deserialiser, method_name)(input_file)
    
    pd_list = []
    for obj in ret:
        pd_list.append(PersonalData(obj))

    for pd in pd_list:
        print(pd.display(output_format))

if __name__ == "__main__":
    sys.exit(main())
