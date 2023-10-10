#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Get employee's todo list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Create a CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write todo list data to CSV
        for task in todo_list:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow(
                [user_id, username, task_completed_status, task["title"]])

    print(f"Data exported to {csv_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
