print("TO-DO List")
tasks = []
def add_task(a):
    tasks.append(a)
def view_tasks():
    if not tasks:
        print("There is no task")
    else:
        for index, string in enumerate(tasks, start=1):
            print(f"{index}: {string}")
def remove_task(b):
    del tasks[b-1]
def clear_tasks():
    tasks.clear()

menu = """
1. Add Task
2. View Task
3. Remove Task
4. Clear All Task
5. Exit
"""
print(menu)
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter task index to remove: "))
        remove_task(index)
    elif choice == '4':
        clear_tasks()
        print("All tasks cleared.")
    elif choice == '5':
        print("Exited")
        break
    else:
        print("Invalid choice")