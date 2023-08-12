#!/usr/bin/python3

""" Sends a request to the URL and displays the body of the response. """

import requests
import sys

if __name__ == '__main__':

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code:', r.status_code)
        sys.exit(1)

    else:
        print(r.text)
