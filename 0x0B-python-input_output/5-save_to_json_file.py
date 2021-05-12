#!/usr/bin/python3
"""writes json str to file"""


def save_to_json_file(my_obj, filename):
    """write json str to a file"""
    import json
    with open(filename, "w+") as fh:
        try:
            obj = json.dumps(my_obj)
        except:
            raise TypeError("{} is not JSON serializable".format(my_obj))
        else:
            fh.write(obj)
