#!/usr/bin/python3

"""Module that imports requeats package and retrieves data from the url."""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    if response.status_code == 200:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)

    else:
        print("Error:", response.status_code)
