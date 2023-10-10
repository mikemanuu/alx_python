#!/usr/bin/python3
"""Returns information about employee's to-do list for a given employee id."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_employee = requests.get(employee_url)
    employee_data = response_employee.json()
    employee_name = employee_data.get("name")

    # Get employee's todo list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response_todo = requests.get(todo_url)
    todo_list = response_todo.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])
    in_progress_tasks = total_tasks - completed_tasks

    # Display progress
    print(
        f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_list:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

get_employee_todo_progress(1)
