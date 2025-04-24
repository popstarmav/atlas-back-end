# API Data Extraction Project

## Overview

This project focuses on working with REST APIs to extract, process, and export employee data in various formats. It demonstrates how to interact with a JSON API, parse the returned data, and export it to CSV and JSON formats.

## Project Structure

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Script to fetch and display an employee's TODO list progress |
| `1-export_to_CSV.py` | Script to export employee TODO list data to CSV format |
| `2-export_to_JSON.py` | Script to export a single employee's TODO list data to JSON format |
| `3-dictionary_of_list_of_dictionaries.py` | Script to export all employees' TODO list data to JSON format |
| `2.csv` | Example CSV output from script 1 |
| `2.json` | Example JSON output from script 2 |
| `todo_all_employees.json` | Example JSON output from script 3 with all employees' data |

## Requirements

- Python 3.8.5 or later
- Libraries: `requests`, `json`, `csv`, `sys`
- All files should end with a new line
- First line of all files should be `#!/usr/bin/python3`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Code should follow PEP8 style (version 2.8.0)
- All files must be executable

## API Used

The project uses the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API, which provides fake data for testing and prototyping. Specifically, it uses:

- `/users` - To get user information
- `/todos` - To get TODO list items

## Scripts Description

### 0-gather_data_from_an_API.py

This script takes an employee ID as a parameter and returns information about their TODO list progress.

```bash
./0-gather_data_from_an_API.py 2

Execute

Output format:

Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE
    TASK_TITLE
    ...



1-export_to_CSV.py
This script exports an employee's TODO list data to a CSV file.

./1-export_to_CSV.py 2

Execute

The CSV file will be named USER_ID.csv and will have the format:

"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"



2-export_to_JSON.py
This script exports an employee's TODO list data to a JSON file.

./2-export_to_JSON.py 2

Execute

The JSON file will be named USER_ID.json and will have the format:

{"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}



3-dictionary_of_list_of_dictionaries.py
This script exports all employees' TODO list data to a single JSON file.

./3-dictionary_of_list_of_dictionaries.py

Execute

The JSON file will be named todo_all_employees.json and will have the format:

{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}



Examples
Example of todo_all_employees.json
{
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": false},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": false},
        ...
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": true},
        ...
    ],
    ...
}



Learning Objectives
Understanding REST APIs and how to interact with them
Working with API endpoints and parameters
Parsing JSON data in Python
Exporting data to different formats (CSV, JSON)
Handling command-line arguments in Python scripts
