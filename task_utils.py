from datetime import datetime
# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implemented add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return
    if not validate_task_description(description):
        return
    if not validate_due_date(due_date):
        return
        
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implemented mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Error: Invalid task index.")
    except ValueError:
        print("Error: Please enter a valid numerical index.")

# Implemented view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [t for t in tasks if not t["completed"]]
    if not pending_tasks:
        print("No pending tasks currently.")
        return
        
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i + 1}. [{task['title']}] {task['description']} (Due: {task['due_date']})")

# Implemented calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for t in tasks if t["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress
