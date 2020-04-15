#!/usr/bin/python3

from sys import argv
import requests

if __name__ == '__main__':

        url = argv[1]
        requestt = requests.get(url)
        try:
                requestt.raise_for_status()
                print(requestt.text)
        except:
                print("Error code: {}".format(requestt.status_code))
