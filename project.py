from task_class import Task
from operator import attrgetter
from tabulate import tabulate


def main():
    # create a dictionary to hold the tasks
    to_do_list = list()

    while True:
        command = input("What would you like to do? (ADD, DELETE, UPDATE, SAVE, DISPLAY, QUIT): ")
        if command.strip().upper() == "ADD":
            print(add_task(to_do_list))
        elif command.strip().upper() == "DELETE":
            print(delete_task(to_do_list))
        elif command.strip().upper() == "UPDATE":
            print(update_task(to_do_list))
        elif command.strip().upper() == "SAVE":
            save_task(to_do_list)
        elif command.strip().upper() == "DISPLAY":
            print(display_task(to_do_list))
        elif command.strip().upper() == "QUIT":
            break
        else:
            print("Invalid command")

# define an add function
def add_task(list):
    try:
        info = input("What task would you like to add?: ")
        due_date = input("Due (MM/DD): ")
        list.append(Task(info, due_date))
        return "Task added!"

    except:
        return "invalid date"


# define a delete function
def delete_task(list):
    try:
        item = input("What task would you like to delete?: ")
        due_date = input("When is this task due? (MM/DD): ")
        task = Task(item, due_date)
        for object in list:
            if str(task) == str(object):
                list.remove(object)
                return "Task deleted!"
        else:
            return "Invalid task"

    except:
        return "Invalid task"


# define an update function
def update_task(task_list):
    try:
        old_item = input("What task would you like to update?: ")
        old_time = input("When is this task due?: ")
        old_task = Task(old_item, old_time)

        for task in task_list:
            if str(old_task) == str(task):
                task_list.remove(task)
                break
        else:
            return "Invalid task"

        new_item = input("What is the new task?: ")
        new_time = input("What is the new time?: ")
        new_task = Task(new_item, new_time)
        task_list.append(new_task)
        return "Task updated!"

    except ValueError:
        return "Invalid date"


# define a save function (text file)
def save_task(list):
    with open("to_do_list.txt", "w") as file:
        file.write(display_task(list))


# define a display funciton (ASCII art)
def display_task(list):
    new_list = []
    list = sorted(list, key=attrgetter("date"))
    headers = ["Task", "Due"]

    for item in list:

        listette = []
        task, due = str(item).split(" due ")
        listette.append(task)
        listette.append(due)
        new_list.append(listette)

    return(tabulate(new_list, headers=headers, tablefmt="fancy_outline"))

if __name__ == "__main__":
    main()
