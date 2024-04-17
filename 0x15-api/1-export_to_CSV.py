#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
exports information about his/her TODO list progress to a CSV file.
"""

import csv
import requests
import sys

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    todo_url = main_url + "/user/{}/todos".format(employee_id)
    user_url = main_url + "/users/{}".format(employee_id)
    todo_result = requests.get(todo_url).json()
    user_result = requests.get(user_url).json()

    username = user_result.get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # writer.writerow(
        #     ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todo_result:
            task_completed_status = ("True" if todo.get("completed")
                                     else "False")
            task_title = todo.get("title")
            writer.writerow(
                [employee_id, username, task_completed_status, task_title])
