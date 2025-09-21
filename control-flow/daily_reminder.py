# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_text = "a high priority task"
    case "medium":
        priority_text = "a medium priority task"
    case "low":
        priority_text = "a low priority task"
    case _:
        priority_text = "a task"

if time_bound == "yes":
    print("Reminder:", "'" + task + "'", "is", priority_text, "that requires immediate attention today!")
else:
    print("Note:", "'" + task + "'", "is", priority_text + ".", "Consider completing it when you have free time.")
