#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_employee_data(employee_id):
    # Fetch employee details
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch employee's TODO list
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    todos_data = todos_response.json()

    # Calculate TODO list progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Display the TODO list progress
    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
