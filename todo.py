#!/usr/bin/env python3
"""
Simple To-Do List CLI for DecodeLabs Internship Project 1.

Features:
- Stores tasks in a list called `my_tasks`.
- Add/View/Delete tasks from the list.
- Save to / load from a JSON file `tasks.json`.

Author: Suhail (suhailapvak)
"""

import json
import os

# File used to persist tasks
TASKS_FILE = "tasks.json"

# List to store tasks in memory
my_tasks = []


def load_tasks():
    """Load tasks from TASKS_FILE into `my_tasks`.

    If the file does not exist, `my_tasks` remains empty.
    Handles JSON errors gracefully.
    """
    global my_tasks
    if not os.path.exists(TASKS_FILE):
        print(f"No existing {TASKS_FILE} found — starting fresh.")
        return

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                my_tasks = data
                print(f"Loaded {len(my_tasks)} task(s) from {TASKS_FILE}.")
            else:
                print(f"Invalid data in {TASKS_FILE}; expected a list.")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Failed to load tasks: {e}")


def save_tasks():
    """Save `my_tasks` to TASKS_FILE in JSON format."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(my_tasks, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(my_tasks)} task(s) to {TASKS_FILE}.")
    except IOError as e:
        print(f"Failed to save tasks: {e}")


def add_task():
    """Prompt the user to add a new task to `my_tasks`."""
    task = input("Enter the new task: ").strip()
    if task:
        my_tasks.append(task)
        print(f"Added task: {task}")
    else:
        print("Empty task not added.")


def view_tasks():
    """Display all tasks with numbers. Shows a friendly message when empty."""
    if not my_tasks:
        print("No tasks yet!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(my_tasks, start=1):
        print(f"{i}. {task}")
    print()


def delete_task():
    """Delete a task by its number (as shown by view_tasks())."""
    if not my_tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    choice = input("Enter the number of the task to delete: ").strip()
    try:
        index = int(choice)
        if 1 <= index <= len(my_tasks):
            removed = my_tasks.pop(index - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    """Print the menu options for the user."""
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Save tasks to a JSON file (tasks.json)")
    print("5. Load tasks from JSON file (tasks.json)")
    print("6. Exit")


def main():
    """Main loop for the CLI.

    Loads tasks on startup and then shows the menu until the user exits.
    """
    # Load tasks from disk when program starts (requirement 5)
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            # Allow user to reload tasks from file during the session
            load_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices gracefully
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted — exiting.")
