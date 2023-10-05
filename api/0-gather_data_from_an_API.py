#!/usr/bin/python3
"""Returns information about employee's to-do list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [l.get("title") for l in to_do if l.get("completed") is True]
    print("Employee {} is done with tasks ({}/{}):".format(user.get("name"),
          len(completed), len(to_do)))
    [print("\t {}".format(c)) for c in completed]
