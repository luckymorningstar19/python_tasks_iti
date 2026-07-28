tasks_list = []

#create 
def add_task():
    task = input("please fill your task:")
    tasks_list.append({"task": task, "done": False})
    print(f"your task [{task}] is added successfully!")

#view 
def read_task():
    if not tasks_list:
        print('no tasks found!')
        return
    print("these are your tasks:")
    for i, task in enumerate(tasks_list, start=1):
        status = "done" if task["done"] else "pending"
        print(f"{i}- {task['task']} [{status}]")

#update 
def update_task():
    read_task()
    if not tasks_list:
        return
    try:
        index = int(input("enter the task number you want to update:")) - 1
        if 0 <= index < len(tasks_list):
            new_task = input("enter the new task:")
            tasks_list[index]["task"] = new_task
            print(f"task updated successfully to [{new_task}]")
        else:
            print("invalid task number")
    except ValueError:
        print("please enter a valid number")

#delete 
def delete_task():
    read_task()
    if not tasks_list:
        return
    try:
        index = int(input("enter the task number you want to delete:")) - 1
        if 0 <= index < len(tasks_list):
            removed = tasks_list.pop(index)
            print(f"task [{removed['task']}] deleted successfully!")
        else:
            print("invalid task number")
    except ValueError:
        print("please enter a valid number")

#bonus
def mark_done():
    read_task()
    if not tasks_list:
        return
    try:
        index = int(input("enter the task number to mark as done:")) - 1
        if 0 <= index < len(tasks_list):
            tasks_list[index]["done"] = True
            print(f"Task [{tasks_list[index]['task']}] marked as done")
        else:
            print("invalid task number!")
    except ValueError:
        print("please enter a valid number!")

def menu():
    while True:
        print("\nto do list ")
        print("1.add task")
        print("2.view tasks")
        print("3.update task")
        print("4.delete task")
        print("5.mark task as done")
        print("6.exit")
        choice=input("Choose an option:")

        if choice == "1":
            add_task()
        elif choice == "2":
            read_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            print("goodbye")
            break
        else:
            print("Invalid choice, try again")

menu()