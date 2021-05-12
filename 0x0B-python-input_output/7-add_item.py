#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
x = 1
if len(argv) == 1:
    with open("add_item.json", "w") as fh:
        fh.write("[]")
else:
    try:
        st = load_from_json_file("add_item.json")
        print("HERE")
        print(st)
    except:
        st = list()
    finally:
        if type(st) is list:
            while x < len(argv):
                st.append(argv[x])
                x += 1
        save_to_json_file(st, "add_item.json")
