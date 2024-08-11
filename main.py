import json
import datetime


# Display of time and day
def display():
    current_time = datetime.datetime.now()
    month_num = current_time.month
    hour_num = current_time.hour

    # Using a list for month name assignment
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Retrieve month name using month number
    month = months[month_num - 1]

    # Using a list for personalized message
    messages = [
        'Good Morning', 'Good Afternoon', 'Good Evening',
        'Late Night', 'Early Morning'
    ]

    # Retrieve message using day number
    if 3 <= hour_num < 6:
        message = messages[4]
    elif 6 <= hour_num < 12:
        message = messages[0]
    elif 12 <= hour_num < 18:
        message = messages[1]
    elif 18 <= hour_num < 22:
        message = messages[2]
    else:
        message = messages[3]

    # Print formatted date
    print(f"{message}! Today is {month} {current_time.day}, {current_time.year}")


# Load the tasks from a file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save the tasks to a file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)


# Display the menu
def display_menu():
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Remove task")
    print("5. Exit")


# Add task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks currently")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")


# Mark task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


# Main function
def main():
    tasks = load_tasks()
    display()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved! Exiting...")
            break
        else:
            print("Invalid option, Please Try Again")


if __name__ == "__main__":
    main()
