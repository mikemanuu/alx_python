#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]

    userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

    employeeName = profileJson_Data['username']

    dataList = []

    for data in todoJson_Data:
        dataDict = {"userId": data['userId'], "name": employeeName,
                    "completed": data['completed'], "title": data['title']}
        dataList.append(dataDict)

    csv_file_path = '{}.csv'.format(todoJson_Data[0]['userId'])

    fieldnames = ["userId", "name", "completed", "title"]

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        for row in dataList:
            csv_writer.writerow(row)
