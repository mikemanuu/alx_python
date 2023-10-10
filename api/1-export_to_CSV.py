#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # getting user info
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url)
    user_data = user.json()

    # getting todo info

    todos_url = 'https://jsonplaceholder.typicode.com/users/1/todos'.format(
        user_id)
    todos = requests.get(todos_url)
    todos_data = todos.json()

    # Export data to csv
    csv_file = "{}.csv".format(user_id)
    with open(csv_file, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        for task in todos_data:
            csv_writer.writerow(
                [user_id, str(user_data['name']), task['completed'], task['title']])
