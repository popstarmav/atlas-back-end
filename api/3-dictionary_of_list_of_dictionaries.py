#!/usr/bin/python3
"""
Python script that, using this REST API, 
records all tasks from all employees
and exports them to a JSON file.
"""
import requests
import json


def fetch_all_employees_data():
    try:
        # Fetch all users
        users_response = requests.get('https://jsonplaceholder.typicode.com/users')
        users_response.raise_for_status()  # Check if the request was successful
        users_data = users_response.json()

        # Fetch all tasks
        todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
        todos_response.raise_for_status()  # Check if the request was successful
        todos_data = todos_response.json()

        # Organize tasks by user ID
        data = {}
        for user in users_data:
            user_id = user.get('id')
            username = user.get('username')
            user_tasks = [
                {
                    "username": username,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                for task in todos_data if task.get('userId') == user_id
            ]
            data[str(user_id)] = user_tasks

        # Write data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as file:
            json.dump(data, file, indent=4)
        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except KeyError:
        print("Invalid data format.")
        sys.exit(1)


if __name__ == '__main__':
    fetch_all_employees_data()
