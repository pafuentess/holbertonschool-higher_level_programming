#!/usr/bin/python3
""" doc """

from sys import argv
import requests

if __name__ == '__main__':

    url = argv[1]
    value = {'email': argv[2]}
    requestt = requests.post(url, value)
    print(requestt.text)
