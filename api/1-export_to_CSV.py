#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="\n") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, t.get(
            "completed"), t.get("title")]) for t in todos]
__doc__ = """doc for module"""
