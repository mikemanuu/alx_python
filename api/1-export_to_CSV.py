#!/usr/bin/python3
""" Exports data in the CSV format. """

import csv
import requests
import sys

id = sys.argv[1]
request = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
request1 = requests.get(
    'https://jsonplaceholder.typicode.com/user' + id + '/todos')
data = request.json()
data1 = request1.json()
completed = 0
tasks = []

for i in data1:
    if i.get('completed') == True:
        completed = completed + 1
        tasks.append([id, data.get('name'), "Completed", i.get('title')])
    else:
        tasks.append([id, data.get('name'), "Not Completed", i.get('title')])

csv_file = "{}.csv".format(id)

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(tasks)

print(
    f'Employee {data.get("name")} is done with tasks ({completed}/{len(data1)}):')
for item in data1:
    if item.get('completed') == True:
        print(f'\t {item.get("title")}')

print(f'Data exported to {csv_file}.')
