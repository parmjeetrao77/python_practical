tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Run tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter task name: ")
        condition = input("Run this task? (yes/no): ").lower()

        tasks.append({
            "name": name,
            "condition": condition
        })
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        for i, task in enumerate(tasks, 1):
            print(i, task["name"], "-", task["condition"])

    elif choice == "3":
        for task in tasks:
            if task["condition"] == "yes" and task["name"]:
                print("Executing task:", task["name"])
            else:
                print("Skipping task:", task["name"])

    elif choice == "4":
        print("Scheduler closed.")
        break

    else:
        print("Invalid choice.")