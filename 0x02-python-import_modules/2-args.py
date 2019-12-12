#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1
if (argc == 0):
    print(argc, "arguments.")
else:
    if (argc == 1):
        print(argc, "argument:")
    else:
        print(argc, "arguments:")
    for i, j in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, j))
