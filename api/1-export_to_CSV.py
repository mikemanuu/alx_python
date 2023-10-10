#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

# Not executed
if __name__ == "__main__":

    # Pass employee id on command line
    id = sys.argv[0]

# API
    userTodoURL = "https://jsonplaceholder.typicode.com/users/1/todos".format(
        id)
    userProfile = "https://jsonplaceholder.typicode.com/users/1".format(id)

# APIs requests
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

# Parse responses
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

# Get employee information
    employeeName = profileJson_Data['username']

    dataList = []

    for data in todoJson_Data:
        dataDict = {"userId": data['userId'], "name": employeeName,
                    "completed": data['completed'], "title": data['title']}
        dataList.append(dataDict)

# Specify csv filepath
    csv_file_path = '{}.csv'.format(todoJson_Data[0]['userId'])

# Define the fieldnames
    fieldnames = ["userId", "name", "completed", "title"]

# Open csvfile in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

# Write data rows
        for row in dataList:
            csv_writer.writerow(row)
