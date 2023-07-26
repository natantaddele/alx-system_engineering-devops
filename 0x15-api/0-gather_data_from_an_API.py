import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee information
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch TODO list for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Count the number of completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        # Display the result in the specified format
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

