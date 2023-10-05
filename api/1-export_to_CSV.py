#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches employee todo list and export it to a csv file.
    Args:
        employee_id(int): The id of the employee.
    Returns:
        None
    """
    # Define api urls for employee's details and to_do list.
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:

        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get("id", "Unknown")
        user_name = user_data.get("name", "Unknown")

        # Fetch user todo list
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json

        # Calculate the no of completed and total tasks
        total_tasks = len(todo_response)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        # Display todo list progress
        print(
            f"Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task["completed"]:
                print(f"{task['title']}")

        # Export data to csv
        csv_file_name = f"{user_id}.csv"
        with open(csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todo_data:
                csv_writer.writerow(
                    [user_id, user_name, str(task["completed"]), task["title"]])

        print(f"Data exported to {csv_file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
