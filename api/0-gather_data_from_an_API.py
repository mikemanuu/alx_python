#!/usr/bin/python3
"""Returns information about employee's to-do list progress."""
import requests
import sys


def fetch_employee_data(employee_id):
    """ Define base url for api """
    url = "https://jsonplaceholder.typicode.com"

    """ GET request to retrieve employee information. """
    response = requests.get(f"{url}/users/{employee_id}")

    """ Check if request was successful. """
    if response.status_code == 200:
        employee_data = response.json()
        return employee_data
    else:
        print("Error: Unable to fetch employee data.")
        return None


def fetch_todo_list(employee_id):
    """ Define base url for api """
    url = "https://jsonplaceholder.typicode.com"

    """ GET request to retrieve employee information. """
    response = requests.get(f"{url}/users/{employee_id}/todos")

    """ Check if request was successful. """
    if response.status_code == 200:
        todo_list = response.json()
        return todo_list
    else:
        print("Error: Unable to fetch todo list data.")
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data
    employee_data = fetch_employee_data(employee_id)

    if employee_data:

        # Fetch todo list for employee
        todo_list = fetch_todo_list(employee_id)
        if todo_list:

            # Calculate no of completed tasks
            completed_tasks = [task for task in todo_list if task["completed"]]
            num_completed_tasks = len(completed_tasks)

            # calculate total no of tasks
            total_tasks = len(todo_list)

            # Display employee's information and task progress
            print(
                f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
            for task in completed_tasks:
                print(f"{task['title']}")


if __name__ == "__main__":
    main()
