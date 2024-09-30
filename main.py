import json
import datetime
from dataclasses import dataclass
from typing import Optional

# Using a list for month name assignment
MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Using a list for personalized message
MESSAGES = [
    'Good Morning', 'Good Afternoon', 'Good Evening',
    'Late Night', 'Early Morning', 'Welcome Back'
]


# Using a dataclass for the tasks
@dataclass
class Task:
    task: str
    complete: bool = False
    working: bool = False
    completed_at: Optional[datetime.datetime] = None


# Display of time and day
def display():
    current_time = datetime.datetime.now()
    month = MONTHS[current_time.month - 1]
    hour_num = current_time.hour
    message = get_time_message(hour_num)

    # Print formatted date
    print(f"{message}! Today is {month} {current_time.day}, {current_time.year}")


def display_insights(tasks):
    completion_rate = calculate_completion_rate(tasks)
    print(f"\nOverall Task Completion Rate: {completion_rate:.2f}%")
    analyze_completion_patterns(tasks)

def get_time_message(hour_num):
    # Retrieve message using day number
    time_ranges = [
        (3, 6, MESSAGES[4]),  # Early Morning
        (6, 12, MESSAGES[0]),  # Good Morning
        (12, 18, MESSAGES[1]),  # Good Afternoon
        (18, 22, MESSAGES[2]),  # Good Evening
        (22, 24, MESSAGES[3]),  # Late Night
        (0, 3, MESSAGES[3])  # Late Night
    ]

    for start, end, message in time_ranges:
        if start <= hour_num < end:
            return message
        return MESSAGES[5]  # Fallback


# Load the tasks from a file
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return [Task(**task) for task in json.load(file)]
    except FileNotFoundError:
        return []


# Save the tasks to a file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)


# Display the menu
def display_menu():
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark current task (being worked on)")
    print("4. Mark task as complete")
    print("5. Remove task")
    print("6. View insights")
    print("7. Exit")


# Calculate Completion rate
def calculate_completion_rate(tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0
    completed_tasks = sum(1 for task in tasks if task.complete)
    return completed_tasks / total_tasks * 100


# Add task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(Task(task))


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks currently")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task.complete else ""
            working_status = "Current Task" if task.working else ""
            print(f"{index}. {task.task} - {status}{working_status}")


# Mark task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = safe_input("Enter the number of the task to mark as completed: ")
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1].complete = True
        tasks[task_num - 1].completed_at = datetime.datetime.now()
        print(f"Task '{tasks[task_num - 1].task}' is now marked as completed")
    else:
        print("Invalid task number")


# Mark task as currently being worked on
def mark_task_working(tasks):
    view_tasks(tasks)
    task_num = safe_input("Enter the number of the task to mark as currently working on: ")
    if 0 < task_num <= len(tasks):
        # Set all tasks' working status to False before marking a new one as True
        for task in tasks:
            task.working = False
        tasks[task_num - 1].working = True
        print(f"Task '{tasks[task_num - 1].task}' is now marked as being worked on")
    else:
        print("Invalid task number")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    task_num = safe_input("Enter the number of the task to remove: ")
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number")


def analyze_completion_patterns(tasks):
    time_bins = {hour: 0 for hour in range(24)}
    for task in tasks:
        if task.completed_at:
            hour_completed = task.completed_at.hour
            time_bins[hour_completed] += 1

    print("\nTask Completion Patterns by Hour:")
    for hour, count in time_bins.items():
        print(f"{hour}:00 - {count} completed tasks")


def safe_input(prompt, expected_type=int):
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {expected_type.__name__}.")


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
            mark_task_working(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            display_insights(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("Tasks saved! Exiting...")
            break
        else:
            print("Invalid option, Please Try Again")


if __name__ == "__main__":
    main()

