#!/usr/bin/python3
""" Export data in the JSON format. """

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    user_tasks = []
    for task in tasks_data:
        user_tasks.append(
            {
                "username": username,
                "tasks": task.get("completed"),
            }
        )
    todo_dict = {user_id: user_tasks}

    # Export data to json
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(todo_dict, json_file)
