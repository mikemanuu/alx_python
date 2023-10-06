#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

if __name__ == "__main__":

    # pass employee id on command line
    id = sys.argv[1]

    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    # Make api requeats
    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # Parse responses
    todoJson_data = todo_response.json()
    userJson_data = user_response.json()

    # get employee information
    employee_id = userJson_data['username']

    dataList = []

    for data in todoJson_data:
        data_dict = {"userId": data['userId'], "name": employee_id,
                     "completed": data['completed'], "ttitle": data['title']}
        dataList.append(data_dict)

    # csv file path
    csv_file_path = '{}.csv'.format(todoJson_data[0]['userId'])

    # Define filed namwe column headers
    fieldnames = ["userId", "name", "completed", "title"]

    # open csv in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for row in dataList:
            csv_writer.writerow(row)
