from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) == False:
        return
    if validate_task_description(description) == False:
        return
    if validate_due_date(due_date) == False:
        return
        
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    idx = int(index) - 1
    task = tasks[idx]
    task["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    # Check if there are any pending tasks first
    has_pending = False
    for t in tasks:
        if t["completed"] == False:
            has_pending = True
            
    if has_pending == False:
        print("No pending tasks currently.")
        return

    # Print the pending tasks with a simple counter loop
    counter = 1
    for t in tasks:
        if t["completed"] == False:
            print(str(counter) + ". [" + t["title"] + "] " + t["description"] + " (Due: " + t["due_date"] + ")")
        counter = counter + 1

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0
        
    completed_count = 0
    for t in tasks:
        if t["completed"] == True:
            completed_count = completed_count + 1
            
    progress = (completed_count / len(tasks)) * 100
    return progress
