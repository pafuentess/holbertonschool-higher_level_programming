#!/usr/bin/python3
""" doc """

import requests
from sys import argv


if __name__ == '__main__':

    requestt = requests.get(argv[1])
    print(requestt.headers.get("X-Request-Id"))
