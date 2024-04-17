#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    todo_url = main_url + "/user/{}/todos".format(employee_id)
    user_url = main_url + "/users/{}".format(employee_id)
    todo_result = requests.get(todo_url).json()
    user_result = requests.get(user_url).json()

    total_tasks = len(todo_result)
    num_done_tasks = len([todo for todo in todo_result
                         if todo.get("completed")])
    username = user_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(username, num_done_tasks, total_tasks))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
