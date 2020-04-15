#!/usr/bin/python3

import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2:
        value = {'q': argv[1]}
    else:
        value = {'q': ''}

    url = "http://0.0.0.0:5000/search_user"
    requestt = requests.post(url, value=value)
    try:
        answer = requestt.json()
        if len(answer) == 0:
            print("No result")
        else:
            print("[{}] {}".format(answer.get("id"), answer.get("name")))
    except ValueError:
        print("Not a valid JSON")
