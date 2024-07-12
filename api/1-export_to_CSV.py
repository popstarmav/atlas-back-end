#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO
list progress and exports it to a CSV file.
"""
import csv
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
        employee_name = user_data.get('username')
        print(f"DEBUG: Fetched employee username: {employee_name}")

        # Fetch employee's TODO list
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Write data to CSV file
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_name,
                    task.get('completed'),
                    task.get('title')
                ])
        print(f"Data exported to {csv_filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except KeyError:
        print("Invalid employee ID or data format.")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
