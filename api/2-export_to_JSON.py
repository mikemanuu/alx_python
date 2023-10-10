#!/usr/bin/python3
""" Exports data in the JSON format. """

import json
import requests
import sys

from requests.api import request


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({"task": task.get(
            'title'), "completed": task.get('completed'), "username": username})
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
