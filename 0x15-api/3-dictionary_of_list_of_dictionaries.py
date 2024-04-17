#!/usr/bin/python3
"""Export data in JSON format."""
import json
import requests
from sys import argv


def export_to_json():
    """Export data in JSON format."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        tasks = response.json()

        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks
        ]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    export_to_json()
