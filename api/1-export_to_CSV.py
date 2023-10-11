#!/usr/bin/python3
""" Exports data in the CSV format. """
import csv
import os
import requests
import sys


def user_info(employee_id):
    # Fetch employee information
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if employee_response.status_code != 200:
        print("Error: Unable to fetch employee data.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name", "Unknown Employee")
    employee_username = employee_data.get("username", "Unknown Username")

    # Fetch employee's tasks
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch tasks for employee ID {employee_id}.")
        return

    todo_data = todos_response.json()

    # Create csv
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow(
                [employee_name, employee_username, task_completed_status, task["title"]])

    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_o.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        user_info(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
