#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
exports information about his/her TODO list progress to a json file.
"""
import json
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

    json_data = {employee_id: []}
    for task in todo_result:

        json_data[employee_id].append({
            "task": task["title"],
            "completed": task.get("completed"),
            "username": username
        })

    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(json_data, file)

    print(f"Tasks for user {employee_id} have been exported to {filename}")
