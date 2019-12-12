#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1
suma = 0

if (argc == 1):
    print(0)
else:
    for i in argv[1:]:
        suma = suma + int(i)
print(suma)
