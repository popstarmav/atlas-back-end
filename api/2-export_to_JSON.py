#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO
list progress and exports it to a JSON file.
"""
import json
import requests
import sys


def fetch_employee_data(employee_id):
    try:
        # Fetch employee details
        user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_username = user_data.get('username')
        print(f"DEBUG: Fetched employee username: {employee_username}")

        # Fetch employee's TODO list
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare data for JSON export
        tasks = [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_username
        } for task in todos_data]

        data = {str(employee_id): tasks}

        # Write data to JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, mode='w') as file:
            json.dump(data, file, indent=4)
        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except KeyError:
        print("Invalid employee ID or data format.")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
