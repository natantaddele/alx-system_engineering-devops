Employee TODO List Progress Script
This Python script allows you to fetch an employee's TODO list progress from a REST API based on their employee ID. It uses the requests module to interact with the API and display the progress in a specific format.

Requirements
Python 3.x
requests module
Installation
Make sure you have Python 3.x installed on your system. If not, you can download it from the official website: https://www.python.org/downloads/

Install the required requests module using pip:

Copy code
pip install requests
Usage
Save the Python script in a file named script.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the script.py file.

Run the script using the following command:

Copy code
python script.py EMPLOYEE_ID
Replace EMPLOYEE_ID with the ID of the desired employee for whom you want to fetch the TODO list progress.

The script will display the employee's progress in the following format:

csharp
Copy code
Employee EMPLOYEE NAME is done with tasks(NUMBER OF DONE TASKS/TOTAL NUMBER OF TASKS):
    TASK_TITLE
    TASK_TITLE
    ...
Example
Copy code
python script.py 1
Output:

csharp
Copy code
Employee Leanne Graham is done with tasks (8/20):
    sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    ...

REST API
The script uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) to fetch employee and TODO list information.

License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute this script as per the terms of the MIT License.
