#!/usr/bin/python3
""" doc """

import requests
from sys import argv

if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = argv[1]
    password = argv[2]

    try:
        requestt = requests.get(url, auth=(user, password)).json()
        print(requestt["id"])
    except:
        print("None")
