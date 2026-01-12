# To-Do List Application
# CodSoft Internship - Task 1

tasks = []


def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "status": "Pending"})
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks found.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")
    print()


def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as Done: "))
        tasks[num - 1]["status"] = "Done"
        print("Task updated!\n")
    except:
        print("Invalid input.\n")


def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!\n")
    except:
        print("Invalid input.\n")


while True:
    print("----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
