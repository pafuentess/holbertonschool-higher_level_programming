#!/usr/bin/python3


from sys import argv

save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

try:
    f = load_file("add_item.json")
    f += argv[1:]
except Exception:
    f = argv[1:]
save_file(f, "add_item.json")
