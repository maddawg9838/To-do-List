# To-Do List Application

## Overview
This Python-based To-Do List application allows users to manage their tasks efficiently. Users can add, view, mark, and remove tasks, while also receiving a personalized greeting based on the current time of day.

## Features
- **Personalized Greeting**: Displays a greeting based on the time of day.
- **Task Management**: Add, view, complete, and remove tasks
- **Persistent Storage**: Tasks are saved to and loaded from a JSON file (tasks.json).

## Prerequisites
- Python 3.x installed on your system

## How to Use
1. **Clone the Repository**:
```bash
git clone https://github.com/yourusername/todo-list.git
cd todo-list
```
2. **Run the Application**:
```bash
python todo.py
```
3. **Interacting with the Application**:
- Choose from the displayed menu options to manage your tasks
- Follow prompts to add, view, complete, or remove tasks
- Tasks are automatically saved when you exit

## Code Overview
The application is structured around several functions, each handling a specific task

### Key Functions
- display(): Displays the current data and a personalized greeting
- load_tasks(filename): Loads tasks from a JSON file
- save_tasks(tasks, filename): Saves tasks to a JSON file
- display_menu(): Displays the menu options to the user.
- add_task(tasks): Adds a new task to the list.
- view_tasks(tasks): Displays the current tasks with their statuses.
- mark_task_completed(tasks): Marks a selected task as completed.
- remove_task(tasks): Removes a selected task from the list.

## Author
Madison Humphries
