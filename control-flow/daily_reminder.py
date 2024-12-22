var_task = input("Enter your task: ")
var_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match var_priority:
    case "high" if time_bound =="yes":
        print(f"'{var_task}' is a {var_priority} task that requires immediate attention today.")
    case "medium" | "low" if time_bound =="no":
        print(f"Note: '{var_task}' is a {var_priority} task. Consider completing it when you have free time.")
    case _:
        print("Invalid input.")