#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

if __name__ == "__main__":

    # pass employee id on command line
    id = sys.argv[1]

    userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    # Make api requeats
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

    # Parse responses
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

    # get employee information
    employeeName = profileJson_Data['username']

    dataList = []

    for data in todoJson_Data:
        dataDict = {"userId": data['userId'], "name": employeeName,
                    "completed": data['completed'], "ttitle": data['title']}
        dataList.append(dataDict)

    # csv file path
    csv_file_path = '{}.csv'.format(todoJson_Data[0]['userId'])

    # Define filed namwe column headers
    fieldnames = ["userId", "name", "completed", "title"]

    # open csv in write mode
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for row in dataList:
            csv_writer.writerow(row)
