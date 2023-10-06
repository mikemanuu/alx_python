#!/usr/bin/python3
""" Export data in the JSON format. """

import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    users_res = requests.get('{}/users'.format(API_URL)).json()
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(lambda x: {'username': user_name, 'task': x.get(
            'title'), 'completed': x.get('completed')}, todos))
