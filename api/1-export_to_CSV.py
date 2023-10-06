#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys


def fetch_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/1/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()
    return tasks


def export_to_csv(user_id, tasks):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow()

        for task in tasks:
            writer.writerow({"USER_ID": user_id, "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": atr(
                task['completed']), "TASK_TITLE": task['title']})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
