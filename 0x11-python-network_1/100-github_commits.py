#!/usr/bin/python3

import requests
from sys import argv

if __name__ == '__main__':

    repo_name = argv[1]
    owner = argv[2]

    url = "http://api.github.com/repos/" + argv[2] + "/" + argv[1] + "/commits"

    requestt = requests.get(url)
    try:
        answer = requestt.json()
        if len(answer) == 0:
            print("No result")
        else:
            for i in range(0, len(answer)):
                print("{}: {}".format(answer[i].get("sha"), answer[i].get(
                    "commit").get("author").get("name")))
                if i == 9:
                    break

    except ValueError:
        print("Not a valid JSON")
