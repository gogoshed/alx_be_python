def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Consider completing it as soon as possible."
        case "medium":
            reminder = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that needs to be done today."
            else:
                reminder += ". You can complete it when you have some free time."
        case "low":
            reminder = f"'{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " that you should try to finish today."
            else:
                reminder += ". Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level."

    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()