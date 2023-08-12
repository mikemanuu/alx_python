#!/usr/bin/python3
""" Displays the X-Request-Id header variable of a request to a given URL. """

import sys
import requests

url = sys.argv[1]
print(response.headers.get("X-Request-Id"))
