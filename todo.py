FILE = "tasks.txt"


def load_tasks():
    try:
        with open(FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\n Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(" Task added!")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f" Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid choice.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do App ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid option.")


main()
