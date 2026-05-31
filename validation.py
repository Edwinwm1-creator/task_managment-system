from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        print("Error: Title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        print("Error: Description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    if len(due_date.strip()) == 0:
        print("Error: Due date cannot be empty.")
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False
