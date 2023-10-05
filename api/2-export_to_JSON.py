#!/usr/bin/python3
""" Exports data in the JSON format. """

import json
import requests
import sys


def get_employee_data(employee_id):
    """
    Fetches employee data and their todo list, then exports it to a json file.
    Args:
        employee_id(int): The id of the employee for whom data is to be fetched and exported.
    Retruns: None
    """

    employee = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    to_do = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee)
    to_do_response = requests.get(to_do)

    if employee_response.status_code == 200 and to_do_response.status_code == 200:
        employee_data = employee_response.json()
        to_do_data = to_do_response.json()

        json_data = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_data["username"]
                }
                for task in to_do_data
            ]
        }

        json_file_name = f"{employee_id}.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_file_name}")

    else:
        print(f"Failed to retreive data for employee ID {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 3 script.py <employee>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
