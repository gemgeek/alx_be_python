# daily_reminder.py

# Step 1: Get inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Set base message using match case
match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base = f"Note: '{task}' is a low priority task"
    case _:
        base = f"Note: '{task}' has an unknown priority level"

# Step 3: Add time-sensitivity
if time_bound == "yes":
    base += " that requires immediate attention today!"
else:
    base += ". Consider completing it when you have free time."

# Step 4: Output
print()
print(base)

