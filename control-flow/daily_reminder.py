task = input("Enter your task: ").title()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high" if time_bound =="yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case "high" if time_bound =="no":
        print(f"Reminder: '{task}' is a {priority} priority task that requires attetion")
    case "medium" | "low" if time_bound == "yes":
        print(f"'{task}' is a {priority} priority task that task. Consider completing it.")
    case "medium" | "low" if time_bound == "no":
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")