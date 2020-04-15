#!/usr/bin/python3
""" doc """
import requests

if __name__ == '__main__':

    requestt = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(requestt.text)))
    print("\t- content: {}".format(requestt.content.decode()))
