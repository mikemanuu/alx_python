#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys


def get_employee_data(employee_id):
    """ Define api urls for employee's details and to_do list. """
    employee = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    to_do = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    """ Fetch employee details and to_do list. """
    employee_response = requests.get(employee)
    to_do_response = requests.get(to_do)

    """ Check if requests are successful. """
    if employee_response.status_code == 200 and to_do_response.status_code == 200:
        employee_data = employee_response.json()
        to_do_data = to_do_response.json()

        """ Check if user_id and user_name are 25 characters long. """
        user_id = f"{employee_id:025}"
        user_name = f"{employee_data['username'][:25]:<25}"

        """ Calculate no. of completed tasks. """
        completed_tasks = len(
            [task for task in to_do_data if task["completed"]])
        total_tasks = len(to_do_data)

        """ Display to_do list progesss. """
        print(f"UserId and Username: {user_id} - {user_name}")
        print(
            f"Employee {employee_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")

        """ Write data to a csv file. """
        csv_file_name = f"{user_id}.csv"
        with open(csv_file_name, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictReader(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            # write the tasks in a row
            for task in to_do_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": user_name,
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print(f"Data exported to {csv_file_name}")
    else:
        print(f"Failed to retrieve data for employee ID {employee_id}")

    # if __name__ == "__main__":

        """ command-line argument for employee_id.
        if len(sys.argv) != 2:
            print("Usage: python 3 script.py <employee_id>")
            sys.exit(1)

        employee_id = int(sys.argv[1])
        get_employee_data(employee_id)
        """
