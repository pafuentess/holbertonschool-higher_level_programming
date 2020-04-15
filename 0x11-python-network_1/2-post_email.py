#!/usr/bin/python3
""" doc """

from sys import argv
from urllib import request, parse

if __name__ == '__main__':

    url = argv[1]
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    requestt = request.Request(url, data)

    with request.urlopen(requestt) as response:
            answer = response.read()
            print(answer.decode())
