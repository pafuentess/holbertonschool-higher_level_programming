#!/usr/bin/python3

from sys import argv
from urllib import request, parse, error

if __name__ == '__main__':

        url = argv[1]
        requestt = request.Request(url)
        try:
                with request.urlopen(requestt) as response:
                        answer = response.read()
                        print(answer.decode())
        except error.HTTPError as errors:
                print("Error code: {}".format(errors.code))
