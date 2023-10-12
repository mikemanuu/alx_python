#!/usr/bin/python3
import csv
import requests
import sys


def get_employee_data(employee_id):
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get('id')
        username = user_data.get('username')

        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create a CSV file for the employee
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header row
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write task data to the CSV
            for task in todos_data:
                csv_writer.writerow(
                    [user_id, username, task["completed"], task["title"]])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

employee_id = int(sys.argv[1])
get_employee_data(1)
